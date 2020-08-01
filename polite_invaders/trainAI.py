import pygame
import neat
import os
import random
from reference import *
from enemy_ship import enemyShip, enemyShipCreeper, enemyShipDeathStar, enemyShipCookie
from player_ship import playerShip
from star import Star
from projectile import Projectile, MailProjectile
from apology import Apology

"""Music: www.bensound.com" or "Royalty Free Music from Bensound"""


def make_decision(network, player_ship, enemy_ship):
    go_left = 0
    go_right = 0
    stay = 0
    shoot = 0

    if enemy_ship is not None:
        x_dist = enemy_ship.x - player_ship.x_velocity
        if x_dist > 0:
            go_right = 1
        elif x_dist < 0:
            go_left = 1
        else:
            stay = 1

        if abs(x_dist) < 10:
            shoot = 1
    else:
        stay = 1

    inputs = tuple([go_left, go_right, stay, shoot])

    decision = network.activate(inputs)
    return decision


def get_closest_enemy(enemy_ships):
    if len(enemy_ships) > 0:
        chosen = enemy_ships[0]
        y = (WIN_HEIGHT-70) - chosen.y
        for enemy_ship in enemy_ships:
            cur_y = (WIN_HEIGHT-70) - enemy_ship.y
            if cur_y < y:
                chosen = enemy_ship
                y = cur_y
        return chosen
    else:
        return None


def create_mail(mail_list, x):
    y = WIN_HEIGHT-80
    mail_projectile = MailProjectile(x, y)
    mail_list.append(mail_projectile)


def create_stars():
    star_set = set()

    count = 0
    while count < 50:
        x = random.randint(5, WIN_WIDTH - 5)
        y = random.randint(5, WIN_HEIGHT - 5)
        star = Star(x, y)
        if star not in star_set:
            star_set.add(star)
            count += 1

    return star_set


def add_enemy(enemy_ships):
    x = random.randrange(10, WIN_WIDTH - 80)
    y = 10
    n = random.randint(1, 3)

    if n == 1:
        enemy_ships.append(enemyShipCreeper(x, y))
    elif n == 2:
        enemy_ships.append(enemyShipDeathStar(x, y))
    elif n == 3:
        enemy_ships.append(enemyShipCookie(x, y))
    return enemy_ships


def eval_edge_projectiles(mail_list):
    to_remove = list()
    for mail_projectile in mail_list:
        if mail_projectile.y > WIN_HEIGHT-50:
            to_remove.append(mail_projectile)

    for mail_projectile in to_remove:
        mail_list.remove(mail_projectile)


def eval_edge_enemies(genome, enemy_ships, star_set):
    to_remove = list()
    for enemy_ship in enemy_ships:
        if enemy_ship.y > WIN_HEIGHT-50:
            genome.fitness -= 1.5
            return False
        elif enemy_ship.y < 10:
            to_remove.append(enemy_ship)

    for ship in to_remove:
        enemy_ships.remove(ship)
    return True


def draw(window, star_set, mail_list, player_ship, enemy_ships, apologies, score, time_in_s):
    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    for mail_projectile in mail_list:
        mail_projectile.draw(window)

    for enemy_ship in enemy_ships:
        enemy_ship.draw(window)

    for apology in apologies:
        apology.draw(window)

    font = pygame.font.Font(resource_path+"/comicsans.ttf", 30)
    text = font.render("Score: "+str(score), True, (255, 255, 255))
    window.blit(text, (10, 5))

    text = font.render("Time: "+str(time_in_s), True, (255, 255, 255))
    window.blit(text, (WIN_WIDTH - 120, 5))

    player_ship.draw(window)

    pygame.display.update()


