from copy import deepcopy
from random import randint
from tile import Tile, plains, forest, pines, mountain, water
from colors import RED, GREEN, BLUE, ANSI_RESET, BOLD


class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        # Holds the rendered frame (terrain + player)
        self.map_data: list[list[Tile]] = []

        # This will hold ONLY terrain (forests, water, etc)
        # Use this to reset the map every frame before drawing player
        self.base_map: list[list[Tile]] = []

        self.generate_map()

        # Generate terrain features
        self.generate_patch(forest, 5, 8, 8)
        self.generate_patch(pines, 4, 4, 6)
        self.generate_patch(mountain, 3, 7, 9)
        self.generate_patch(water, 2, 10, 12)

        # Save the terrain now that patches have been generated
        self.base_map = deepcopy(self.map_data)

    def generate_map(self) -> None:
        self.init_map_data: list[list[Tile]] = [
            [plains for _ in range(self.width)] for _ in range(self.height)
        ]
        self.map_data = deepcopy(self.init_map_data)

    def generate_patch(
        self,
        tile: Tile,
        num_patches: int,
        min_size: int,
        max_size: int,
        irregular: bool = True,  # randomize each row start/end position
    ) -> None:
        for _ in range(num_patches):
            width = randint(min_size, max_size)
            height = randint(min_size, max_size)
            start_x = randint(1, self.width - width - 1)
            start_y = randint(1, self.height - height - 1)

            if irregular:
                init_start_x = randint(3, self.width - max_size)

            for i in range(height):
                if irregular:
                    width = randint(int(0.7 * max_size), max_size)
                    start_x = init_start_x - randint(1, 2)
                for j in range(width):
                    # Boundary check to prevent crashes if patch goes off-screen
                    if 0 <= start_y + i < self.height and 0 <= start_x + j < self.width:
                        self.map_data[start_y + i][start_x + j] = tile

    def display_map(self) -> None:
        frame = "x" + self.width * "=" + "x"
        print(frame)
        for row in self.map_data:
            # Use tile.symbol to get the colored string
            row_tiles = [tile.symbol for tile in row]
            print("|" + "".join(row_tiles) + "|")
        print(frame)
        print()
        self.display_map_legend()

    def display_map_legend(self):
        print(f"{BOLD}--------- Map Atlas ----------{ANSI_RESET}")
        print(f" @ - Player  |  {RED}E - Enemy{ANSI_RESET}")
        print(f" {BLUE}~ - Water{ANSI_RESET}  |  A - Mountain")
        print(f" {GREEN}8 - Forest{ANSI_RESET}  | {GREEN}Y - Pine Forest{ANSI_RESET}")
        print(f"{BOLD}------------------------------{ANSI_RESET}\n")

    def update_map(self, player, enemies) -> None:
        # Reset to terrain
        self.map_data = deepcopy(self.base_map)

        # Draw enemies first
        for enemy in enemies:
            ex, ey = enemy.pos
            if 0 <= ey < self.height and 0 <= ex < self.width:
                self.map_data[ey][ex] = enemy.symbol

        # Draw player last so appears on top
        px, py = player.pos
        if 0 <= py < self.height and 0 <= px < self.width:
            self.map_data[py][px] = player.symbol
