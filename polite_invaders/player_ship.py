import pygame
from reference import *


class PlayerShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = 0.6/100*WIN_WIDTH
        self.MOVE_TICK = 0
        self.img = PLAYER_SHIP_IMG

    def move(self, direction):
        if direction == "L":
            new_x = self.x - (self.x_velocity + self.MOVE_TICK)
        elif direction == "R":
            new_x = self.x + (self.x_velocity + self.MOVE_TICK)
        else:
            self.MOVE_TICK = 0
            return

        if new_x > 10 and new_x < WIN_WIDTH - 62:
            self.x = new_x

        if self.MOVE_TICK < 4:
            self.MOVE_TICK += 1

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
