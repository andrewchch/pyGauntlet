# Game Menu Feature

## Overview
The game now includes a menu system that displays when the game starts and when paused.

## Usage

### Starting the Game
1. Run `python main.py`
2. The game displays a menu with "pyGauntlet" title and "Play" option
3. Press **RETURN** or **SPACE** to start playing

### Pausing the Game
- During gameplay, press **ESC** to pause
- The menu appears over the game with "Resume" option
- The game state is frozen (no updates)

### Resuming the Game
From the pause menu, you can:
- Press **RETURN** or **SPACE** to select "Resume", or
- Press **ESC** again to toggle back to playing

## Implementation Details

### Game States
The game now has three states:
- `STATE_MENU` (0) - Initial menu before starting
- `STATE_PLAYING` (1) - Active gameplay
- `STATE_PAUSED` (2) - Game paused with menu overlay

### Files Modified
- `constants.py` - Added game state constants
- `game.py` - Integrated menu system and state management
- `menu.py` - New menu class for rendering and input handling

### Controls
- **Arrow Keys**: Move player (only when playing)
- **SPACE**: Fire projectile (only when playing) OR select menu option
- **RETURN**: Select menu option
- **ESC**: Pause/resume game (toggle)

## Testing
Run the menu tests:
```bash
python test_menu.py          # Unit tests for menu component
python test_menu_flow.py     # Integration test for menu flow
```

All existing tests continue to pass.
