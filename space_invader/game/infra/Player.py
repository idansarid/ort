import math
from space_invader.game.infra.PygameObject import PygameObject


class Player(PygameObject):

    def __init__(self, x=370, y=480):
        self.x = x
        self.y = y
        self.playerX_change = 0
        self.playerY_change = 0

    def move(self):
        """

        :return:
        """
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736
