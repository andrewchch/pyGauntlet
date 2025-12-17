# Character Sprite Animation Implementation

## Overview
This implementation adds sprite-based walking animations to the pyGauntlet game using the LPC (Liberated Pixel Cup) sprite sheet format.

## Files Created

### Core Implementation
- **`entities/__init__.py`** - Package initialization for entity classes
- **`entities/character.py`** - `AnimatedCharacter` class implementing sprite-based animations

### Tests
- **`test_animation.py`** - Unit tests for AnimatedCharacter functionality
- **`test_animation_integration.py`** - Integration tests with game loop
- **`test_animation_visual.py`** - Interactive visual test script

### Demo Scripts
- **`create_character_showcase.py`** - Creates showcase screenshot of all animations

## Files Modified

### `player.py`
- Updated to use `AnimatedCharacter` for sprite rendering
- Maintains backward compatibility with fallback to colored square
- Integrates animation updates in the `update()` method

### `constants.py`
- Added `SPRITE_FRAME_SIZE = 64` - Size of sprite frames
- Added `ANIMATION_SPEED = 0.15` - Animation speed multiplier

### `test_health_system.py`
- Fixed to initialize pygame display before creating Player objects

### `.gitignore`
- Added `character_animation_showcase.png` to ignore demo screenshots

## Architecture

### AnimatedCharacter Class
Located in `entities/character.py`, this class provides:

**Key Features:**
- Loads LPC sprite sheets (832x3456 pixels with 64x64 frames)
- Extracts 9-frame walking animations for 4 directions
- Smooth animation cycling with configurable speed
- Idle state detection (shows frame 0 when not moving)
- Direction-based animation selection

**Direction Mapping:**
```python
DIRECTION_UP = 0    # Row 0 in sprite sheet
DIRECTION_LEFT = 1  # Row 1 in sprite sheet
DIRECTION_DOWN = 2  # Row 2 in sprite sheet
DIRECTION_RIGHT = 3 # Row 3 in sprite sheet
```

**Public Methods:**
- `__init__(x, y, sprite_sheet_path, frame_size=64, animation_speed=0.15)` - Initialize character
- `set_direction(dx, dy)` - Set movement direction (-1, 0, or 1 for each axis)
- `update_animation()` - Advance animation frame (call each game loop iteration)
- `get_current_frame()` - Get current animation frame surface

### Integration with Player Class

The `Player` class now:
1. Attempts to load animated sprite on initialization
2. Falls back to colored square if sprite sheet not found
3. Updates animation direction based on keyboard input
4. Advances animation frame each update
5. Syncs sprite position with player rect

**Code Flow:**
```python
# In Player.__init__():
if sprite_sheet_exists:
    self.animated_char = AnimatedCharacter(x, y, sprite_path)
    self.has_animation = True

# In Player.update():
if self.has_animation:
    # Update direction based on input
    self.animated_char.set_direction(dx, dy)
    
    # Advance animation
    self.animated_char.update_animation()
    
    # Update displayed image
    self.image = self.animated_char.image
```

## Sprite Sheet Format

The implementation uses LPC (Liberated Pixel Cup) sprite sheet format:

**Dimensions:** 832 x 3456 pixels (13 columns × 54 rows)
**Frame Size:** 64 x 64 pixels
**Walking Animations:** First 4 rows (9 frames each)

**Layout:**
```
Row 0: Walk Up    [9 frames: 0-8]
Row 1: Walk Left  [9 frames: 0-8]
Row 2: Walk Down  [9 frames: 0-8]
Row 3: Walk Right [9 frames: 0-8]
```

**Frame Extraction:**
Each frame is extracted from position `(col * 64, row * 64)` with size `(64, 64)`.

## Animation System

### Frame Cycling
- Animation frame is stored as float for smooth progression
- Advances by `animation_speed` (default 0.15) each update
- Wraps around when reaching frame 9 (last frame)
- At 60 FPS with speed 0.15, full cycle takes ~4 seconds

### Idle State
- When `is_moving` is False, displays frame 0 (idle pose)
- Resets animation frame to 0.0
- Maintains current direction

### Direction Priority
When multiple keys are pressed:
1. Vertical movement (up/down) takes priority
2. Then horizontal movement (left/right)
3. Last valid direction is maintained

## Testing

### Unit Tests (`test_animation.py`)
✓ Sprite sheet loading
✓ Animation frame extraction (all 4 directions)
✓ Direction changes based on movement
✓ Animation frame cycling
✓ Idle frame display
✓ Character positioning

### Integration Tests (`test_animation_integration.py`)
✓ Animated player in game context
✓ Animation direction updates
✓ Idle state detection
✓ Frame advancement during movement
✓ Sprite size verification
✓ Animation persistence across updates

### Existing Tests
✓ All player movement tests pass
✓ Health system tests pass
✓ No regressions introduced

## Usage Examples

### Creating an Animated Character
```python
from entities.character import AnimatedCharacter

# Create character at position (100, 100)
char = AnimatedCharacter(
    x=100, 
    y=100, 
    sprite_sheet_path='resources/sprites/character-spritesheet.png',
    frame_size=64,
    animation_speed=0.15
)
```

### Updating Animation
```python
# In game loop:
keys = pygame.key.get_pressed()

# Determine movement
dx = 1 if keys[pygame.K_RIGHT] else (-1 if keys[pygame.K_LEFT] else 0)
dy = 1 if keys[pygame.K_DOWN] else (-1 if keys[pygame.K_UP] else 0)

# Update direction and animation
char.set_direction(dx, dy)
char.update_animation()

# Draw
screen.blit(char.image, char.rect)
```

### Running Visual Tests
```bash
# Interactive animation test
python test_animation_visual.py

# Create showcase screenshot
python create_character_showcase.py
```

## Performance Considerations

- Sprite sheet is loaded once during initialization
- All frames are extracted and cached in memory
- No file I/O during gameplay
- Animation uses integer frame indexing from float counter
- Only one 64x64 surface is blitted per character per frame

## Future Enhancements

Possible improvements:
- Add attack animations (slash, spellcast)
- Support for different character types/classes
- Animation events (callbacks on specific frames)
- Rotation/flip for additional directions
- Sprite color tinting for player customization
- Animation blending/transitions

## Compliance

**PEP 8:** All code follows Python style guidelines
- Type hints on all function parameters and return values
- Docstrings for classes and public methods
- Proper naming conventions
- Line length < 100 characters

**Project Guidelines:**
- Uses pygame sprite system
- Component-based architecture
- Separation of concerns (animation logic separate from game logic)
- Backward compatible (fallback to colored squares)
- Well-tested with comprehensive test coverage
