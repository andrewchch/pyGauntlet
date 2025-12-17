"""
Enemy generator/spawner class
"""
import pygame
from constants import *
from enemy import Enemy

class Generator(pygame.sprite.Sprite):
    """A generator that spawns enemies"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE
        self.last_spawn_time = 0
        self.spawn_interval = SPAWN_INTERVAL
        
    def update(self, current_time, enemies):
        """Spawn enemies at intervals"""
        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.last_spawn_time = current_time
            # Spawn enemy at generator location
            enemy = Enemy(self.rect.x, self.rect.y)
            enemies.add(enemy)
