"""Debug the first test scenario"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from enemy import Enemy
from player import Player
from wall import Wall
from game_map import GameMap
from constants import TILE_SIZE

pygame.init()
pygame.display.set_mode((1, 1))

player = Player(0, 0)
enemy = Enemy(2 * TILE_SIZE, 2 * TILE_SIZE)

walls = pygame.sprite.Group()
wall1 = Wall(1, 1)
wall2 = Wall(2, 1)
wall3 = Wall(1, 2)
walls.add(wall1, wall2, wall3)

print(f"TILE_SIZE: {TILE_SIZE}")
print(f"\nPlayer rect: ({player.rect.x}, {player.rect.y}) to ({player.rect.right}, {player.rect.bottom})")
print(f"Enemy rect:  ({enemy.rect.x}, {enemy.rect.y}) to ({enemy.rect.right}, {enemy.rect.bottom})")
print(f"\nWalls:")
for i, wall in enumerate(walls, 1):
    print(f"  Wall{i}: ({wall.rect.x}, {wall.rect.y}) to ({wall.rect.right}, {wall.rect.bottom})")

print(f"\nEnemy initial collision check: {enemy.check_collision(walls)}")

dx = player.rect.centerx - enemy.rect.centerx
dy = player.rect.centery - enemy.rect.centery
print(f"\ndx={dx}, dy={dy}")
print(f"Primary direction: {'HORIZONTAL (left)' if abs(dx) > abs(dy) else 'VERTICAL (up)'}")

# Try movements manually
print("\nManual movement test:")
test_enemy = Enemy(2 * TILE_SIZE, 2 * TILE_SIZE)
print(f"Initial: ({test_enemy.rect.x}, {test_enemy.rect.y})")

# Try left
test_enemy.rect.x -= 2
print(f"After left by 2: ({test_enemy.rect.x}, {test_enemy.rect.y}), collision: {test_enemy.check_collision(walls)}")
test_enemy.rect.x += 2

# Try up
test_enemy.rect.y -= 2
print(f"After up by 2: ({test_enemy.rect.x}, {test_enemy.rect.y}), collision: {test_enemy.check_collision(walls)}")
test_enemy.rect.y += 2

# Try right
test_enemy.rect.x += 2
print(f"After right by 2: ({test_enemy.rect.x}, {test_enemy.rect.y}), collision: {test_enemy.check_collision(walls)}")
test_enemy.rect.x -= 2

# Try down  
test_enemy.rect.y += 2
print(f"After down by 2: ({test_enemy.rect.x}, {test_enemy.rect.y}), collision: {test_enemy.check_collision(walls)}")
