from tile import player, mountain, water


class Player:
    def __init__(self):
        self.pos = [0, 0]
        self.symbol = player

    def move(self, x: int, y: int) -> None:
        self.pos[0] += x
        self.pos[1] += y

    def get_valid_moves(self, game_map: list[list]) -> dict[str, bool]:
        x, y = self.pos

        def is_walkable(nx, ny):
            # Check map boundaries
            if not (0 <= nx < game_map.width and 0 <= ny < game_map.height):
                return False
            # Check if the tile at that coordinate is impassable
            target_tile = game_map.base_map[ny][nx]
            if not target_tile.walkable:
                return False
            return True

        return {
            "w": is_walkable(x, y - 1),
            "s": is_walkable(x, y + 1),
            "a": is_walkable(x - 1, y),
            "d": is_walkable(x + 1, y),
        }
