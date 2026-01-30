# CLI Roguelike Adventure

A simple text-based roguelike game built in Python.
Move around a small world map and defeat all enemies to win.
Made for boot.dev personal project #1

---
### Gameplay
- Explore a map made of plains, forests, mountains, and water
- Some tiles are **impassable** (water and mountains)
- Randomly placed enemies move around the map
- Encountering an enemy triggers a battle:
	- Attack to reduce enemy HP
	- Flee to escape
- Win the game by defeating all enemies
- Lose the game if your HP reaches 0

---
### Controls
| Key | Action             |
| --- | ------------------ |
| `W` | Move up            |
| `A` | Move left          |
| `S` | Move down          |
| `D` | Move right         |
| `R` | Rest (regain HP)   |
| `1` | Attack (in battle) |
| `2` | Flee (in battle)   |

---
### Installation
1. Clone the repo:
```bash
git clone https://github.com/LunarDrift/CLI-RPG.git
cd CLI-RPG
```
1. Make sure you have Python 3 installed:
```bash
python --version
```
1. Run the game:
```bash
python main.py
```

---
### How to Play
1. Start the game. Your player will spawn at a random walkable location
2. Move around the map using WASD
3. Avoid mountains and water
4. Enemies move randomly each turn
5. If you move next to/on top of an enemy, choose **Attack** or **Flee**
6. Keep track of your and the enemy's HP
7. Defeat all enemies to win

---
### Project Features
- Randomly generated map with terrain patches (plains, forest, pines, mountain, water)
- Player movement with collision detection
- Enemy movement and simple AI (avoiding impassable tiles)
- Basic battle system (Attack / Flee)
- Win/Loss conditions
- Text-based rendering with colored ANSI tiles

---
### Future Improvements
- Smooth terminal rendering (curses)
- Multiple enemy types with different stats
- Item pickups and inventory system
- Procedural map generation
- More complex battle mechanics
