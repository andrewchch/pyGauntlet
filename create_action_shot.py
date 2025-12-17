"""
Create an action-packed screenshot showing game features
"""
import pygame
import os

os.environ['SDL_VIDEODRIVER'] = 'dummy'
os.environ['SDL_AUDIODRIVER'] = 'dummy'

from game import Game
from constants import *

def create_action_screenshot():
    """Create a screenshot showing various game elements"""
    pygame.init()
    
    # Create game instance
    game = Game()
    
    # Position player in middle of map
    game.player.rect.x = 600
    game.player.rect.y = 500
    
    # Run game for a while to spawn lots of enemies
    for i in range(500):
        current_time = i * 16  # Simulate 60 FPS (16ms per frame)
        
        # Update generators
        for gen in game.game_map.generators:
            gen.update(current_time, game.enemies)
        
        # Update enemies to move toward player
        for enemy in game.enemies:
            enemy.update(game.player, game.game_map.walls, game.game_map)
        
        # Add some projectiles in different directions
        if i % 80 == 0 and len(game.projectiles) < 5:
            game.player.last_direction = [(1,0), (-1,0), (0,1), (0,-1)][i % 4]
            proj = game.player.shoot()
            game.projectiles.add(proj)
        
        # Update projectiles
        for projectile in game.projectiles:
            projectile.update(game.game_map.walls, game.enemies, game.game_map.generators)
    
    # Update camera to center on player
    game.camera.update(game.player)
    
    # Draw the game state
    game.draw()
    
    # Save screenshot
    pygame.image.save(game.screen, '/tmp/pygauntlet_action.png')
    
    print("Action screenshot created!")
    print(f"Game state:")
    print(f"  - Enemies: {len(game.enemies)}")
    print(f"  - Projectiles: {len(game.projectiles)}")
    print(f"  - Walls: {len(game.game_map.walls)}")
    print(f"  - Generators: {len(game.game_map.generators)}")
    
    pygame.quit()
    return '/tmp/pygauntlet_action.png'

if __name__ == "__main__":
    screenshot_path = create_action_screenshot()
    print(f"\nScreenshot saved to: {screenshot_path}")
