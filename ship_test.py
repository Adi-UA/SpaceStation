import pygame
pygame.init()

window_height = 480
window_width = 640

win = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Test game")

x = 50
y = 410
width = 40
height = 60
vel = 15

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()   

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= vel
        else:
            x = window_width
    if keys[pygame.K_RIGHT]:
        if x < window_width:
            x += vel
        else:
            x = 0

    win.fill((0,0,0))
    pygame.draw.rect(win,  (255,0,255), (x,y, width, height))
    pygame.display.update()
    
pygame.quit()