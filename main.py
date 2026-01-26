from map import Map
from player import Player
import random


def main():
    map_w, map_h = 30, 15
    game_map = Map(map_w, map_h)
    player = Player()

    # Spawn Logic:
    # Set player to a random spot, or a fixed spot like (1, 1)
    # Ideally, you would check game_map.base_map[y][x] to make sure
    # you aren't spawning inside a mountain or water
    player.pos = [random.randint(1, map_w - 2), random.randint(1, map_h - 2)]

    # Perform initial draw so player appears before the first move
    game_map.update_map(player.pos, player.symbol)

    while True:
        # Clear screen with ANSI code
        print("\033c", end="")

        game_map.display_map()

        # Get valid player moves
        valid_moves = player.get_valid_moves(game_map)

        print(f"W: {'OK' if valid_moves['w'] else 'BLOCKED'}")
        print(f"A: {'OK' if valid_moves['a'] else 'BLOCKED'}")
        print(f"S: {'OK' if valid_moves['s'] else 'BLOCKED'}")
        print(f"D: {'OK' if valid_moves['d'] else 'BLOCKED'}")

        # print(f"Pos: {player.pos}")  # Debugging info

        movement = input(">>> ").lower()

        # Store previous position in case we need to revert (collision logic later)
        dx, dy = 0, 0

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

        # Update visuals
        game_map.update_map(player.pos, player.symbol)


if __name__ == "__main__":
    main()
