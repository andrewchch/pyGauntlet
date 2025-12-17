"""
Menu system for pyGauntlet
"""
import pygame
from constants import *

class Menu:
    """Game menu for start and pause screens"""
    
    def __init__(self, screen):
        self.screen = screen
        self.font_title = pygame.font.Font(None, 72)
        self.font_option = pygame.font.Font(None, 48)
        self.selected_index = 0
        
    def draw(self, is_paused=False, is_game_over=False):
        """Draw the menu"""
        # Semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        # Title
        if is_game_over:
            title_text = "Game Over!"
            title_color = RED
        else:
            title_text = "pyGauntlet"
            title_color = YELLOW
        
        title_surface = self.font_title.render(title_text, True, title_color)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
        self.screen.blit(title_surface, title_rect)
        
        # Menu option
        if is_paused:
            option_text = "Resume"
        else:
            option_text = "Play"
        
        option_color = GREEN if self.selected_index == 0 else WHITE
        option_surface = self.font_option.render(option_text, True, option_color)
        option_rect = option_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.screen.blit(option_surface, option_rect)
        
    def handle_input(self, event):
        """Handle menu input and return True if selection was made"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                return True
        return False
