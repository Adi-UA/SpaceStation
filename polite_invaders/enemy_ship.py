import pygame
from reference import *


class EnemyShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_collided = False
        self.y_velocity = 0.3 / 100 * WIN_HEIGHT

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def collide(self, player_ship):
        if not self.has_collided:
            player_ship_mask = player_ship.get_mask()
            self_mask = pygame.mask.from_surface(self.img)

            offset = (round(self.x - player_ship.x),
                      round(self.y - player_ship.y))

            overlaps = player_ship_mask.overlap(self_mask, offset)

            if overlaps:
                self.has_collided = True
                return True
            else:
                return False
        else:
            return False

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def move(self, reverse=False):
        if reverse:
            self.y_velocity = -self.y_velocity * 1.5

        self.y += self.y_velocity

    def __eq__(self, other):
        if other is not None and (
            isinstance(
                other,
                EnemyShip) or issubclass(
                other,
                EnemyShip)):
            return self.x == other.x and self.y == other.y
        else:
            return False


class EnemyShipCreeper(EnemyShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = ENEMY_SHIP_IMG_1
        self.y_velocity = self.y_velocity * 2


class EnemyShipDeathStar(EnemyShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = ENEMY_SHIP_IMG_2


class EnemyShipCookie(EnemyShip):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.img = ENEMY_SHIP_IMG_3
        self.y_velocity = self.y_velocity * 1.5
