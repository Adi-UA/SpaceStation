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

    def move(self):
        self.y += self.y_velocity