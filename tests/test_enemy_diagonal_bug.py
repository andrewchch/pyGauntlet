"""
Test to reproduce the specific bug where enemies stop when diagonal movement is blocked
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from enemy import Enemy
from player import Player
from wall import Wall
from game_map import GameMap
from constants import TILE_SIZE

def test_enemy_stops_at_diagonal_wall():
    """
    Reproduce the bug: enemy should continue moving when diagonal is blocked,
    but currently it stops.
    
    Layout (each character is one tile):
        P . . . .
        . . . . .
        . . W W W   <- horizontal wall
        . . E . .   <- enemy below wall trying to reach player
    
    The enemy wants to move diagonally up-left to reach the player.
    When it tries to move up, it will hit the wall.
    It should then try moving left (which reduces distance) but currently might stop.
    """
    print("Testing Diagonal Wall Bug")
    print("=" * 50)
    
    pygame.init()
    pygame.display.set_mode((1, 1))
    
    # Player at top-left
    player = Player(0, 0)
    
    # Enemy directly below a horizontal wall, diagonal to player
    enemy = Enemy(2 * TILE_SIZE, 3 * TILE_SIZE)
    
    walls = pygame.sprite.Group()
    # Create horizontal wall between enemy and player
    wall1 = Wall(2 * TILE_SIZE, 2 * TILE_SIZE)
    wall2 = Wall(3 * TILE_SIZE, 2 * TILE_SIZE)
    wall3 = Wall(4 * TILE_SIZE, 2 * TILE_SIZE)
    walls.add(wall1, wall2, wall3)
    
    game_map = GameMap()
    
    print(f"Player at: ({player.rect.x}, {player.rect.y})")
    print(f"Enemy at:  ({enemy.rect.x}, {enemy.rect.y})")
    print(f"Wall at:   y={2 * TILE_SIZE} (horizontal)")
    
    # Calculate initial distances
    dx_initial = abs(player.rect.centerx - enemy.rect.centerx)
    dy_initial = abs(player.rect.centery - enemy.rect.centery)
    print(f"Initial distances: dx={dx_initial}, dy={dy_initial}")
    
    # The enemy should primarily try to move vertically (dy > dx)
    # But when blocked, it should move horizontally
    
    movements = []
    for i in range(10):
        old_pos = (enemy.rect.x, enemy.rect.y)
        enemy.update(player, walls, game_map)
        new_pos = (enemy.rect.x, enemy.rect.y)
        
        if old_pos != new_pos:
            movement = (new_pos[0] - old_pos[0], new_pos[1] - old_pos[1])
            movements.append(movement)
            print(f"Update {i+1}: moved by {movement}, now at ({new_pos[0]}, {new_pos[1]})")
    
    if len(movements) == 0:
        print("✗ BUG CONFIRMED: Enemy did not move at all!")
        return False
    elif len(movements) < 5:
        print(f"⚠ Enemy only moved {len(movements)} times out of 10 updates - might be stuck")
        return False
    else:
        print(f"✓ Enemy moved {len(movements)} times - continuing toward player")
        
        # Check if enemy moved horizontally at some point (which it should when vertical is blocked)
        horizontal_moves = [m for m in movements if m[0] != 0]
        if horizontal_moves:
            print(f"✓ Enemy made horizontal movements: {horizontal_moves}")
            return True
        else:
            print("⚠ Enemy only made vertical movements - might not be navigating around wall optimally")
            return False


def test_enemy_blocked_by_corner():
    """
    Test enemy behavior when in a corner with walls blocking both diagonal directions
    
    Layout:
        P . . . .
        . . . . .
        . W W . .   <- walls forming an L-shape
        . W E . .   <- enemy in corner
        
    Enemy should move right or down (away from walls) if that reduces distance
    """
    print("\n\nTesting Corner Wall Scenario")
    print("=" * 50)
    
    pygame.init()
    pygame.display.set_mode((1, 1))
    
    player = Player(0, 0)
    enemy = Enemy(2 * TILE_SIZE, 3 * TILE_SIZE)
    
    walls = pygame.sprite.Group()
    # L-shaped walls
    wall1 = Wall(1 * TILE_SIZE, 2 * TILE_SIZE)
    wall2 = Wall(2 * TILE_SIZE, 2 * TILE_SIZE)
    wall3 = Wall(1 * TILE_SIZE, 3 * TILE_SIZE)
    walls.add(wall1, wall2, wall3)
    
    game_map = GameMap()
    
    print(f"Player at: ({player.rect.x}, {player.rect.y})")
    print(f"Enemy at:  ({enemy.rect.x}, {enemy.rect.y})")
    print(f"Walls forming L-shape to the left and above enemy")
    
    movements = []
    for i in range(10):
        old_pos = (enemy.rect.x, enemy.rect.y)
        enemy.update(player, walls, game_map)
        new_pos = (enemy.rect.x, enemy.rect.y)
        
        if old_pos != new_pos:
            movement = (new_pos[0] - old_pos[0], new_pos[1] - old_pos[1])
            movements.append(movement)
            print(f"Update {i+1}: moved by {movement}")
    
    if len(movements) == 0:
        print("✗ BUG: Enemy completely stuck in corner!")
        return False
    else:
        print(f"✓ Enemy moved {len(movements)} times")
        return True


if __name__ == '__main__':
    test1 = test_enemy_stops_at_diagonal_wall()
    test2 = test_enemy_blocked_by_corner()
    
    print("\n" + "=" * 50)
    if test1 and test2:
        print("All tests passed!")
    else:
        print("Bug detected - enemies stop when they should continue moving")
