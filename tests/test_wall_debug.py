"""Quick debug for wall positioning"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from wall import Wall
from constants import TILE_SIZE

pygame.init()
pygame.display.set_mode((1, 1))

print(f"TILE_SIZE = {TILE_SIZE}")

# Test old vs new wall constructor usage
print("\nOld usage: Wall(1 * TILE_SIZE, 1 * TILE_SIZE)")
wall_old_style = Wall(1 * TILE_SIZE, 1 * TILE_SIZE)
print(f"  Wall position: ({wall_old_style.rect.x}, {wall_old_style.rect.y})")

print("\nNew usage: Wall(1, 1)")
wall_new_style = Wall(1, 1)
print(f"  Wall position: ({wall_new_style.rect.x}, {wall_new_style.rect.y})")

print("\nExpected position for tile (1, 1): (32, 32)")
