import pygame
import os
from reference import *
from enemy_ship import enemyShip
from player_ship import playerShip

def enemy_at_edge(enemy_ships):
    for enemy_ship in enemy_ships:
        if enemy_ship.y > WIN_HEIGHT-70:
            return True
    return False

def draw(window, player_ship, enemy_ship):
    window.fill((0, 0, 51))
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

        if enemy_at_edge(enemy_ships):
            isRunning = False
            pygame.quit()
            exit(0)

        for enemy_ship in enemy_ships:
            enemy_ship.move()
        draw(WINDOW, player_ship, enemy_ship)


main()
