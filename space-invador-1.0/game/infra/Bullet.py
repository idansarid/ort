import math
from game.infra.PygameObject import PygameObject


class Bullet(PygameObject):

    def __init__(self, x=0, y=480):
        self.x = x
        self.y = y
        self.bulletX_change = 0
        self.bulletY_change = 0.4
        self.bullet_state = "ready"

    def move(self):
        self.y -= self.bulletY_change