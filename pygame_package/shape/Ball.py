import pygame

PINK = (255, 0, 0)


class Ball(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(self.__class__, self).__init__()
        self.image = pygame.image.load('base.jpg')
        self.image.convert()
        self.image.set_colorkey(PINK)
        self.image_size = self.image.get_size()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.__vx = 3
        self.__vy = 5

    def update_v(self, vx, vy):
        self.__vx = vx
        self.__vy = vy

    def update_loc(self):
        self.rect.x += self.__vx
        self.rect.y += self.__vy

    def get_pos(self):
        return self.rect.x, self.rect.y

    def get_v(self):
        return self.__vx, self.__vy
