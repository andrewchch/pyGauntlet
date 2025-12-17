"""
Test animated character sprite functionality
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from entities.character import AnimatedCharacter
from constants import *


def test_sprite_sheet_loading():
    """Test that sprite sheet loads correctly"""
    pygame.init()
    pygame.display.set_mode((800, 600))  # Need display mode to load images
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    char = AnimatedCharacter(100, 100, sprite_path)
    
    # Verify sprite sheet was loaded
    assert char.sprite_sheet is not None, "Sprite sheet should be loaded"
    assert char.sprite_sheet.get_width() > 0, "Sprite sheet should have width"
    assert char.sprite_sheet.get_height() > 0, "Sprite sheet should have height"
    
    print("✓ Sprite sheet loaded successfully")
    pygame.quit()


def test_animation_frames_extracted():
    """Test that animation frames are extracted for all directions"""
    pygame.init()
    pygame.display.set_mode((800, 600))  # Need display mode to load images
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    char = AnimatedCharacter(100, 100, sprite_path)
    
    # Verify all directions have frames
    directions = [
        AnimatedCharacter.DIRECTION_UP,
        AnimatedCharacter.DIRECTION_DOWN,
        AnimatedCharacter.DIRECTION_LEFT,
        AnimatedCharacter.DIRECTION_RIGHT,
    ]
    
    for direction in directions:
        assert direction in char.animations, f"Direction {direction} should have animations"
        frames = char.animations[direction]
        assert len(frames) == 9, f"Direction {direction} should have 9 frames"
        
        # Verify each frame is a valid surface
        for i, frame in enumerate(frames):
            assert isinstance(frame, pygame.Surface), f"Frame {i} should be a Surface"
            assert frame.get_width() == SPRITE_FRAME_SIZE, f"Frame {i} should be {SPRITE_FRAME_SIZE}px wide"
            assert frame.get_height() == SPRITE_FRAME_SIZE, f"Frame {i} should be {SPRITE_FRAME_SIZE}px tall"
    
    print("✓ Animation frames extracted for all directions")
    pygame.quit()


def test_direction_change():
    """Test that character direction changes based on movement"""
    pygame.init()
    pygame.display.set_mode((800, 600))  # Need display mode to load images
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    char = AnimatedCharacter(100, 100, sprite_path)
    
    # Test all directions
    test_cases = [
        ((0, -1), AnimatedCharacter.DIRECTION_UP, "UP"),
        ((0, 1), AnimatedCharacter.DIRECTION_DOWN, "DOWN"),
        ((-1, 0), AnimatedCharacter.DIRECTION_LEFT, "LEFT"),
        ((1, 0), AnimatedCharacter.DIRECTION_RIGHT, "RIGHT"),
    ]
    
    for (dx, dy), expected_dir, name in test_cases:
        char.set_direction(dx, dy)
        assert char.current_direction == expected_dir, f"Direction should be {name}"
        assert char.is_moving == True, f"Should be moving when direction is {name}"
        print(f"✓ Direction changes correctly for {name}")
    
    # Test idle state
    char.set_direction(0, 0)
    assert char.is_moving == False, "Should not be moving when dx=dy=0"
    print("✓ Idle state detected correctly")
    
    pygame.quit()


def test_animation_cycling():
    """Test that animation frames cycle correctly"""
    pygame.init()
    pygame.display.set_mode((800, 600))  # Need display mode to load images
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    char = AnimatedCharacter(100, 100, sprite_path)
    
    # Set character to moving down
    char.set_direction(0, 1)
    assert char.is_moving == True, "Character should be moving"
    
    # Initial frame should be 0
    assert char.animation_frame == 0.0, "Initial animation frame should be 0"
    
    # Update animation multiple times
    initial_image = char.image
    updates_needed = int(1.0 / char.animation_speed) + 1  # Enough to advance one frame
    
    for _ in range(updates_needed):
        char.update_animation()
    
    # Frame should have advanced
    assert char.animation_frame > 0, "Animation frame should have advanced"
    
    print(f"✓ Animation cycling works (frame: {char.animation_frame})")
    pygame.quit()


def test_idle_frame():
    """Test that idle frame (frame 0) is used when not moving"""
    pygame.init()
    pygame.display.set_mode((800, 600))  # Need display mode to load images
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    char = AnimatedCharacter(100, 100, sprite_path)
    
    # Set to not moving
    char.set_direction(0, 0)
    char.update_animation()
    
    # Should use frame 0 (idle frame)
    assert char.animation_frame == 0.0, "Should use frame 0 when idle"
    
    # Verify image matches first frame of current direction
    expected_frame = char.animations[char.current_direction][0]
    assert char.image == expected_frame, "Image should match idle frame"
    
    print("✓ Idle frame used when not moving")
    pygame.quit()


def test_character_positioning():
    """Test that character is positioned correctly"""
    pygame.init()
    pygame.display.set_mode((800, 600))  # Need display mode to load images
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    x, y = 200, 300
    char = AnimatedCharacter(x, y, sprite_path)
    
    assert char.rect.x == x, f"Character x should be {x}"
    assert char.rect.y == y, f"Character y should be {y}"
    
    print("✓ Character positioned correctly")
    pygame.quit()


if __name__ == "__main__":
    print('='*60)
    print('Testing Animated Character')
    print('='*60)
    print()
    
    test_sprite_sheet_loading()
    test_animation_frames_extracted()
    test_direction_change()
    test_animation_cycling()
    test_idle_frame()
    test_character_positioning()
    
    print()
    print('='*60)
    print('All animation tests passed!')
    print('='*60)
