# Copilot Instructions for pyGauntlet

## Project Overview
pyGauntlet is an implementation of the classic Gauntlet II arcade game using pygame. The project aims to recreate the dungeon-crawling, multiplayer action experience of the original game.

## Development Guidelines

### Code Style and Standards
- Follow PEP 8 Python style guidelines
- Use type hints for function parameters and return values
- Write clear, descriptive docstrings for classes and functions
- Prefer composition over inheritance where appropriate
- Keep functions focused and single-purpose (max ~50 lines)
- Use meaningful variable names that reflect game concepts (e.g., `player_health`, `enemy_position`)

### Project Architecture
- Use pygame's sprite system for game entities (players, enemies, items, walls)
- Implement a game state manager for different screens (menu, gameplay, game over)
- Separate game logic from rendering code
- Use a component-based approach for game entities where possible
- Organize code into logical modules:
  - `entities/` - Player, enemies, items, projectiles
  - `levels/` - Level data, map loading, dungeon generation
  - `ui/` - Menus, HUD, score display
  - `assets/` - Images, sounds, fonts
  - `utils/` - Helper functions, constants, configuration

### Pygame Best Practices
- Use `pygame.sprite.Group` for managing collections of sprites
- Implement proper game loop with fixed timestep for consistent physics
- Handle events in a centralized event handler
- Use `pygame.Surface.blit()` efficiently for rendering
- Load assets once during initialization, not in game loop
- Use sprite sheets for animations where appropriate
- Implement proper collision detection using pygame's collision methods

### Game-Specific Features
- Support multiple character classes (Warrior, Valkyrie, Wizard, Elf)
- Implement various enemy types with different behaviors
- Create a health system with food consumption mechanics (health constantly decreases, food restores it)
- Support multiplayer (local co-op)
- Implement power-ups and special items (potions, keys, treasure)
- Create procedural or hand-designed dungeon levels
- Add score tracking and high scores

### Testing
- Write unit tests for game logic (health calculations, collision detection, scoring)
- Test edge cases (player death, level completion, item pickup)
- Manual testing for gameplay feel and balance
- Test on different screen resolutions

### Dependencies
- Use `pygame` for game engine
- Minimize external dependencies
- Document any additional dependencies in requirements.txt
- Pin dependency versions for reproducibility

### Performance Considerations
- Profile code to identify bottlenecks
- Optimize rendering by only drawing visible sprites
- Use dirty rect rendering for performance
- Keep sprite counts reasonable (cull off-screen sprites)
- Cache computed values when appropriate

### Assets and Resources
- Organize assets by type (sprites, sounds, music, fonts)
- Use appropriate file formats (PNG for sprites with transparency, OGG/WAV for audio)
- Document asset sources and licensing
- Consider creating placeholder art for development

### Comments and Documentation
- Comment complex game logic and algorithms
- Document game mechanics in code comments
- Keep README.md updated with setup instructions and gameplay info
- Add inline comments for non-obvious pygame patterns

### Git Workflow
- Write clear commit messages describing changes
- Keep commits focused on single features or fixes
- Don't commit compiled files or caches (use .gitignore)
- Don't commit large binary assets without consideration

## Common Patterns to Use

### Game Loop
```python
FPS = 60  # Target frame rate; consider making configurable for different hardware
clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(FPS) / 1000.0  # Delta time in seconds
    # Handle events
    # Update game state
    # Render
    pygame.display.flip()
```

### Sprite Creation
```python
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def update(self, dt):
        # Update sprite state
        pass
```

### Collision Detection
```python
hits = pygame.sprite.spritecollide(player, enemy_group, False)
for enemy in hits:
    # Handle collision
    pass
```

## Things to Avoid
- Don't use global variables excessively; prefer dependency injection
- Avoid hardcoding values; use constants or configuration files
- Don't mix game logic with rendering code
- Avoid blocking operations in the game loop
- Don't reinvent the wheel; use pygame's built-in features

## Security and Best Practices
- Validate user input from configuration files
- Be cautious with `eval()` and `exec()`
- Handle file I/O errors gracefully
- Don't expose sensitive data in version control
