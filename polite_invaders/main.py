import pygame
import os
from reference import *
from enemy_ship import enemyShip
from player_ship import playerShip


def eval_edge_enemies(enemy_ships):
    to_remove = list()
    for enemy_ship in enemy_ships:
        if enemy_ship.y > WIN_HEIGHT-70:
            pygame.quit()
            exit(0)
        elif enemy_ship.y < 10:
            to_remove.append(enemy_ship)

    for ship in to_remove:
        enemy_ships.remove(ship)


def draw(window, player_ship, enemy_ships):
    window.fill((0, 0, 51))

    for enemy_ship in enemy_ships:
        enemy_ship.draw(window)

    player_ship.draw(window)
    pygame.display.update()


def main():
    isRunning = True
    player_ship = playerShip(WIN_WIDTH//2, WIN_HEIGHT-70)
    enemy_ships = [enemyShip(WIN_WIDTH//2, 10)]

    while isRunning:
        game_clock.tick(60)

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
                enemy_ship.move(reverse=True)
            else:
                enemy_ship.move()

        draw(WINDOW, player_ship, enemy_ships)


main()
