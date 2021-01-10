import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("ufo.svg")
pygame.display.set_icon(icon)
playerImg = pygame.image.load("space-invaders.png")
enemyImg = pygame.image.load("ufo.png")
playerX = 370
playerY = 480

enemyX = 370
enemyY = 50


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


running = True
playerX_change = 0
playerY_change = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
            if event.key == pygame.K_UP:
                playerY_change = -0.1
            if event.key == pygame.K_DOWN:
                playerY_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                playerY_change = 0

    screen.fill((0, 0, 0))
    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()