def eval(genomes, config):

    for _, genome in genomes:
        network = neat.nn.FeedForwardNetwork.create(genome, config)
        genome.fitness = 0

        global MAX_ENEMY_TICK

        isRunning = True
        score = 0
        star_set = create_stars()
        mail_list = list()
        player_ship = playerShip(WIN_WIDTH//2, WIN_HEIGHT-70)
        enemy_ships = add_enemy(list())
        apologies = list()
        enemy_tick = MAX_ENEMY_TICK
        projectile_tick = PROJECTILE_TICK
        clear_text_tick = CLEAR_TEXT_TICK

        start_time = pygame.time.get_ticks()

        prev_closest_enemy = get_closest_enemy(enemy_ships)
        prev_dist_x = abs(player_ship.x - prev_closest_enemy.x)

        while isRunning:
            game_clock.tick(1000)

            if score >= 42:
                isRunning = False
                break

            time_elapsed_in_s = round(
                (pygame.time.get_ticks() - start_time)/1000)

            if time_elapsed_in_s >= 900:
                isRunning = False
                break

            if clear_text_tick < 1:
                if len(apologies) > 0:
                    apologies.pop(0)
                clear_text_tick = CLEAR_TEXT_TICK
            else:
                clear_text_tick -= 1

            if enemy_tick < 1:
                enemy_tick = MAX_ENEMY_TICK
                enemy_ships = add_enemy(enemy_ships)
            enemy_tick -= 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    isRunning = False
                    pygame.quit()
                    exit(0)

            closest_enemy = get_closest_enemy(enemy_ships)
            decision = make_decision(network, player_ship, closest_enemy)
            max_val = max(decision[:3])

            if decision[0] == max_val:
                player_ship.move("L")
            elif decision[1] == max_val:
                player_ship.move("R")
            elif decision[2] == max_val:
                player_ship.move("N")

            if prev_closest_enemy == closest_enemy and prev_closest_enemy is not None:
                new_dist_x = abs(player_ship.x - closest_enemy.x)
                if new_dist_x < prev_dist_x:
                    genome.fitness += 1
                else:
                    genome.fitness -= 1.5
                prev_dist_x = new_dist_x
            else:
                prev_closest_enemy = closest_enemy

            if decision[3] > 0.5 and projectile_tick >= PROJECTILE_TICK:
                create_mail(mail_list, player_ship.x)
                projectile_tick = 0
            else:
                projectile_tick += 1

            projectile_to_remove = list()
            enemy_to_remove = list()
            for mail_projectile in mail_list:
                mail_projectile.move()
                for enemy_ship in enemy_ships:
                    if mail_projectile.collide(enemy_ship):
                        score += 1
                        genome.fitness += 5
                        projectile_to_remove.append(mail_projectile)
                        enemy_to_remove.append(enemy_ship)
                        if score % 10 == 0:
                            MAX_ENEMY_TICK -= 25

            for enemy_ship in enemy_ships:
                if enemy_ship.collide(player_ship):
                    score += 1
                    genome.fitness += 5
                    enemy_to_remove.append(enemy_ship)

                    if score % 10 == 0:
                        MAX_ENEMY_TICK -= 25
                else:
                    enemy_ship.move()

            for enemy_ship in enemy_to_remove:
                enemy_ship.move(reverse=True)
                rand = random.randint(0, 3)
                apology = Apology(
                    APOLOGY_OPTIONS[rand], enemy_ship.x, enemy_ship.y)
                apologies.append(apology)

            for mail_projectile in projectile_to_remove:
                mail_list.remove(mail_projectile)

            result = eval_edge_enemies(genome, enemy_ships, star_set)
            if not result:
                isRunning = False
                break

            eval_edge_projectiles(mail_list)

            draw(WINDOW, star_set, mail_list, player_ship,
                 enemy_ships, apologies, score, time_elapsed_in_s)


def run(config_path):
    """
    This function runs each generation of NNs using the configuration file
    passed to it.

    Arguments:
        config_path  -- Path to the NNs config file
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_path)

    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))

    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run(eval, 1000)


def main():
    config_path = os.path.join(resource_path, "config-feedforward.txt")
    run(config_path)


main()
