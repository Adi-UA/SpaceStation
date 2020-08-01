import pygame
import os
import random

resource_path = os.path.dirname(__file__)
songs = ["/ImperialMarch.ogg", "/rick_and_morty.ogg", "/StarTrek.ogg", "/Starwars.ogg"]

def random_music():
    i = random.randint(0,len(songs)-1)
    return songs[i]


pygame.init()
game_clock = pygame.time.Clock()

WIN_WIDTH = 800
WIN_HEIGHT = 450
pygame.display.set_caption('Space Rave with Rick and Morty')
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
bg = pygame.image.load(resource_path+'/RandM.jpg')
win.blit(bg, (0,0))
font = pygame.font.Font(resource_path + "/comicsans.ttf", 34)
text = font.render(" PRESS THE SPACE BAR TO CHANGE THE SONG 0",
                    True, (255, 255, 255), (0,0,0))
win.blit(text, (0, 405 ))
pygame.display.update()


isRunning = True
isFirst = True

while isRunning:
    if isFirst:
        pygame.mixer.music.load(resource_path + random_music())
        pygame.mixer.music.play(1)
        isFirst = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()
            exit(0)

        keys = pygame.key.get_pressed()   

        if keys[pygame.K_SPACE]:
            pygame.mixer.music.load(resource_path + random_music())
            pygame.mixer.music.play(1)


