# pyGauntlet
A Gauntlet II-inspired game implementation in pygame

## Description
pyGauntlet is a top-down action game inspired by the classic arcade game Gauntlet II. Control a Warrior character through a tiled, scrolling dungeon filled with enemies spawned from generators. Battle your way through hordes of foes using projectile attacks while navigating around walls and obstacles.

## Features
- **Player Character (Warrior)**: Control a blue warrior that can move in four directions
- **Movement**: Use arrow keys to navigate through the dungeon
- **Combat**: Press SPACE to fire projectiles at enemies
- **Enemy Spawners**: Purple generators continuously spawn red enemies
- **AI Enemies**: Enemies chase the player using intelligent pathfinding
- **Collision Detection**: Both player and enemies are blocked by gray wall tiles
- **Scrolling Camera**: The view follows the player through the large dungeon map
- **Real-time Action**: Fast-paced gameplay at 60 FPS

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/andrewchch/pyGauntlet.git
cd pyGauntlet
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

### Running the Game
```bash
python main.py
```

### Controls
- **Arrow Keys**: Move the Warrior character
  - ↑ Up
  - ↓ Down
  - ← Left
  - → Right
- **SPACE**: Fire projectile in the last direction moved
- **ESC / Close Window**: Quit the game

### Game Elements
- **Blue Square**: Your Warrior character
- **Red Squares**: Enemy creatures that chase you
- **Purple Squares**: Enemy generators that spawn enemies
- **Gray Blocks**: Walls that block movement
- **Yellow Dots**: Your projectiles

### Objective
Survive as long as possible while fighting off waves of enemies. Destroy enemies by shooting them with projectiles. The enemy counter at the top-left shows how many foes you're facing.

## Project Structure
```
pyGauntlet/
├── main.py              # Entry point for the game
├── game.py              # Main game loop and logic
├── player.py            # Player character class
├── enemy.py             # Enemy AI and behavior
├── generator.py         # Enemy spawner class
├── projectile.py        # Projectile/bullet class
├── wall.py              # Wall tile class
├── game_map.py          # Map layout and generation
├── camera.py            # Scrolling camera system
├── constants.py         # Game configuration and constants
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Testing
Run the component tests to verify all game systems:
```bash
python test_components.py
```

## Customization
You can modify game parameters in `constants.py`:
- `PLAYER_SPEED`: How fast the player moves
- `ENEMY_SPEED`: How fast enemies move
- `PROJECTILE_SPEED`: How fast projectiles travel
- `SPAWN_INTERVAL`: Time between enemy spawns (milliseconds)
- `MAP_WIDTH` / `MAP_HEIGHT`: Size of the game world
- Colors and other visual settings

## Future Enhancements
Potential features for future versions:
- Multiple character classes
- Power-ups and health system
- More enemy types
- Destroyable generators
- Score tracking
- Multiple levels
- Sound effects and music

## License
This project is open source and available for educational purposes.

## Credits
Inspired by the classic Gauntlet II arcade game by Atari Games.
