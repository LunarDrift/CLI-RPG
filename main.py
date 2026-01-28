import random
from map import Map
from player import Player
from enemy import Enemy


def get_random_walkable_position(game_map) -> tuple[int, int]:
    while True:
        x = random.randint(1, game_map.width - 3)
        y = random.randint(1, game_map.height - 2)

        if game_map.base_map[y][x].walkable:
            return x, y


def main():
    map_w, map_h = 90, 30
    game_map = Map(map_w, map_h)
    player = Player()

    enemy_x, enemy_y = get_random_walkable_position(game_map)
    enemy = Enemy(enemy_x, enemy_y)
    enemies = [enemy]

    player.pos = list(get_random_walkable_position(game_map))

    # Perform initial draw so player appears before the first move
    game_map.update_map(player, enemies)

    while True:
        # Clear screen with ANSI code
        print("\033c", end="")

        game_map.display_map()

        # Get valid player moves
        valid_moves = player.get_valid_moves(game_map)

        print(f"W - UP: {'OK' if valid_moves['w'] else 'BLOCKED'}")
        print(f"A - LEFT: {'OK' if valid_moves['a'] else 'BLOCKED'}")
        print(f"S - DOWN: {'OK' if valid_moves['s'] else 'BLOCKED'}")
        print(f"D - RIGHT: {'OK' if valid_moves['d'] else 'BLOCKED'}")

        # print(f"Pos: {player.pos}")  # Debugging info

        movement = input(">>> ").lower()

        # Only move if the key exists in our dict AND it is True
        if movement in valid_moves and valid_moves[movement]:
            match movement:
                case "w":
                    player.move(0, -1)
                case "a":
                    player.move(-1, 0)
                case "s":
                    player.move(0, 1)
                case "d":
                    player.move(1, 0)

        else:
            print("You can't go that way!")
            import time

            time.sleep(0.5)

        # Enemy movement
        for enemy in enemies:
            enemy.move()

        # Update visuals
        game_map.update_map(player, enemies)


if __name__ == "__main__":
    main()
