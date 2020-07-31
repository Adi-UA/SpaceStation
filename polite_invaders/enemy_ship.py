import pygame
from reference import *


class enemyShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_collided = False
        self.y_velocity = 0.27/100*WIN_HEIGHT
        self.img = ENEMY_SHIP_IMG_1

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def collide(self, player_ship):
        if not self.has_collided:
            player_ship_mask = player_ship.get_mask()
            self_mask = pygame.mask.from_surface(self.img)

            offset = (round(self.x - player_ship.x), round(self.y - player_ship.y))

            overlaps = player_ship_mask.overlap(self_mask, offset)

            if overlaps:
                return True
                self.has_collided = True
            else:
                return False
        else:
            return False

    def move(self, reverse=False):
        if reverse:
            self.y = self.y - 32
            self.y_velocity = -self.y_velocity*2

        self.y += self.y_velocity


class enemyShipCreeper(enemyShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = ENEMY_SHIP_IMG_1


class enemyShipDeathStar(enemyShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = ENEMY_SHIP_IMG_2
