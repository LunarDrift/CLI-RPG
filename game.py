import time
import random
from map import Map
from player import Player
from enemy import Enemy


class Game:
    def __init__(self, map_width: int, map_height: int):
        self.game_map: Map = Map(map_width, map_height)
        self.player: Player = Player()
        self.enemies: list = []

        # Keep track of turns
        self.turns = 0

    def get_random_walkable_position(self, game_map: Map) -> tuple[int, int]:
        while True:
            x = random.randint(1, game_map.width - 3)
            y = random.randint(1, game_map.height - 2)

            if game_map.base_map[y][x].walkable:
                return x, y

    def is_adjacent(self, player: Player, enemy: Enemy) -> tuple:
        dx = abs(player.pos[0] - enemy.pos[0])
        dy = abs(player.pos[1] - enemy.pos[1])
        # If they are next to each other:
        # one axis differs by 1
        # the other axis differs by 0
        return dx + dy == 1 or dx + dy == 0

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

    def move_player(self, valid_moves, movement):
        self.turns += 1

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

    def move_enemies(self):
        # ---------------
        # Enemy movement
        # ---------------
        for enemy in self.enemies:
            # Collect all valid neighboring tiles to prevent getting 'stuck'
            valid_moves = [
                (dx, dy)
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]
                if self.can_move_to(self.game_map, enemy.pos[0] + dx, enemy.pos[1] + dy)
            ]
            if valid_moves:
                dx, dy = random.choice(valid_moves)
                enemy.pos[0] += dx
                enemy.pos[1] += dy

    def battle(self, player, enemy):
        print("You've encountered an enemy! Prepare for battle!\n")

        while player.hp > 0 and enemy.hp > 0:
            print("1. Attack    2. Flee\n")
            print(f"Current HP: {player.hp}")
            print(f"Enemy HP: {enemy.hp}")

            player_choice = input(">>> ")

            if player_choice not in ("1", "2"):
                print("Enter a valid choice. 1 or 2.")

            elif player_choice == "1":
                enemy.hp -= 1
                if enemy.hp <= 0:
                    print("Enemy defeated!")
                    return "enemy_killed"

                else:
                    # Enemy hits player back
                    player.hp -= 1

            elif player_choice == "2":
                return "fled"

        if player.hp <= 0:
            return "player_dead"

    def run(self):
        self.spawn_enemies(self.game_map, self.enemies, 5)

        self.player.pos = list(self.get_random_walkable_position(self.game_map))

        # Perform initial draw so player appears before the first move
        self.game_map.update_map(self.player, self.enemies)

        while True:
            # Clear screen with ANSI code
            print("\033c", end="")

            self.game_map.display_map()

            # Battles
            for enemy in self.enemies:
                if self.is_adjacent(self.player, enemy):
                    result = self.battle(self.player, enemy)

                    if result == "enemy_killed":
                        self.enemies.remove(enemy)
                        # Win condition
                        # All enemies killed = Winner
                        if len(self.enemies) == 0:
                            # Clear screen
                            print("\033c", end="")

                            # Print win message
                            print(
                                "Congrats! You've defeated all enemies and returned peace to the lands!"
                            )
                            time.sleep(1.0)
                            raise SystemExit()

                        break

                    elif result == "fled":
                        break
                    elif result == "player_dead":
                        print("You Died!")
                        time.sleep(0.5)
                        raise SystemExit()

            # UI Info
            print(f"Pos: {self.player.pos}")
            print(f"HP: {self.player.hp}")
            print(f"Enemies Left: {len(self.enemies)}")
            print(f"Turns Survived: {self.turns}\n")

            # ---------------
            # Player movement
            # ---------------
            # Get valid player moves
            valid_moves = self.player.get_valid_moves(self.game_map)

            print(f" W - UP: {'OK' if valid_moves['w'] else 'BLOCKED'}")
            print(f" A - LEFT: {'OK' if valid_moves['a'] else 'BLOCKED'}")
            print(f" S - DOWN: {'OK' if valid_moves['s'] else 'BLOCKED'}")
            print(f" D - RIGHT: {'OK' if valid_moves['d'] else 'BLOCKED'}")
            print(" R - Rest to regain HP\n")

            player_input = input(">>> ").lower()

            # Press 'r' to rest and regain hp
            if player_input == "r":
                self.player.hp = min(self.player.hp + 1, 10)

            self.move_player(valid_moves, player_input)
            self.move_enemies()

            # Update visuals
            self.game_map.update_map(self.player, self.enemies)
