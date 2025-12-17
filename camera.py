"""
Camera class for scrolling the game view
"""
import pygame
from constants import *

class Camera:
    """Handles viewport scrolling to follow the player"""
    
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        
    def apply(self, entity):
        """Apply camera offset to an entity"""
        return entity.rect.move(-self.camera.x, -self.camera.y)
    
    def update(self, target):
        """Update camera position to follow target"""
        # Center camera on target
        x = target.rect.centerx - SCREEN_WIDTH // 2
        y = target.rect.centery - SCREEN_HEIGHT // 2
        
        # Limit scrolling to map boundaries
        x = max(0, min(x, self.width - SCREEN_WIDTH))
        y = max(0, min(y, self.height - SCREEN_HEIGHT))
        
        self.camera = pygame.Rect(x, y, SCREEN_WIDTH, SCREEN_HEIGHT)
