"""
Player character class
"""
import pygame
from constants import *

class Player(pygame.sprite.Sprite):
    """Warrior character controlled by the player"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 4, TILE_SIZE - 4))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = PLAYER_SPEED
        self.last_direction = (0, -1)  # Up by default
        
    def update(self, keys, walls):
        """Update player position based on input"""
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT]:
            dx = -self.speed
            self.last_direction = (-1, 0)
        elif keys[pygame.K_RIGHT]:
            dx = self.speed
            self.last_direction = (1, 0)
        
        if keys[pygame.K_UP]:
            dy = -self.speed
            self.last_direction = (0, -1)
        elif keys[pygame.K_DOWN]:
            dy = self.speed
            self.last_direction = (0, 1)
        
        # Try horizontal movement
        if dx != 0:
            self.rect.x += dx
            if self.check_collision(walls):
                self.rect.x -= dx
        
        # Try vertical movement
        if dy != 0:
            self.rect.y += dy
            if self.check_collision(walls):
                self.rect.y -= dy
    
    def check_collision(self, walls):
        """Check if player collides with any wall"""
        return pygame.sprite.spritecollideany(self, walls) is not None
    
    def shoot(self):
        """Create and return a projectile"""
        from projectile import Projectile
        return Projectile(
            self.rect.centerx,
            self.rect.centery,
            self.last_direction
        )
