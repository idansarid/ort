import math
from game.infra.PygameObject import PygameObject
import random


class Enemy(PygameObject):

    def __init__(self, x=None, y=None):
        self.x = random.randint(0, 735)
        self.y = random.randint(50, 150)
        self.enemyX_change = 0.2
        self.enemyY_change = 3
        self.hit_count = 0

    def move(self):
        """
        :return:
        """
        self.x += self.enemyX_change
        if self.x <= 0:
            self.enemyX_change = 0.2
            self.x += self.enemyX_change
        elif self.x >= 736:
            self.enemyX_change = -0.2
            self.x += self.enemyX_change