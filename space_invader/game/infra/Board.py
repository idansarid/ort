from space_invader.game.infra.Player import Player
from space_invader.game.infra.Bullet import Bullet
from space_invader.game.infra.Enemy import Enemy
import pygame
import random
import math

pygame.init()
pygame.display.set_caption("Space Invader")
background = pygame.image.load("outer_space.jpg")
bullet_image = pygame.image.load("bullet.png")
icon = pygame.image.load("ufo.svg")
pygame.display.set_icon(icon)
#player
playerImg = pygame.image.load("space-invaders.png")
enemyImg = pygame.image.load("ufo.png")
bulletImage = pygame.image.load("bullet.png")
END_FONT = pygame.font.SysFont('courier', 40)
WIDTH = 800
HEIGHT = 600
RED = (255,   0,   0)
GREY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Board(object):

    def __init__(self):
        self.player = Player()
        self.enemy = Enemy()
        self.bullet = Bullet()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.score = 0
        self.background = pygame.image.load("outer_space.jpg")

    def player_blit(self, x, y):
        self.screen.blit(playerImg, (x, y))

    def enemy_blit(self, x, y):
        self.screen.blit(enemyImg, (x, y))

    def fire_bullet(self, x, y):
        self.bullet.bullet_state = "fire"
        self.screen.blit(bullet_image, (x + 16, y + 10))

    def display_message(self, content):
        pygame.time.delay(500)
        self.screen.fill(RED)
        end_text = END_FONT.render(content, 1, BLACK)
        self.screen.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.delay(1000)

    def bullet_hits_enemy(self, x2, x1, y2, y1):
        if self.is_collision(x2=x2,x1=x1,y2=y2,y1=y1):
            print(self.score)
            # self.display_message("Enemy is Hit!!!")

    def is_collision(self,x1,y1,x2,y2):
        dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        if dis < 27:
            return True
        else:
            return False
