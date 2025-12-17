"""
Integration test for animated character in game loop
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from game import Game
from constants import *


def test_animated_player_in_game():
    """Test that animated player works in the game context"""
    pygame.init()
    game = Game()
    
    # Verify player has animation enabled
    assert game.player.has_animation == True, "Player should have animation enabled"
    assert game.player.animated_char is not None, "Player should have AnimatedCharacter instance"
    
    print("✓ Player has animation enabled")
    
    # Verify initial state
    initial_direction = game.player.animated_char.current_direction
    assert initial_direction in [0, 1, 2, 3], "Initial direction should be valid"
    
    print(f"✓ Player has valid initial direction: {initial_direction}")
    
    # Simulate movement and check animation updates
    class KeyState:
        """Helper class to simulate key presses"""
        def __init__(self, active_key):
            self.active_key = active_key
        def __getitem__(self, key):
            return key == self.active_key
    
    # Test moving right
    keys = KeyState(pygame.K_RIGHT)
    game.player.update(keys, game.game_map.walls)
    
    # Verify animation direction changed
    assert game.player.animated_char.current_direction == game.player.animated_char.DIRECTION_RIGHT, \
        "Direction should be RIGHT when moving right"
    assert game.player.animated_char.is_moving == True, "Character should be marked as moving"
    
    print("✓ Animation direction updates when moving right")
    
    # Test moving up
    keys = KeyState(pygame.K_UP)
    game.player.update(keys, game.game_map.walls)
    
    assert game.player.animated_char.current_direction == game.player.animated_char.DIRECTION_UP, \
        "Direction should be UP when moving up"
    
    print("✓ Animation direction updates when moving up")
    
    # Test idle state
    keys = KeyState(None)  # No keys pressed
    game.player.update(keys, game.game_map.walls)
    
    assert game.player.animated_char.is_moving == False, "Character should not be moving when no keys pressed"
    
    print("✓ Animation correctly detects idle state")
    
    # Verify image updates
    initial_image = game.player.image
    
    # Move and update multiple times to advance animation
    keys = KeyState(pygame.K_DOWN)
    for _ in range(10):
        game.player.update(keys, game.game_map.walls)
    
    # Image should have been updated (though may be same frame at different times)
    assert game.player.image is not None, "Player image should be set"
    assert game.player.animated_char.animation_frame > 0, "Animation frame should have advanced"
    
    print(f"✓ Animation frames advance during movement (frame: {game.player.animated_char.animation_frame})")
    
    pygame.quit()


def test_player_sprite_size():
    """Test that player sprite has reasonable size"""
    pygame.init()
    game = Game()
    
    # Verify sprite size
    width = game.player.image.get_width()
    height = game.player.image.get_height()
    
    assert width == SPRITE_FRAME_SIZE, f"Player width should be {SPRITE_FRAME_SIZE}, got {width}"
    assert height == SPRITE_FRAME_SIZE, f"Player height should be {SPRITE_FRAME_SIZE}, got {height}"
    
    print(f"✓ Player sprite size is {width}x{height}")
    
    pygame.quit()


def test_animation_persists_across_updates():
    """Test that animation state persists correctly across game updates"""
    pygame.init()
    game = Game()
    
    class KeyState:
        def __init__(self, active_key):
            self.active_key = active_key
        def __getitem__(self, key):
            return key == self.active_key
    
    # Move in one direction for several frames
    keys = KeyState(pygame.K_LEFT)
    
    frame_values = []
    for i in range(20):
        game.player.update(keys, game.game_map.walls)
        frame_values.append(game.player.animated_char.animation_frame)
    
    # Verify frames are advancing
    assert frame_values[-1] > frame_values[0], "Animation frames should advance over time"
    
    # Verify direction stayed consistent
    assert game.player.animated_char.current_direction == game.player.animated_char.DIRECTION_LEFT, \
        "Direction should remain LEFT throughout"
    
    print(f"✓ Animation advances over {len(frame_values)} updates: {frame_values[0]:.2f} -> {frame_values[-1]:.2f}")
    
    pygame.quit()


if __name__ == "__main__":
    print('='*60)
    print('Testing Animated Character Game Integration')
    print('='*60)
    print()
    
    test_animated_player_in_game()
    test_player_sprite_size()
    test_animation_persists_across_updates()
    
    print()
    print('='*60)
    print('All integration tests passed!')
    print('='*60)
