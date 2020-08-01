import pygame
import random
from reference import *


class Star:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.twinkle_tick = 0
        self.img = NORMAL_STAR_IMG

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Star):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        return 2*self.x + self.y
