"""
Player character class
"""
import pygame
import os
from constants import *
from entities.character import AnimatedCharacter

class Player(pygame.sprite.Sprite):
    """Warrior character controlled by the player"""
    
    def __init__(self, x, y):
        super().__init__()
        
        # Try to load animated sprite, fallback to colored square if not available
        sprite_path = os.path.join('resources', 'sprites', 'character-spritesheet.png')
        if os.path.exists(sprite_path):
            self.animated_char = AnimatedCharacter(x, y, sprite_path, 
                                                   SPRITE_FRAME_SIZE, ANIMATION_SPEED)
            self.image = self.animated_char.image
            self.rect = self.animated_char.rect
            self.has_animation = True
        else:
            # Fallback to simple colored square
            self.image = pygame.Surface((TILE_SIZE - 4, TILE_SIZE - 4))
            self.image.fill(BLUE)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.has_animation = False
            self.animated_char = None
        
        self.speed = PLAYER_SPEED
        self.last_direction = (0, -1)  # Up by default
        self.health = 1000  # Initial health
        
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
        
        # Update animation direction if using animated character
        if self.has_animation:
            # Normalize direction for animation (dx and dy should be -1, 0, or 1)
            anim_dx = -1 if dx < 0 else (1 if dx > 0 else 0)
            anim_dy = -1 if dy < 0 else (1 if dy > 0 else 0)
            self.animated_char.set_direction(anim_dx, anim_dy)
        
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
        
        # Update animation frame
        if self.has_animation:
            self.animated_char.rect = self.rect  # Sync position
            self.animated_char.update_animation()
            self.image = self.animated_char.image
    
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
    
    def take_damage(self, damage):
        """Reduce player health by damage amount"""
        self.health -= damage
        if self.health < 0:
            self.health = 0
