from random import randint
from tile import enemy


class Enemy:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.symbol = enemy

    def position(self):
        return self.x, self.y

    def move(self):
        axis = randint(0, 1)
        dx = randint(-1, 1)
        dy = randint(-1, 1)
        if axis == 0:
            # X axis
            self.pos[0] += dx
        elif axis == 1:
            # Y axis
            self.pos[1] += dy
