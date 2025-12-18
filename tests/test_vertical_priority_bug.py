"""
Test case that demonstrates the specific bug in enemy movement logic
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from enemy import Enemy
from player import Player
from wall import Wall
from game_map import GameMap
from constants import TILE_SIZE

def test_vertical_movement_blocked_should_try_horizontal():
    """
    This test demonstrates the exact bug:
    When abs(dy) > abs(dx), the enemy only tries vertical movement.
    If that's blocked, it doesn't try horizontal movement.
    
    Setup:
        P . . .
        . . . .
        W W W W  <- wall blocking vertical path
        . E . .  <- enemy positioned so dy > dx (prefers vertical)
        
    Expected: Enemy should move left toward player when up is blocked
    Bug: Enemy stops moving because it only tries vertical
    """
    print("Test: Vertical Movement Blocked Should Try Horizontal")
    print("=" * 70)
    
    pygame.init()
    pygame.display.set_mode((1, 1))
    
    # Position player and enemy such that:
    # - Enemy is almost directly below player (dy > dx)
    # - This makes enemy prioritize vertical movement
    # - But there's a wall blocking vertical movement
    
    player = Player(TILE_SIZE, TILE_SIZE)  
    # Position enemy just below the wall (at 2*TILE_SIZE)
    # The wall occupies y=64 to y=96 (TILE_SIZE = 32, so wall is from 64 to 96)
    # Enemy rect is TILE_SIZE-4 = 28 pixels tall
    # Position enemy so its top is at y=97 (just below wall bottom at 96)
    enemy = Enemy(TILE_SIZE + 10, 2 * TILE_SIZE + TILE_SIZE - 1)  # y = 95, enemy will collide immediately
    
    # Create a horizontal wall between them (Wall class multiplies coords by TILE_SIZE)
    walls = pygame.sprite.Group()
    for i in range(5):
        wall = Wall(i, 2)  # This creates walls at y = 2 * TILE_SIZE = 64
        walls.add(wall)
    
    game_map = GameMap()
    
    dx = abs(player.rect.centerx - enemy.rect.centerx)
    dy = abs(player.rect.centery - enemy.rect.centery)
    
    print(f"Player position: ({player.rect.x}, {player.rect.y})")
    print(f"Enemy position:  ({enemy.rect.x}, {enemy.rect.y})")
    print(f"Distances: dx={dx}, dy={dy}")
    print(f"Enemy will prioritize: {'VERTICAL' if dy > dx else 'HORIZONTAL'} movement")
    print(f"Wall at y={2 * TILE_SIZE} blocks upward movement")
    
    # Verify our setup
    assert dy > dx, "Test setup error: dy should be > dx for this test"
    
    print("\nRunning 20 updates:")
    print("-" * 70)
    
    moved = False
    last_printed_pos = (enemy.rect.x, enemy.rect.y)
    
    for i in range(20):
        old_pos = (enemy.rect.x, enemy.rect.y)
        enemy.update(player, walls, game_map)
        new_pos = (enemy.rect.x, enemy.rect.y)
        
        if old_pos != new_pos:
            moved = True
            if new_pos != last_printed_pos:
                print(f"Update {i+1}: position ({new_pos[0]}, {new_pos[1]})")
                last_printed_pos = new_pos
    
    print("\n" + "=" * 70)
    
    if moved:
        final_dx = abs(player.rect.centerx - enemy.rect.centerx)
        final_dy = abs(player.rect.centery - enemy.rect.centery)
        
        distance_reduced = (final_dx < dx) or (final_dy < dy)
        
        print(f"Final distances: dx={final_dx}, dy={final_dy}")
        
        if distance_reduced:
            print("✓ PASS: Enemy moved and reduced distance to player")
            return True
        else:
            print("✗ FAIL: Enemy moved but didn't reduce distance")
            return False
    else:
        print("✗ FAIL: Enemy got STUCK - this demonstrates the bug!")
        print("  The enemy prioritized vertical movement (dy > dx)")
        print("  Vertical movement was blocked by wall")
        print("  Enemy didn't try horizontal movement as fallback")
        return False


if __name__ == '__main__':
    success = test_vertical_movement_blocked_should_try_horizontal()
    
    print("\n" + "=" * 70)
    if success:
        print("No bug detected in this scenario")
    else:
        print("BUG CONFIRMED: Enemy stops when vertical movement is blocked")
        print("even though horizontal movement would reduce distance to player")
