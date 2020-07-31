import pygame
import os


pygame.init()
game_clock = pygame.time.Clock()

WIN_WIDTH = 1280
WIN_HEIGHT = 720
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
resource_path = os.path.dirname(__file__)


class enemyShip:
    def __init__(self):
        self.x = 600
        self.y = 10
        self.img = image_reader(resource_path, "creeper2.png")

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += 5


class playerShip:
    def __init__(self):
        self.x = 600
        self.y = 650
        self.img = image_reader(resource_path, "creeper.png")



    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


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


def draw(window, player_ship, enemy_ship):
    window.fill((0, 0, 51))
    enemy_ship.draw(window)
    player_ship.draw(window)
    pygame.display.update()


def main():
    isRunning = True
    player_ship = playerShip()
    enemy_ship = enemyShip()

    while isRunning:
        game_clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                
        enemy_ship.move()
        draw(WINDOW, player_ship, enemy_ship)


main()
