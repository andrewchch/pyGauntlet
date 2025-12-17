"""
Create a screenshot of the game with animated character
"""
import pygame
import sys
from game import Game
from constants import *

def create_game_screenshot():
    """Create a screenshot showing the animated character in the game"""
    pygame.init()
    game = Game()
    
    # Set game state to playing
    game.state = STATE_PLAYING
    
    # Update a few times to get a nice animation frame
    class KeyState:
        def __init__(self, key=None):
            self.key = key
        def __getitem__(self, k):
            return k == self.key
    
    # Move down a bit to show walking animation
    for i in range(10):
        keys = KeyState(pygame.K_DOWN)
        game.player.update(keys, game.game_map.walls)
    
    # Update camera
    game.camera.update(game.player)
    
    # Draw the game
    game.screen.fill(BLACK)
    
    # Draw walls
    for wall in game.game_map.walls:
        game.screen.blit(wall.image, game.camera.apply(wall))
    
    # Draw generators
    for generator in game.game_map.generators:
        game.screen.blit(generator.image, game.camera.apply(generator))
    
    # Draw player with animated sprite
    game.screen.blit(game.player.image, game.camera.apply(game.player))
    
    # Draw UI
    game.draw_ui()
    
    # Add annotation
    font = pygame.font.Font(None, 36)
    text = font.render("Animated Character Sprite (LPC Format)", True, YELLOW)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
    
    # Draw background for text
    bg_rect = text_rect.inflate(20, 10)
    pygame.draw.rect(game.screen, BLACK, bg_rect)
    pygame.draw.rect(game.screen, YELLOW, bg_rect, 2)
    
    game.screen.blit(text, text_rect)
    
    # Save screenshot
    pygame.display.flip()
    screenshot_path = "game_with_animated_character.png"
    pygame.image.save(game.screen, screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    
    pygame.quit()
    return screenshot_path

if __name__ == "__main__":
    create_game_screenshot()
