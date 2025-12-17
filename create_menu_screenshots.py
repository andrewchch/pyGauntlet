"""
Create screenshots of menu states for verification
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from game import Game
from constants import *

def create_menu_screenshots():
    """Create screenshots of different menu states"""
    print("Creating menu screenshots...")
    
    pygame.init()
    game = Game()
    
    # Screenshot 1: Initial menu (STATE_MENU with "Play")
    print("Creating screenshot of initial menu...")
    game.state = STATE_MENU
    game.draw()
    pygame.image.save(game.screen, "/home/runner/work/pyGauntlet/pyGauntlet/screenshot_menu_initial.png")
    print("✓ Saved: screenshot_menu_initial.png")
    
    # Screenshot 2: Game playing
    print("Creating screenshot of gameplay...")
    game.state = STATE_PLAYING
    # Simulate a few frames to spawn enemies
    for i in range(100):
        current_time = pygame.time.get_ticks()
        game.update(current_time)
    game.draw()
    pygame.image.save(game.screen, "/home/runner/work/pyGauntlet/pyGauntlet/screenshot_gameplay.png")
    print("✓ Saved: screenshot_gameplay.png")
    
    # Screenshot 3: Paused menu (STATE_PAUSED with "Resume")
    print("Creating screenshot of pause menu...")
    game.state = STATE_PAUSED
    game.draw()
    pygame.image.save(game.screen, "/home/runner/work/pyGauntlet/pyGauntlet/screenshot_menu_paused.png")
    print("✓ Saved: screenshot_menu_paused.png")
    
    print("\nAll screenshots created successfully!")
    pygame.quit()

if __name__ == "__main__":
    create_menu_screenshots()
