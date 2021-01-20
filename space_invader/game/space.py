import pygame
import random
import math
from infra.Player import Player
from infra.Enemy import Enemy
from infra.Bullet import Bullet
from infra.Board import Board


# pygame.init()
# WIDTH = 800
# HEIGHT = 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
#
# pygame.display.set_caption("Space Invader")
# background = pygame.image.load("outer_space.jpg")
# bullet_image = pygame.image.load("bullet.png")
# icon = pygame.image.load("ufo.svg")
# pygame.display.set_icon(icon)
# #player
# playerImg = pygame.image.load("space-invaders.png")
# enemyImg = pygame.image.load("ufo.png")
# bulletImage = pygame.image.load("bullet.png")
# END_FONT = pygame.font.SysFont('courier', 40)
# player = Player()
# enemy = Enemy()
# bullet = Bullet()
#
# # colors
# RED = (255,   0,   0)
# GREY = (200, 200, 200)
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)


if __name__ == '__main__':
    board = Board()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.player.playerX_change = -0.1
                if event.key == pygame.K_RIGHT:
                    board.player.playerX_change = 0.1
                if event.key == pygame.K_UP:
                    board.player.playerY_change = -0.1
                if event.key == pygame.K_DOWN:
                    board.player.playerY_change = 0.1
                if event.key == pygame.K_SPACE:
                    if board.bullet.bullet_state == "ready":
                        board.bullet.x = board.player.x
                        board.fire_bullet(board.bullet.x, board.bullet.y)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    board.player.playerX_change = 0
                    board.player.playerY_change = 0

        board.screen.fill((0, 0, 0))
        board.screen.blit(board.background, (0, 0))
        board.player.x += board.player.playerX_change
        board.player.y += board.player.playerY_change
        # boundaries of space ships
        board.player.move()
        board.enemy.move()

        # bullet handling
        if board.bullet.y <= 0:
            board.bullet.y = 480
            board.bullet.bullet_state = "ready"
        elif board.bullet.bullet_state == "fire":
            board.fire_bullet(board.bullet.x, board.bullet.y)
            board.bullet.y -= board.bullet.bulletY_change
            board.bullet_hits_enemy(x2=board.enemy.x, x1=board.bullet.x, y2=board.enemy.y, y1=board.bullet.y)

        board.player_blit(board.player.x, board.player.y)
        board.enemy_blit(board.enemy.x, board.enemy.y)
        pygame.display.update()