"""
Debug version of the test to see what's happening
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from enemy import Enemy
from player import Player
from wall import Wall
from game_map import GameMap
from constants import TILE_SIZE

def test_with_debug():
    pygame.init()
    pygame.display.set_mode((1, 1))
    
    player = Player(TILE_SIZE, TILE_SIZE)  
    enemy = Enemy(TILE_SIZE + 10, 2 * TILE_SIZE + TILE_SIZE - 1)
    
    walls = pygame.sprite.Group()
    for i in range(5):
        wall = Wall(i, 2)
        walls.add(wall)
    
    game_map = GameMap()
    
    print(f"Player: ({player.rect.x}, {player.rect.y}) to ({player.rect.right}, {player.rect.bottom})")
    print(f"Enemy:  ({enemy.rect.x}, {enemy.rect.y}) to ({enemy.rect.right}, {enemy.rect.bottom})")
    
    print("\nWalls:")
    for wall in walls:
        print(f"  Wall: ({wall.rect.x}, {wall.rect.y}) to ({wall.rect.right}, {wall.rect.bottom})")
    
    dx = player.rect.centerx - enemy.rect.centerx
    dy = player.rect.centery - enemy.rect.centery
    print(f"\ndx={dx}, dy={dy}")
    print(f"abs(dx)={abs(dx)}, abs(dy)={abs(dy)}")
    print(f"Primary direction: {'HORIZONTAL' if abs(dx) > abs(dy) else 'VERTICAL'}")
    
    # Check if enemy collides with wall initially
    if enemy.check_collision(walls):
        print("WARNING: Enemy starts in collision with wall!")
    
    print("\nTrying one update...")
    old_pos = (enemy.rect.x, enemy.rect.y)
    enemy.update(player, walls, game_map)
    new_pos = (enemy.rect.x, enemy.rect.y)
    
    print(f"Enemy moved from {old_pos} to {new_pos}")
    if old_pos == new_pos:
        print("Enemy did not move")
        
        # Manually check what happens with movements
        print("\nManual movement test:")
        test_enemy = Enemy(TILE_SIZE + 10, 2 * TILE_SIZE + TILE_SIZE - 1)
        
        print(f"Initial enemy pos: ({test_enemy.rect.x}, {test_enemy.rect.y})")
        
        # Try moving up
        test_enemy.rect.y -= 2
        print(f"After moving up by 2: ({test_enemy.rect.x}, {test_enemy.rect.y})")
        if test_enemy.check_collision(walls):
            print("  -> Collision detected!")
            test_enemy.rect.y += 2
        else:
            print("  -> No collision")
        
        # Try moving left  
        test_enemy.rect.x -= 2
        print(f"After moving left by 2: ({test_enemy.rect.x}, {test_enemy.rect.y})")
        if test_enemy.check_collision(walls):
            print("  -> Collision detected!")
            test_enemy.rect.x += 2
        else:
            print("  -> No collision")

if __name__ == '__main__':
    test_with_debug()
