import math
from abc import ABC, abstractmethod


class PygameObject(ABC):

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    @abstractmethod
    def move(self):
        pass