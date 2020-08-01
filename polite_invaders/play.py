import pygame
import os
import random
from reference import *
from enemy_ship import EnemyShip, EnemyShipCreeper, EnemyShipDeathStar, EnemyShipCookie
from player_ship import PlayerShip
from star import Star
from projectile import Projectile, MailProjectile
from apology import Apology
import eel

"""Music: www.bensound.com" or "Royalty Free Music from Bensound"""


def create_mail(mail_list, x):
    """
    Creates mail projectiles and adds them to the list of projectiles

    Args:
        mail_list (list): The current list of mail projectiles
        x (int): The position to spawn the projectile at
    """

    y = WIN_HEIGHT - 80
    mail_projectile = MailProjectile(x, y)
    mail_list.append(mail_projectile)


def create_stars():
    """
    Create and return the set of stars used in the background

    Returns:
        set: The set of Star objects
    """

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
    """
    Adds a random enemy to the list of enemies

    Args:
        enemy_ships (list): The list of enemy ships

    Returns:
        list: The updated list of enemy ships
    """

    x = random.randrange(10, WIN_WIDTH - 80)
    y = 10
    n = random.randint(1, 3)

    if n == 1:
        enemy_ships.append(EnemyShipCreeper(x, y))
    elif n == 2:
        enemy_ships.append(EnemyShipDeathStar(x, y))
    elif n == 3:
        enemy_ships.append(EnemyShipCookie(x, y))
    return enemy_ships


def eval_edge_projectiles(mail_list):
    """
    Removes projectiles if they've reache the top edge

    Args:
        mail_list (list): The list of mail projectiles
    """

    to_remove = list()
    for mail_projectile in mail_list:
        if mail_projectile.y > WIN_HEIGHT - 50:
            to_remove.append(mail_projectile)

    for mail_projectile in to_remove:
        mail_list.remove(mail_projectile)


def eval_edge_enemies(enemy_ships, star_set):
    """
    Evaluates enemies at the top and bottom edge and takes actions appropriately

    Args:
        enemy_ships (list): The enemy ships
        star_set (set): The set of stars

    Returns:
        boolean: True if all checks pass and False if an enemy reached the bottom edge
    """

    to_remove = list()
    for enemy_ship in enemy_ships:
        if enemy_ship.y > WIN_HEIGHT - 50:
            lose_screen(WINDOW, star_set)
        elif enemy_ship.y < 10:
            to_remove.append(enemy_ship)

    for ship in to_remove:
        enemy_ships.remove(ship)


