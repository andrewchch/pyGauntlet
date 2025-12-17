"""
Test script to verify the health system implementation
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from player import Player
from enemy import Enemy
from constants import TILE_SIZE

def test_health_system():
    """Test that the health system works correctly"""
    print("Testing Health System")
    print("=" * 50)
    
    pygame.init()
    pygame.display.set_mode((800, 600))  # Initialize display mode
    
    # Test 1: Player initial health
    print("\nTest 1: Player initial health...")
    player = Player(100, 100)
    assert player.health == 1000, f"Expected 1000, got {player.health}"
    print(f"✓ Player starts with {player.health} health")
    
    # Test 2: Enemy has damage property
    print("\nTest 2: Enemy damage property...")
    enemy = Enemy(200, 200)
    assert hasattr(enemy, 'damage'), "Enemy should have damage property"
    assert enemy.damage == 10, f"Expected 10, got {enemy.damage}"
    print(f"✓ Enemy has damage property set to {enemy.damage}")
    
    # Test 3: Player takes damage
    print("\nTest 3: Player takes damage...")
    initial_health = player.health
    player.take_damage(enemy.damage)
    expected_health = initial_health - enemy.damage
    assert player.health == expected_health, f"Expected {expected_health}, got {player.health}"
    print(f"✓ Player health reduced from {initial_health} to {player.health}")
    
    # Test 4: Multiple damage hits
    print("\nTest 4: Multiple damage hits...")
    for i in range(5):
        player.take_damage(enemy.damage)
    expected_health = 1000 - (6 * 10)  # Initial damage + 5 more
    assert player.health == expected_health, f"Expected {expected_health}, got {player.health}"
    print(f"✓ After 6 hits, player health is {player.health}")
    
    # Test 5: Health doesn't go below zero
    print("\nTest 5: Health doesn't go below zero...")
    player2 = Player(300, 300)
    for i in range(150):  # More than enough to kill the player
        player2.take_damage(enemy.damage)
    assert player2.health == 0, f"Expected 0, got {player2.health}"
    print(f"✓ Player health correctly capped at {player2.health}")
    
    # Test 6: Exact death scenario
    print("\nTest 6: Exact death at zero health...")
    player3 = Player(400, 400)
    # Reduce health to exactly 0
    for i in range(100):  # 100 hits * 10 damage = 1000
        player3.take_damage(enemy.damage)
    assert player3.health == 0, f"Expected 0, got {player3.health}"
    print(f"✓ Player health reaches exactly {player3.health} after 100 hits")
    
    print("\n" + "=" * 50)
    print("All health system tests passed! ✓")
    print("=" * 50)
    
    pygame.quit()

if __name__ == "__main__":
    test_health_system()
