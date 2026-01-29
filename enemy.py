from random import choice
from tile import enemy


class Enemy:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.symbol = enemy

    def position(self):
        return self.x, self.y

    def choose_direction(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = choice(directions)
        return dx, dy
