ANSI_RESET = "\033[0m"
WHITE = "\033[97m"
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"


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
