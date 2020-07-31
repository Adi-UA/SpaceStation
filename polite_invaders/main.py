import pygame
import os


pygame.init()
game_clock = pygame.time.Clock()

WIN_WIDTH = 1280
WIN_HEIGHT = 720
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
resource_path = os.path.dirname(__file__)


class enemyShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.y_velocity = 5
        self.img = image_reader(resource_path, "player_ship.png")

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.y_velocity


class playerShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_velocity = 5
        self.MOVE_TICK = 0
        self.img = image_reader(resource_path, "player_ship.png")

    def move(self, direction):
        if direction == "L":
            new_x = self.x - (self.x_velocity + self.MOVE_TICK)
        elif direction == "R":
            new_x = self.x + (self.x_velocity + self.MOVE_TICK)
        else:
            self.MOVE_TICK = 0
            return

        if new_x > 10 and new_x < 1220:
            self.x = new_x

        if self.MOVE_TICK < 4:
            self.MOVE_TICK += 1

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
    player_ship = playerShip(600, 650)
    enemy_ship = enemyShip(600, 10)

    while isRunning:
        game_clock.tick(60)

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
                pygame.quit()
                exit(0)

        if keys[pygame.K_LEFT]:
            player_ship.move("L")
        elif keys[pygame.K_RIGHT]:
            player_ship.move("R")
        else:
            player_ship.move("N")

        enemy_ship.move()
        draw(WINDOW, player_ship, enemy_ship)


main()
