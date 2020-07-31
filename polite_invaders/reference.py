import pygame
import os


def image_reader(directory, filename):
    """
    This function grabs the images from the specified filepath using pygame's
    image.load functionality and then returns them. It also scales the images to
    2x and uses convert() to boost performance.

    Arguments: directory   -- Path to the directory in which the image is
        located filename  -- The filename for the image.

    Returns: -- The image at the given location
    """
    return pygame.transform.scale2x(
        pygame.image.load(
            os.path.join(
                directory,
                filename))).convert_alpha()


pygame.init()
game_clock = pygame.time.Clock()

WIN_WIDTH = 600
WIN_HEIGHT = 800
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
resource_path = os.path.dirname(__file__)
ENEMY_SHIP_IMG = image_reader(resource_path, "player_ship.png")
PLAYER_SHIP_IMG = image_reader(resource_path, "player_ship.png")
