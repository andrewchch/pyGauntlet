"""
Test player movement functionality
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from game import Game
from constants import *


def test_player_spawns_without_collision():
    """Test that player spawns in a position without wall collision"""
    pygame.init()
    game = Game()
    
    # Check player doesn't overlap with walls
    overlap = pygame.sprite.spritecollideany(game.player, game.game_map.walls)
    assert overlap is None, f"Player spawns overlapping wall at {overlap.rect if overlap else 'N/A'}"
    print("✓ Player spawns without wall collision")
    pygame.quit()


def test_player_can_move_in_all_directions():
    """Test that player can move in all four cardinal directions"""
    pygame.init()
    game = Game()
    
    # Helper class to simulate key presses
    class KeyState:
        def __init__(self, active_key):
            self.active_key = active_key
        def __getitem__(self, key):
            return key == self.active_key
    
    # Test all four directions
    directions = [
        (pygame.K_RIGHT, 'x', PLAYER_SPEED, 'RIGHT'),
        (pygame.K_LEFT, 'x', -PLAYER_SPEED, 'LEFT'),
        (pygame.K_DOWN, 'y', PLAYER_SPEED, 'DOWN'),
        (pygame.K_UP, 'y', -PLAYER_SPEED, 'UP'),
    ]
    
    for key, axis, expected_delta, name in directions:
        # Reset player to safe starting position
        game.player.rect.x = 480
        game.player.rect.y = 480
        
        initial_value = getattr(game.player.rect, axis)
        keys = KeyState(key)
        game.player.update(keys, game.game_map.walls)
        new_value = getattr(game.player.rect, axis)
        
        delta = new_value - initial_value
        assert delta == expected_delta, f"Expected {name} movement of {expected_delta}, got {delta}"
        print(f"✓ Player can move {name}")
    
    pygame.quit()


def test_player_collision_with_walls():
    """Test that player is blocked by walls"""
    pygame.init()
    game = Game()
    
    # Position player next to a wall at y=10 (tile coordinates)
    # Wall is at x=10-19, y=10 (world coordinates 320-608, 320)
    # Place player at (9, 10) in tiles = (288, 320) in world
    game.player.rect.x = 9 * TILE_SIZE
    game.player.rect.y = 10 * TILE_SIZE
    
    # Try to move right (into the wall)
    class KeyState:
        def __init__(self, active_key):
            self.active_key = active_key
        def __getitem__(self, key):
            return key == self.active_key
    
    initial_x = game.player.rect.x
    keys = KeyState(pygame.K_RIGHT)
    
    # Player should not move through the wall
    for _ in range(10):  # Try multiple times
        game.player.update(keys, game.game_map.walls)
    
    # Player might move a bit but should be blocked before entering the wall
    # Player is 28 pixels wide, wall starts at x=320
    # Player left edge starts at 288, can move to at most 320 - 28 = 292
    assert game.player.rect.x < 10 * TILE_SIZE, "Player should be blocked by wall"
    print(f"✓ Player blocked by walls (position: {game.player.rect.x})")
    
    pygame.quit()


if __name__ == "__main__":
    print('='*60)
    print('Testing Player Movement')
    print('='*60)
    print()
    
    test_player_spawns_without_collision()
    test_player_can_move_in_all_directions()
    test_player_collision_with_walls()
    
    print()
    print('='*60)
    print('All movement tests passed!')
    print('='*60)
