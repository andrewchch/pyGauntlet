"""
Test script to verify game components
"""
import pygame
from constants import *
from player import Player
from enemy import Enemy
from wall import Wall
from generator import Generator
from game_map import GameMap
from camera import Camera

def test_components():
    """Test that all components can be instantiated"""
    print("Testing pygame initialization...")
    pygame.init()
    
    print("Testing Player creation...")
    player = Player(100, 100)
    assert player.rect.x == 100
    assert player.rect.y == 100
    print("✓ Player created successfully")
    
    print("Testing Enemy creation...")
    enemy = Enemy(200, 200)
    assert enemy.rect.x == 200
    assert enemy.rect.y == 200
    print("✓ Enemy created successfully")
    
    print("Testing Wall creation...")
    wall = Wall(5, 5)
    assert wall.rect.x == 5 * TILE_SIZE
    assert wall.rect.y == 5 * TILE_SIZE
    print("✓ Wall created successfully")
    
    print("Testing Generator creation...")
    generator = Generator(10, 10)
    assert generator.rect.x == 10 * TILE_SIZE
    assert generator.rect.y == 10 * TILE_SIZE
    print("✓ Generator created successfully")
    
    print("Testing GameMap creation...")
    game_map = GameMap()
    assert len(game_map.walls) > 0
    assert len(game_map.generators) > 0
    print(f"✓ GameMap created with {len(game_map.walls)} walls and {len(game_map.generators)} generators")
    
    print("Testing Camera creation...")
    camera = Camera(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE)
    print("✓ Camera created successfully")
    
    print("Testing Player movement...")
    walls = pygame.sprite.Group()
    keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True, pygame.K_UP: False, pygame.K_DOWN: False}
    old_x = player.rect.x
    player.update(keys, walls)
    assert player.rect.x > old_x
    print("✓ Player movement works")
    
    print("Testing Player shooting...")
    projectile = player.shoot()
    assert projectile is not None
    print("✓ Player shooting works")
    
    print("\n" + "="*50)
    print("All component tests passed! ✓")
    print("="*50)
    
    pygame.quit()

if __name__ == "__main__":
    test_components()
