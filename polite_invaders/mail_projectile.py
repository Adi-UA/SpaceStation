import pygame
import random
from reference import *


class MailProjectile:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.has_collided = False
        self.y_velocity = -0.6/100*WIN_HEIGHT
        self.img = MAIL_PROJECTILE_IMG

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.y_velocity

    def collide(self, enemy_ship):
        if not self.has_collided:
            enemy_ship_mask = enemy_ship.get_mask()
            self_mask = pygame.mask.from_surface(self.img)

            offset = (round(self.x - enemy_ship.x),
                      round(self.y - enemy_ship.y))

            overlaps = enemy_ship_mask.overlap(self_mask, offset)

            if overlaps:
                self.has_collided = True
                return True
            else:
                return False
        else:
            return False

