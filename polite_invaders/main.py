import pygame
import os
import random
from reference import *
from enemy_ship import enemyShip, enemyShipCreeper, enemyShipDeathStar, enemyShipCookie
from player_ship import playerShip


def add_enemy(enemy_ships):
    x = random.randrange(10, WIN_WIDTH - 80)
    y = 10
    n = random.randint(1, 3)
    print(n)
    if n == 1:
        enemy_ships.append(enemyShipCreeper(x, y))
    elif n == 2:
        enemy_ships.append(enemyShipDeathStar(x, y))
    elif n == 3:
        enemy_ships.append(enemyShipCookie(x, y))
    return enemy_ships


def eval_edge_enemies(enemy_ships):
    to_remove = list()
    for enemy_ship in enemy_ships:
        if enemy_ship.y > WIN_HEIGHT-50:
            print("The enemy got through")
            pygame.quit()
            exit(0)
        elif enemy_ship.y < 10:
            to_remove.append(enemy_ship)

    for ship in to_remove:
        enemy_ships.remove(ship)


def draw(window, player_ship, enemy_ships, score):
    window.fill((0, 0, 51))

    for enemy_ship in enemy_ships:
        enemy_ship.draw(window)

    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, (255, 255, 255))
    window.blit(text, (640, 0))
    player_ship.draw(window)
    pygame.display.update()


def main():
    global MAX_ENEMY_TICK
    isRunning = True
    score = 0
    player_ship = playerShip(WIN_WIDTH//2, WIN_HEIGHT-70)
    enemy_ships = add_enemy(list())
    enemy_tick = MAX_ENEMY_TICK

    while isRunning:
        game_clock.tick(60)

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

        eval_edge_enemies(enemy_ships)

        for enemy_ship in enemy_ships:
            if enemy_ship.collide(player_ship):
                score += 1
                enemy_ship.move(reverse=True)

            else:
                enemy_ship.move()

        draw(WINDOW, player_ship, enemy_ships, score)


main()
