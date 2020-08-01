import pygame
import random
from reference import *


class Apology:

    def __init__(self, text, x, y):
        self.text = text
        self.x = x
        self.y = y

    def draw(self, window):
        font = pygame.font.Font(resource_path + "/comicsans.ttf", 30)
        apology = font.render(self.text, True, (255, 255, 255))
        window.blit(apology, (self.x, self.y))
