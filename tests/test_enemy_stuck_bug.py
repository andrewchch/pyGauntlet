"""
More precise test to demonstrate the diagonal blocking bug
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from enemy import Enemy
from player import Player
from wall import Wall
from game_map import GameMap
from constants import TILE_SIZE

def test_enemy_hits_wall_should_move_sideways():
    """
    The critical test: Enemy trying to move diagonally hits a wall
    and should switch to moving along the wall
    
    Layout (@ = enemy starting position very close to wall):
        P . . .
        . . . .
        W W W W   <- solid horizontal wall
        . @ . .   <- enemy just below wall, diagonal to player
    
    Enemy should try to move up (blocked by wall), then move left toward player
    """
    print("Critical Test: Enemy Should Move Sideways When Vertical Is Blocked")
    print("=" * 70)
    
    pygame.init()
    pygame.display.set_mode((1, 1))
    
    # Player at top-left
    player = Player(TILE_SIZE, TILE_SIZE)
    
    # Enemy positioned just below a wall at position where:
    # - it wants to move diagonally up-left
    # - but wall blocks upward movement
    # - so it should move left instead
    enemy_start_x = 3 * TILE_SIZE
    enemy_start_y = 3 * TILE_SIZE - 2  # Very close to the wall tile above
    enemy = Enemy(enemy_start_x, enemy_start_y)
    
    walls = pygame.sprite.Group()
    # Horizontal wall at y = 2*TILE_SIZE (Wall class multiplies by TILE_SIZE)
    for i in range(5):
        wall = Wall(i, 2)
        walls.add(wall)
    
    game_map = GameMap()
    
    print(f"Player at:     ({player.rect.x}, {player.rect.y})")
    print(f"Enemy at:      ({enemy.rect.x}, {enemy.rect.y})")
    print(f"Wall line at:  y={2 * TILE_SIZE}")
    print(f"Enemy bottom:  {enemy.rect.bottom}")
    print(f"Wall top:      {2 * TILE_SIZE}")
    
    # Calculate which direction enemy should prefer
    dx = abs(player.rect.centerx - enemy.rect.centerx)
    dy = abs(player.rect.centery - enemy.rect.centery)
    print(f"\nDistances to player: dx={dx}, dy={dy}")
    
    if dy > dx:
        print("Enemy should primarily move vertically (UP)")
    else:
        print("Enemy should primarily move horizontally (LEFT)")
    
    print("\nRunning updates:")
    print("-" * 70)
    
    moved_left = False
    moved_up = False
    stuck_count = 0
    
    for i in range(20):
        old_pos = (enemy.rect.x, enemy.rect.y)
        enemy.update(player, walls, game_map)
        new_pos = (enemy.rect.x, enemy.rect.y)
        
        if old_pos == new_pos:
            stuck_count += 1
            if stuck_count >= 3:
                print(f"Update {i+1}: STUCK - no movement for {stuck_count} consecutive updates!")
                break
        else:
            stuck_count = 0
            move_x = new_pos[0] - old_pos[0]
            move_y = new_pos[1] - old_pos[1]
            
            direction = []
            if move_x < 0:
                direction.append("LEFT")
                moved_left = True
            elif move_x > 0:
                direction.append("RIGHT")
            if move_y < 0:
                direction.append("UP")
                moved_up = True
            elif move_y > 0:
                direction.append("DOWN")
            
            print(f"Update {i+1}: moved {'+'.join(direction):10s} by ({move_x:3d}, {move_y:3d}) to ({new_pos[0]:3d}, {new_pos[1]:3d})")
    
    print("\n" + "=" * 70)
    print("RESULTS:")
    
    # Check if enemy ever hit the wall
    if enemy.rect.top <= 2 * TILE_SIZE:
        print("✓ Enemy reached the wall level")
    
    if moved_left and moved_up:
        print("✓ PASS: Enemy moved both UP and LEFT (navigating around obstacles)")
        return True
    elif moved_up and not moved_left:
        print("✗ FAIL: Enemy only moved UP - didn't try moving LEFT when blocked")
        return False  
    elif moved_left and not moved_up:
        print("⚠ Enemy only moved LEFT - might not be optimal pathfinding")
        return True
    elif stuck_count >= 3:
        print("✗ FAIL: Enemy got STUCK - this is the bug!")
        return False
    else:
        print("? UNCLEAR: Enemy behavior unclear")
        return False


if __name__ == '__main__':
    success = test_enemy_hits_wall_should_move_sideways()
    
    print("\n" + "=" * 70)
    if success:
        print("TEST PASSED")
    else:
        print("TEST FAILED - Bug exists: enemies stop when diagonal movement is blocked")
