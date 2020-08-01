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

WIN_WIDTH = 1280
WIN_HEIGHT = 720
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
resource_path = os.path.dirname(__file__)
ENEMY_SHIP_IMG_1 = image_reader(resource_path, "alien_1.png")
ENEMY_SHIP_IMG_2 = image_reader(resource_path, "alien_2.png")
ENEMY_SHIP_IMG_3 = image_reader(resource_path, "alien_3.png")
PLAYER_SHIP_IMG = image_reader(resource_path, "player_ship.png")
MAIL_PROJECTILE_IMG = image_reader(resource_path, "mail_projectile.png")
NORMAL_STAR_IMG = pygame.Surface((5, 5))
NORMAL_STAR_IMG.fill((255,255,255))
MAX_ENEMY_TICK = 200
PROJECTILE_TICK = 50
