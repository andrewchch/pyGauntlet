"""
Demo script to create a screenshot of the game
"""
import pygame
import os

# Set up for headless rendering
os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

from game import Game
from constants import *

def create_demo_screenshot():
    """Create a demonstration screenshot"""
    pygame.init()
    
    # Create game instance
    game = Game()
    
    # Move player to a visible location
    game.player.rect.x = 500
    game.player.rect.y = 400
    
    # Simulate game for a bit to spawn enemies
    for i in range(300):
        current_time = i * 16  # Simulate 60 FPS
        
        # Update generators every spawn interval
        for gen in game.game_map.generators:
            gen.update(current_time, game.enemies)
        
        # Update enemies
        for enemy in game.enemies:
            enemy.update(game.player, game.game_map.walls, game.game_map)
        
        # Every 100 frames, add a projectile
        if i % 100 == 0 and i > 0:
            proj = game.player.shoot()
            game.projectiles.add(proj)
    
    # Update camera to center on player
    game.camera.update(game.player)
    
    # Draw the game state
    game.draw()
    
    # Save screenshot
    pygame.image.save(game.screen, '/tmp/pygauntlet_demo.png')
    
    print(f"Screenshot saved!")
    print(f"Game state:")
    print(f"  - Player position: ({game.player.rect.x}, {game.player.rect.y})")
    print(f"  - Enemies spawned: {len(game.enemies)}")
    print(f"  - Walls: {len(game.game_map.walls)}")
    print(f"  - Generators: {len(game.game_map.generators)}")
    print(f"  - Active projectiles: {len(game.projectiles)}")
    
    pygame.quit()
    return '/tmp/pygauntlet_demo.png'

if __name__ == "__main__":
    screenshot_path = create_demo_screenshot()
    print(f"\nScreenshot saved to: {screenshot_path}")
