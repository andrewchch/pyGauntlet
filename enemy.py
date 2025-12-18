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
        
        # Determine primary and alternate directions
        if abs(dx) > abs(dy):
            # Prioritize horizontal movement
            primary_is_horizontal = True
            if dx > 0:
                move_x_primary = min(self.speed, dx)
            else:
                move_x_primary = max(-self.speed, dx)
            if dy > 0:
                move_y_alternate = min(self.speed, dy)
            else:
                move_y_alternate = max(-self.speed, dy)
        else:
            # Prioritize vertical movement
            primary_is_horizontal = False
            if dy > 0:
                move_y_primary = min(self.speed, dy)
            else:
                move_y_primary = max(-self.speed, dy)
            if dx > 0:
                move_x_alternate = min(self.speed, dx)
            else:
                move_x_alternate = max(-self.speed, dx)
        
        # Try to move
        old_x, old_y = self.rect.x, self.rect.y
        
        if primary_is_horizontal:
            # Try horizontal movement first
            self.rect.x += move_x_primary
            if self.check_collision(walls):
                # Horizontal blocked, revert and try vertical
                self.rect.x = old_x
                if move_y_alternate != 0:
                    self.rect.y += move_y_alternate
                    if self.check_collision(walls):
                        self.rect.y = old_y
        else:
            # Try vertical movement first
            self.rect.y += move_y_primary
            if self.check_collision(walls):
                # Vertical blocked, revert and try horizontal
                self.rect.y = old_y
                if move_x_alternate != 0:
                    self.rect.x += move_x_alternate
                    if self.check_collision(walls):
                        self.rect.x = old_x
    
    def check_collision(self, walls):
        """Check if enemy collides with any wall"""
        return pygame.sprite.spritecollideany(self, walls) is not None
