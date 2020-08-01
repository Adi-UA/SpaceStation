import pygame
import os
import random
from reference import *
from enemy_ship import enemyShip, enemyShipCreeper, enemyShipDeathStar, enemyShipCookie
from player_ship import playerShip
from star import Star
from projectile import Projectile, MailProjectile


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


def eval_edge_enemies(enemy_ships, star_set):
    to_remove = list()
    for enemy_ship in enemy_ships:
        if enemy_ship.y > WIN_HEIGHT-50:
            lose_screen(WINDOW, star_set)
        elif enemy_ship.y < 10:
            to_remove.append(enemy_ship)

    for ship in to_remove:
        enemy_ships.remove(ship)


def start_screen(window, star_set):
    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    font = pygame.font.Font(resource_path+"/comicsans.ttf", 80)
    text = font.render("POLITE INVADERS :)", True, (255, 255, 255))
    window.blit(text, (260, WIN_HEIGHT//2 - 30))

    pygame.display.update()
    pygame.time.wait(3000)


def win_screen(window, star_set, win_type):
    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    font = pygame.font.Font(resource_path+"/comicsans.ttf", 60)
    win_text = font.render("YOU WIN!",
                           True, (255, 255, 255))
    window.blit(win_text, (WIN_WIDTH//2-170, WIN_HEIGHT//2 - 80))
    if win_type == "l":
        text = font.render("THEY LEGALLY HAD TO LEAVE...",
                           True, (255, 255, 255))
        window.blit(text, (160, WIN_HEIGHT//2))
    else:
        text = font.render("YOU'RE TOO POLITE TO INVADE...",
                           True, (255, 255, 255))
        window.blit(text, (150, WIN_HEIGHT//2))

    pygame.display.update()
    pygame.time.wait(5000)


def lose_screen(window, star_set):
    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    font = pygame.font.Font(resource_path+"/comicsans.ttf", 60)
    text = font.render("SORRY...YOU WEREN'T POLITE ENOUGH...",
                       True, (255, 255, 255))
    window.blit(text, (30, WIN_HEIGHT//2 - 30))

    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()
    exit(0)


def draw(window, star_set, mail_list, player_ship, enemy_ships, score, time_in_s):
    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    for mail_projectile in mail_list:
        mail_projectile.draw(window)

    for enemy_ship in enemy_ships:
        enemy_ship.draw(window)

    font = pygame.font.Font(resource_path+"/comicsans.ttf", 30)
    text = font.render("Score: "+str(score), True, (255, 255, 255))
    window.blit(text, (10, 5))

    text = font.render("Time: "+str(round(time_in_s)), True, (255, 255, 255))
    window.blit(text, (WIN_WIDTH - 120, 5))

    player_ship.draw(window)

    pygame.display.update()


def main():
    global MAX_ENEMY_TICK

    isRunning = True
    score = 0
    star_set = create_stars()
    mail_list = list()
    player_ship = playerShip(WIN_WIDTH//2, WIN_HEIGHT-70)
    enemy_ships = add_enemy(list())
    enemy_tick = MAX_ENEMY_TICK
    projectile_tick = PROJECTILE_TICK

    start_screen(WINDOW, star_set)
    start_time = pygame.time.get_ticks()

    while isRunning:
        game_clock.tick(60)

        if score >= 42:
            win_screen(WINDOW, star_set, "l")
            isRunning = False
            pygame.quit()
            exit(0)

        time_elapsed_in_s = (pygame.time.get_ticks() - start_time)/1000
        if time_elapsed_in_s >= 900:
            win_screen(WINDOW, star_set, "l")
            isRunning = False
            pygame.quit()
            exit(0)

        if enemy_tick < 1:
            enemy_tick = MAX_ENEMY_TICK
            enemy_ships = add_enemy(enemy_ships)
        enemy_tick -= 1

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit(0)

        if keys[pygame.K_LEFT]:
            player_ship.move("L")
        elif keys[pygame.K_RIGHT]:
            player_ship.move("R")
        else:
            player_ship.move("N")

        if keys[pygame.K_SPACE] and projectile_tick >= PROJECTILE_TICK:
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
                    projectile_to_remove.append(mail_projectile)
                    enemy_to_remove.append(enemy_ship)
                    if score % 10 == 0:
                        MAX_ENEMY_TICK -= 25

        for enemy_ship in enemy_ships:
            if enemy_ship.collide(player_ship):
                score += 1
                enemy_to_remove.append(enemy_ship)

                if score % 10 == 0:
                    MAX_ENEMY_TICK -= 25
            else:
                enemy_ship.move()

        for enemy_ship in enemy_to_remove:
            enemy_ship.move(reverse=True)

        for mail_projectile in projectile_to_remove:
            mail_list.remove(mail_projectile)

        eval_edge_enemies(enemy_ships, star_set)
        eval_edge_projectiles(mail_list)

        draw(WINDOW, star_set, mail_list, player_ship,
             enemy_ships, score, time_elapsed_in_s)


main()
