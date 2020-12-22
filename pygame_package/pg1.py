import pygame, sys

IMAGE = 'nature.jpg'
RED = (255, 0, 0)
BLACK = (0, 0, 0)
img = pygame.image.load(IMAGE)
clock = pygame.time.Clock()

pygame.init()

windowSize = (800, 600)
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(windowSize)
screen.fill(BLACK)

myriadProFont = pygame.font.SysFont("Myriad Pro", 48)

helloWorld = myriadProFont.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(helloWorld, (0, 0))
    # screen.blit(img, [220, 300])
    pygame.display.flip()
    clock.tick(1)
    #
    # pygame.display.update()