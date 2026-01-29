import random
from map import Map
from player import Player
from enemy import Enemy


class Game:
    def __init__(self, map_width: int, map_height: int):
        self.game_map: Map = Map(map_width, map_height)
        self.player: Player = Player()
        self.enemies: list = []

    def get_random_walkable_position(self, game_map) -> tuple[int, int]:
        while True:
            x = random.randint(1, game_map.width - 3)
            y = random.randint(1, game_map.height - 2)

            if game_map.base_map[y][x].walkable:
                return x, y

    def spawn_enemies(self, game_map: Map, enemies_list: list, amount: int) -> None:
        for _ in range(amount):
            enemy_x, enemy_y = self.get_random_walkable_position(game_map)
            enemy = Enemy(enemy_x, enemy_y)
            enemies_list.append(enemy)

    def can_move_to(self, game_map: Map, x: int, y: int) -> bool:
        # Check boundaries
        if not (0 <= x < game_map.width and 0 <= y < game_map.height):
            return False
        # Check terrain
        if not game_map.base_map[y][x].walkable:
            return False
        return True

    def run(self):
        self.spawn_enemies(self.game_map, self.enemies, 10)

        self.player.pos = list(self.get_random_walkable_position(self.game_map))

        # Perform initial draw so player appears before the first move
        self.game_map.update_map(self.player, self.enemies)

        while True:
            # Clear screen with ANSI code
            print("\033c", end="")

            self.game_map.display_map()

            # Get valid player moves
            valid_moves = self.player.get_valid_moves(self.game_map)

            print(f"W - UP: {'OK' if valid_moves['w'] else 'BLOCKED'}")
            print(f"A - LEFT: {'OK' if valid_moves['a'] else 'BLOCKED'}")
            print(f"S - DOWN: {'OK' if valid_moves['s'] else 'BLOCKED'}")
            print(f"D - RIGHT: {'OK' if valid_moves['d'] else 'BLOCKED'}")

            # DEBUGGING
            print(f"Pos: {self.player.pos}")  # Debugging info

            movement = input(">>> ").lower()

            # Only move if the key exists in our dict AND it is True
            if movement in valid_moves and valid_moves[movement]:
                match movement:
                    case "w":
                        self.player.move(0, -1)
                    case "a":
                        self.player.move(-1, 0)
                    case "s":
                        self.player.move(0, 1)
                    case "d":
                        self.player.move(1, 0)

            else:
                print("You can't go that way!")
                import time

                time.sleep(0.5)

            # Enemy movement
            for enemy in self.enemies:
                direction = enemy.choose_direction()
                if self.can_move_to(
                    self.game_map,
                    enemy.pos[0] + direction[0],
                    enemy.pos[1] + direction[1],
                ):
                    new_x = enemy.pos[0] + direction[0]
                    new_y = enemy.pos[1] + direction[1]
                    # return new_x, new_y
                    enemy.pos = [new_x, new_y]

            # for enemy in enemies:
            #     enemy.move()

            # Update visuals
            self.game_map.update_map(self.player, self.enemies)