def start_screen(window, star_set):
    """
    Display the start screen

    Args:
        window : Root pygame window
        star_set (set): Set of stars
    """
    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    font = pygame.font.Font(resource_path + "/comicsans.ttf", 80)
    text = font.render("POLITE INVADERS :)", True, (255, 255, 255))
    window.blit(text, (260, WIN_HEIGHT // 2 - 30))

    pygame.display.update()
    pygame.time.wait(3000)


def win_screen(window, star_set, win_type):
    """
    Display the win screen

    Args:
        window : Root pygame window
        star_set (set): Set of stars
        win_type (str): "l" or "w" for a legal or normal win
    """

    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    font = pygame.font.Font(resource_path + "/comicsans.ttf", 60)
    win_text = font.render("YOU WIN!",
                           True, (255, 255, 255))
    window.blit(win_text, (WIN_WIDTH // 2 - 170, WIN_HEIGHT // 2 - 80))
    if win_type == "l":
        text = font.render("THEY LEGALLY HAD TO LEAVE...",
                           True, (255, 255, 255))
        window.blit(text, (160, WIN_HEIGHT // 2))
    else:
        text = font.render("YOU'RE TOO POLITE TO INVADE...",
                           True, (255, 255, 255))
        window.blit(text, (150, WIN_HEIGHT // 2))

    pygame.display.update()
    pygame.time.wait(5000)


def lose_screen(window, star_set):
    """
    Display the loss screen

    Args:
        window : Root pygame window
        star_set (set): Set of stars
    """

    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    font = pygame.font.Font(resource_path + "/comicsans.ttf", 60)
    text = font.render("SORRY...YOU WEREN'T POLITE ENOUGH...",
                       True, (255, 255, 255))
    window.blit(text, (30, WIN_HEIGHT // 2 - 30))

    pygame.display.update()
    pygame.time.wait(5000)
    pygame.quit()
    exit(0)


def draw(
        window,
        star_set,
        mail_list,
        player_ship,
        enemy_ships,
        apologies,
        score,
        time_in_s):
    """
    Draws the pygame window at each frame

    Args:
        window (Pygame surface): The window to draw on
        star_set (list): The list of stars to draw
        mail_list (list): The list of mail projectiles to draw
        player_ship (PlayerShip): The player ship
        enemy_ships (list): The enemy ships
        apologies (list): The apology objects to draw
        score (int): The current score
        time_in_s (int): The time in seconds rounded to the closest integer
    """

    window.fill((18, 9, 10))

    for star in star_set:
        star.draw(window)

    for mail_projectile in mail_list:
        mail_projectile.draw(window)

    for enemy_ship in enemy_ships:
        enemy_ship.draw(window)

    for apology in apologies:
        apology.draw(window)

    font = pygame.font.Font(resource_path + "/comicsans.ttf", 30)
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(text, (10, 5))

    text = font.render("Time: " + str(time_in_s), True, (255, 255, 255))
    window.blit(text, (WIN_WIDTH - 120, 5))

    player_ship.draw(window)

    pygame.display.update()

def play():
    """
    Run the game
    """

    MAX_ENEMY_TICK = 150
    isRunning = True
    score = 0
    star_set = create_stars()
    mail_list = list()
    player_ship = PlayerShip(WIN_WIDTH // 2, WIN_HEIGHT - 70)
    enemy_ships = add_enemy(list())
    apologies = list()
    enemy_tick = MAX_ENEMY_TICK
    projectile_tick = PROJECTILE_TICK
    clear_text_tick = CLEAR_TEXT_TICK

    start_screen(WINDOW, star_set)
    start_time = pygame.time.get_ticks()
    print('hi')

    while isRunning:
        game_clock.tick(60)  # 60 fps

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit(0)

        if score >= 42:
            # win with a score of 42
            win_screen(WINDOW, star_set, "w")
            isRunning = False
            pygame.quit()
            exit(0)

        time_elapsed_in_s = round(
            (pygame.time.get_ticks() - start_time) / 1000)

        if time_elapsed_in_s >= 99:
            # Survive for 99 seconds
            win_screen(WINDOW, star_set, "l")
            isRunning = False
            pygame.quit()
            exit(0)

        # Clear apologies and add enemies periodically
        if clear_text_tick < 1:
            if len(apologies) > 0:
                apologies.pop(0)
            clear_text_tick = CLEAR_TEXT_TICK

        if enemy_tick < 1:
            enemy_tick = MAX_ENEMY_TICK
            enemy_ships = add_enemy(enemy_ships)

        # Read and use input
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_ship.move("L")
        elif keys[pygame.K_RIGHT]:
            player_ship.move("R")
        else:
            player_ship.move("N")

        if keys[pygame.K_SPACE] and projectile_tick >= PROJECTILE_TICK:
            create_mail(mail_list, player_ship.x)
            projectile_tick = 0

        # remove projectiles and enemies that have collided
        projectile_to_remove = list()
        enemy_to_remove = list()
        for mail_projectile in mail_list:
            mail_projectile.move()
            for enemy_ship in enemy_ships:
                if mail_projectile.collide(enemy_ship):
                    score += 1
                    projectile_to_remove.append(mail_projectile)
                    enemy_to_remove.append(enemy_ship)
                    if score % 5 == 0:
                        MAX_ENEMY_TICK -= 10

        # Remove enemies that bump into a player
        for enemy_ship in enemy_ships:
            if enemy_ship.collide(player_ship):
                score += 1
                enemy_to_remove.append(enemy_ship)

                if score % 5 == 0:
                    MAX_ENEMY_TICK -= 10
            else:
                enemy_ship.move()

        # Removed enemies go in reverse while removed projectiles are not drawn
        # anymore
        for enemy_ship in enemy_to_remove:
            enemy_ship.move(reverse=True)
            rand = random.randint(0, 3)
            apology = Apology(
                APOLOGY_OPTIONS[rand], enemy_ship.x, enemy_ship.y)
            apologies.append(apology)

        for mail_projectile in projectile_to_remove:
            mail_list.remove(mail_projectile)

        # Check if projectiles or enemies reach the edge
        # If an enemy is at the bottom edge, you lose
        eval_edge_enemies(enemy_ships, star_set)
        eval_edge_projectiles(mail_list)

        # Draw the frame
        draw(WINDOW, star_set, mail_list, player_ship,
             enemy_ships, apologies, score, time_elapsed_in_s)

        clear_text_tick -= 1
        enemy_tick -= 1
        projectile_tick += 1


if __name__ == "__main__":
    play()
