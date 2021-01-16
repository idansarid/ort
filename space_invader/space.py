import pygame
import random
import math

pygame.init()
WIDTH=800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invader")
background = pygame.image.load("outer_space.jpg")
bullet = pygame.image.load("bullet.png")
icon = pygame.image.load("ufo.svg")
pygame.display.set_icon(icon)
#player
playerImg = pygame.image.load("space-invaders.png")
playerX = 370
playerY = 480
enemyImg = pygame.image.load("ufo.png")
#enemy
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 3
#bullet
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.4
bullet_state = "ready"

END_FONT = pygame.font.SysFont('courier', 40)

# colors
RED = (255,   0,   0)
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))


def display_message(content):
    pygame.time.delay(500)
    screen.fill(RED)
    end_text = END_FONT.render(content, 1, BLACK)
    screen.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
    pygame.display.update()
    pygame.time.delay(1000)


def bullet_hits_enemy(x2, x1, y2, y1):
    dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if dis < 27:
        display_message("Enemy is Hit!!!")


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
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                playerY_change = 0


    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    playerX += playerX_change
    playerY += playerY_change
    # boundaries of space ships
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.2
        enemyX += enemyX_change
    elif enemyX >= 736:
        enemyX_change = -0.2
        enemyX += enemyX_change

    # bullet handling
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        bullet_hits_enemy(x2=enemyX, x1=bulletX, y2=enemyY, y1=bulletY)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()