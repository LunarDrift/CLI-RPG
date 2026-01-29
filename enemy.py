from random import randint, choice
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

    # def move(self):
    #     # Pick a random cardinal direction; North/South, East/West
    #     # Need this so enemies can't move diagonally
    #     axis = randint(0, 1)
    #     dx = randint(-1, 1)
    #     dy = randint(-1, 1)
    #     if axis == 0:
    #         # X axis
    #         self.pos[0] += dx
    #     elif axis == 1:
    #         # Y axis
    #         self.pos[1] += dy
