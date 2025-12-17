"""
Projectile class for player attacks
"""
import pygame
from constants import *

class Projectile(pygame.sprite.Sprite):
    """A projectile fired by the player"""
    
    def __init__(self, x, y, direction):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.speed = PROJECTILE_SPEED
        self.hit_generators = set()  # Track which generators have been hit
        
    def update(self, walls, enemies, generators=None):
        """Update projectile position"""
        # Move in direction
        self.rect.x += self.direction[0] * self.speed
        self.rect.y += self.direction[1] * self.speed
        
        # Check if hit wall
        if pygame.sprite.spritecollideany(self, walls):
            self.kill()
            return
        
        # Check if hit generator (damages generator but doesn't destroy projectile)
        if generators:
            hit_generators = pygame.sprite.spritecollide(self, generators, False)
            for generator in hit_generators:
                # Only damage each generator once per projectile
                if generator not in self.hit_generators:
                    generator.take_damage()
                    self.hit_generators.add(generator)
        
        # Check if hit enemy
        hit_enemies = pygame.sprite.spritecollide(self, enemies, True)
        if hit_enemies:
            self.kill()
            return
        
        # Check if out of bounds
        if (self.rect.x < 0 or self.rect.x > MAP_WIDTH * TILE_SIZE or
            self.rect.y < 0 or self.rect.y > MAP_HEIGHT * TILE_SIZE):
            self.kill()
