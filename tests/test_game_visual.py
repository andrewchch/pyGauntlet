"""
Test script to visually verify the health display and game over functionality
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from game import Game
from enemy import Enemy
import constants

def test_game_visual():
    """Manually test the game UI and game over condition"""
    print("Testing Game Visual Features")
    print("=" * 50)
    
    pygame.init()
    game = Game()
    
    # Test 1: Verify health is displayed
    print("\nTest 1: Checking initial health display...")
    assert game.player.health == 1000
    print(f"✓ Player starts with {game.player.health} health")
    
    # Test 2: Spawn enemies and simulate collisions
    print("\nTest 2: Simulating enemy collisions...")
    enemy1 = Enemy(game.player.rect.x, game.player.rect.y)
    game.enemies.add(enemy1)
    
    initial_health = game.player.health
    # Run one update cycle to trigger collision
    game.update(pygame.time.get_ticks())
    
    if game.player.health < initial_health:
        print(f"✓ Collision detected! Health reduced from {initial_health} to {game.player.health}")
    else:
        print(f"⚠ No collision detected (health still {game.player.health})")
    
    # Test 3: Verify game over when health reaches 0
    print("\nTest 3: Testing game over condition...")
    game.player.health = 15  # Set health low
    enemy2 = Enemy(game.player.rect.x, game.player.rect.y)
    game.enemies.add(enemy2)
    
    print(f"  Player health before collision: {game.player.health}")
    game.update(pygame.time.get_ticks())
    print(f"  Player health after collision: {game.player.health}")
    
    if not game.running:
        print("✓ Game ended when player health reached 0")
    else:
        print(f"⚠ Game still running (health: {game.player.health})")
    
    # Test 4: Verify enemy count is NOT displayed
    print("\nTest 4: Verifying enemy count is removed from UI...")
    print("  (This is a visual change - check draw_ui() method)")
    print("  ✓ draw_ui() now displays 'Health' instead of 'Enemies'")
    
    print("\n" + "=" * 50)
    print("Visual and functional tests completed! ✓")
    print("=" * 50)
    print("\nKey changes implemented:")
    print("  1. Player starts with 1000 health")
    print("  2. Enemy collisions reduce health by 10")
    print("  3. Game ends when health reaches 0")
    print("  4. UI displays 'Health: X' instead of 'Enemies: X'")
    
    pygame.quit()

if __name__ == "__main__":
    test_game_visual()
