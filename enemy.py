"""
Enemy class with pathfinding AI
"""
import pygame
from constants import *

class Enemy(pygame.sprite.Sprite):
    """An enemy that chases the player"""
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((TILE_SIZE - 4, TILE_SIZE - 4))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = ENEMY_SPEED
        self.damage = 10  # Damage dealt to player on collision
        
    def update(self, player, walls, game_map):
        """Update enemy position to move toward player"""
        # Calculate direction to player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        
        # Normalize and apply speed
        if abs(dx) > abs(dy):
            # Move horizontally
            if dx > 0:
                move_x = min(self.speed, dx)
            else:
                move_x = max(-self.speed, dx)
            move_y = 0
        else:
            # Move vertically
            if dy > 0:
                move_y = min(self.speed, dy)
            else:
                move_y = max(-self.speed, dy)
            move_x = 0
        
        # Try to move
        old_x, old_y = self.rect.x, self.rect.y
        
        # Try horizontal movement
        if move_x != 0:
            self.rect.x += move_x
            if self.check_collision(walls):
                self.rect.x = old_x
                # If blocked, try vertical
                if move_y == 0:
                    if dy > 0:
                        move_y = self.speed
                    else:
                        move_y = -self.speed
        
        # Try vertical movement
        if move_y != 0:
            self.rect.y += move_y
            if self.check_collision(walls):
                self.rect.y = old_y
    
    def check_collision(self, walls):
        """Check if enemy collides with any wall"""
        return pygame.sprite.spritecollideany(self, walls) is not None
