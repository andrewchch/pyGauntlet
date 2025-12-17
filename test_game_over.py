"""
Test game over at exactly zero health
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from game import Game
from enemy import Enemy

def test_game_over():
    """Test game over when health reaches exactly 0"""
    print("Testing Game Over Condition")
    print("=" * 50)
    
    pygame.init()
    game = Game()
    
    # Set health to exactly 10, so next collision brings it to 0
    game.player.health = 10
    print(f"Set player health to: {game.player.health}")
    
    # Add enemy at player position to guarantee collision
    enemy = Enemy(game.player.rect.x, game.player.rect.y)
    game.enemies.add(enemy)
    
    print(f"Game running before update: {game.running}")
    print(f"Triggering collision (enemy damage: {enemy.damage})...")
    
    # Trigger collision
    game.update(pygame.time.get_ticks())
    
    print(f"Player health after collision: {game.player.health}")
    print(f"Game running after update: {game.running}")
    
    if game.player.health == 0 and not game.running:
        print("\n✓ SUCCESS: Game ended when health reached 0")
    else:
        print(f"\n✗ FAILURE: Game should have ended")
        print(f"  Health: {game.player.health}, Running: {game.running}")
    
    pygame.quit()

if __name__ == "__main__":
    test_game_over()
