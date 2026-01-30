from colors import ANSI_RESET, YELLOW, GREEN, WHITE, RED, BLUE


class Tile:
    def __init__(
        self,
        symbol: str,
        color: str = ANSI_RESET,
        colored: bool = True,
        walkable: bool = True,
    ):
        self.symbol = f"{color}{symbol}{ANSI_RESET}" if colored else symbol
        self.walkable = walkable


plains = Tile(symbol=".", color=YELLOW)
forest = Tile(symbol="8", color=GREEN)
pines = Tile(symbol="Y", color=GREEN)
mountain = Tile(symbol="A", color=WHITE, walkable=False)
water = Tile(symbol="~", color=BLUE, walkable=False)

player = Tile(symbol="@", color=WHITE, walkable=False)
enemy = Tile(symbol="E", color=RED, walkable=False)
