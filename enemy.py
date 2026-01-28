from tile import enemy


class Enemy:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.symbol = enemy

    def position(self):
        return self.x, self.y
