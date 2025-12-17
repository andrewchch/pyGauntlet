"""
Wall tile class
"""
import pygame
from constants import *

class Wall(pygame.sprite.Sprite):
    """A wall tile that blocks movement"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(GRAY)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
