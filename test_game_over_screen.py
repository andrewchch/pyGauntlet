"""
Test game over screen functionality
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from game import Game
from enemy import Enemy
from constants import STATE_GAME_OVER, STATE_PLAYING

def test_game_over_screen():
    """Test game over screen appears and can restart"""
    print("Testing Game Over Screen")
    print("=" * 50)
    
    pygame.init()
    game = Game()
    
    # Start the game
    game.state = STATE_PLAYING
    print(f"Game state: PLAYING")
    print(f"Initial player health: {game.player.health}")
    
    # Set health to 10 and trigger game over
    game.player.health = 10
    enemy = Enemy(game.player.rect.x, game.player.rect.y)
    game.enemies.add(enemy)
    
    # Run update to trigger collision
    current_time = pygame.time.get_ticks()
    game.update(current_time)
    
    print(f"Player health after collision: {game.player.health}")
    print(f"Game state after death: {game.state}")
    
    # Verify game over state
    if game.state == STATE_GAME_OVER:
        print("✓ Game correctly transitioned to GAME_OVER state")
    else:
        print(f"✗ Expected STATE_GAME_OVER (3), got {game.state}")
        return False
    
    # Test reset functionality
    print("\nTesting game reset...")
    game.reset_game()
    print(f"Player health after reset: {game.player.health}")
    print(f"Enemies after reset: {len(game.enemies)}")
    print(f"Projectiles after reset: {len(game.projectiles)}")
    
    if game.player.health == 1000:
        print("✓ Player health reset correctly")
    else:
        print(f"✗ Expected health 1000, got {game.player.health}")
        return False
    
    if len(game.enemies) == 0:
        print("✓ Enemies cleared correctly")
    else:
        print(f"✗ Expected 0 enemies, got {len(game.enemies)}")
        return False
    
    print("\n" + "=" * 50)
    print("Game Over Screen tests passed! ✓")
    print("=" * 50)
    
    pygame.quit()
    return True

if __name__ == "__main__":
    success = test_game_over_screen()
    exit(0 if success else 1)
