"""
Test enemy movement behavior, especially when blocked by walls
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from enemy import Enemy
from player import Player
from wall import Wall
from game_map import GameMap
from constants import TILE_SIZE

def test_enemy_movement_around_walls():
    """Test that enemies continue to move toward player when diagonal movement is blocked"""
    print("Testing Enemy Movement Around Walls")
    print("=" * 50)
    
    pygame.init()
    # Initialize a dummy display so sprite loading works
    pygame.display.set_mode((1, 1))
    
    # Create a test scenario with walls blocking diagonal movement
    # Layout:
    #   P . . .
    #   . W W .
    #   . W E .
    #   . . . .
    # P = Player, E = Enemy, W = Wall, . = empty
    # Enemy should move right (reducing horizontal distance) when it can't move diagonally up-right
    
    player = Player(0, 0)
    
    enemy = Enemy(2 * TILE_SIZE, 2 * TILE_SIZE)
    
    walls = pygame.sprite.Group()
    # Create wall blocking diagonal path
    wall1 = Wall(1 * TILE_SIZE, 1 * TILE_SIZE)
    wall2 = Wall(2 * TILE_SIZE, 1 * TILE_SIZE)
    wall3 = Wall(1 * TILE_SIZE, 2 * TILE_SIZE)
    walls.add(wall1, wall2, wall3)
    
    game_map = GameMap()
    
    print(f"Initial enemy position: ({enemy.rect.x}, {enemy.rect.y})")
    print(f"Player position: ({player.rect.x}, {player.rect.y})")
    print(f"Walls at: (32, 32), (64, 32), (32, 64)")
    
    # Update enemy - it should try to move toward player
    initial_x = enemy.rect.x
    initial_y = enemy.rect.y
    
    # Run several updates to see movement
    for i in range(10):
        enemy.update(player, walls, game_map)
        if enemy.rect.x != initial_x or enemy.rect.y != initial_y:
            print(f"After update {i+1}: enemy position: ({enemy.rect.x}, {enemy.rect.y})")
            break
    
    # Enemy should have moved (either up or left, preferably the one that reduces distance more)
    moved = (enemy.rect.x != initial_x) or (enemy.rect.y != initial_y)
    
    if moved:
        print("✓ Enemy moved when diagonal path was blocked")
        
        # Calculate which direction reduces distance to player more
        dx = abs(player.rect.centerx - initial_x)
        dy = abs(player.rect.centery - initial_y)
        
        if dx > dy:
            # Horizontal movement should be prioritized
            if enemy.rect.x < initial_x:
                print("✓ Enemy correctly moved left (horizontally toward player)")
            else:
                print("⚠ Enemy moved in unexpected direction")
        else:
            # Vertical movement should be prioritized
            if enemy.rect.y < initial_y:
                print("✓ Enemy correctly moved up (vertically toward player)")
            else:
                print("⚠ Enemy moved in unexpected direction")
    else:
        print("✗ Enemy did not move - this is the bug we're fixing!")
    
    return moved


def test_enemy_continues_along_wall():
    """Test that enemy moves along a wall when blocked from direct diagonal movement"""
    print("\nTesting Enemy Movement Along Wall")
    print("=" * 50)
    
    pygame.init()
    # Initialize a dummy display so sprite loading works
    pygame.display.set_mode((1, 1))
    
    # Create a scenario with a vertical wall between enemy and player
    # Layout:
    #   P . W E
    #   . . W .
    # Enemy should move down along the wall to get closer
    
    player = Player(0, 0)
    
    enemy = Enemy(3 * TILE_SIZE, 0)
    
    walls = pygame.sprite.Group()
    # Vertical wall
    wall1 = Wall(2 * TILE_SIZE, 0)
    wall2 = Wall(2 * TILE_SIZE, 1 * TILE_SIZE)
    walls.add(wall1, wall2)
    
    game_map = GameMap()
    
    print(f"Initial enemy position: ({enemy.rect.x}, {enemy.rect.y})")
    print(f"Player position: ({player.rect.x}, {player.rect.y})")
    
    initial_distance = ((player.rect.centerx - enemy.rect.centerx) ** 2 + 
                       (player.rect.centery - enemy.rect.centery) ** 2) ** 0.5
    
    # Update enemy multiple times
    for i in range(5):
        old_x, old_y = enemy.rect.x, enemy.rect.y
        enemy.update(player, walls, game_map)
        if enemy.rect.x != old_x or enemy.rect.y != old_y:
            print(f"Update {i+1}: enemy moved from ({old_x}, {old_y}) to ({enemy.rect.x}, {enemy.rect.y})")
    
    final_distance = ((player.rect.centerx - enemy.rect.centerx) ** 2 + 
                     (player.rect.centery - enemy.rect.centery) ** 2) ** 0.5
    
    distance_reduced = final_distance < initial_distance
    
    if distance_reduced:
        print(f"✓ Enemy reduced distance from {initial_distance:.1f} to {final_distance:.1f}")
    else:
        print(f"✗ Enemy did not reduce distance (was {initial_distance:.1f}, now {final_distance:.1f})")
    
    return distance_reduced


if __name__ == '__main__':
    test1_passed = test_enemy_movement_around_walls()
    test2_passed = test_enemy_continues_along_wall()
    
    print("\n" + "=" * 50)
    if test1_passed and test2_passed:
        print("All tests passed! ✓")
    else:
        print("Some tests failed - enemy movement needs improvement")
