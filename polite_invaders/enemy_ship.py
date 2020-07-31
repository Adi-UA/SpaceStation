import pygame
from reference import *


class enemyShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_velocity = 0.3/100*WIN_HEIGHT
        self.img = ENEMY_SHIP_IMG

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def collide(self, player_ship):
        player_ship_mask = player_ship.get_mask()
        self_mask = pygame.mask.from_surface(self.img)

        offset = (round(self.x - player_ship.x), round(self.y - player_ship.y))

        overlaps = player_ship_mask.overlap(self_mask, offset)

        if overlaps:
            return True
        else:
            return False

    def move(self, reverse=False):
        if reverse:
            self.y_velocity = -self.y_velocity

        self.y += self.y_velocity
