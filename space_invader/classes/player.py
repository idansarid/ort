from space_invader.classes.GameObject import GameObject


class Player(GameObject):

    def __init__(self, x,y):
        super.__init__(self.__class__,self).__init__(x,y)


    def alignBoundaries(self):
        if self.x <= 0:
            self.x = 0
        elif self.x >= 736:
            self.x = 736