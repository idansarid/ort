import math
from infra.PygameObject import PygameObject


class Player(PygameObject):

    def __init__(self, x=370, y=480, name="aa"):
        self.x = x
        self.y = y
        self.name = name
        self.playerX_change = 0
        self.playerY_change = 0

    def move(self):
        """

        :return:
        """
        self.x += self.playerX_change
        self.y += self.playerY_change

    def boundary_check(self):
        """

        :return:
        """
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
