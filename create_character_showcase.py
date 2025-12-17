"""
Create a screenshot showing the animated character sprites
"""
import pygame
import os
from entities.character import AnimatedCharacter
from constants import *

def create_sprite_showcase():
    """Create a showcase of all character animations"""
    pygame.init()
    
    # Create a larger display to show all animations
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Character Sprite Showcase")
    
    sprite_path = 'resources/sprites/character-spritesheet.png'
    
    # Create characters for each direction
    chars = []
    directions = [
        (AnimatedCharacter.DIRECTION_UP, "UP", (0, -1)),
        (AnimatedCharacter.DIRECTION_LEFT, "LEFT", (-1, 0)),
        (AnimatedCharacter.DIRECTION_DOWN, "DOWN", (0, 1)),
        (AnimatedCharacter.DIRECTION_RIGHT, "RIGHT", (1, 0)),
    ]
    
    # Position characters in a grid
    start_x = 150
    start_y = 150
    spacing = 180
    
    for i, (direction, name, movement) in enumerate(directions):
        x = start_x + (i % 2) * spacing
        y = start_y + (i // 2) * spacing
        char = AnimatedCharacter(x, y, sprite_path)
        char.set_direction(movement[0], movement[1])
        chars.append((char, name, movement))
    
    # Render the showcase
    screen.fill(BLACK)
    
    # Title
    title_font = pygame.font.Font(None, 48)
    title = title_font.render("Character Animation Showcase", True, WHITE)
    title_rect = title.get_rect(center=(width // 2, 50))
    screen.blit(title, title_rect)
    
    # Draw each character with label
    label_font = pygame.font.Font(None, 32)
    info_font = pygame.font.Font(None, 24)
    
    for char, name, movement in chars:
        # Update animation to show a mid-walk frame
        char.animation_frame = 2.0  # Show frame 2 for variety
        char.update_animation()
        
        # Draw character
        screen.blit(char.image, char.rect)
        
        # Draw label
        label = label_font.render(name, True, YELLOW)
        label_rect = label.get_rect(center=(char.rect.centerx, char.rect.bottom + 20))
        screen.blit(label, label_rect)
    
    # Add info text
    info_lines = [
        "Features:",
        "• 9-frame walking animations",
        "• 4 directions (Up, Down, Left, Right)",
        "• LPC sprite sheet format (64x64 frames)",
        "• Idle states when not moving",
        "• Smooth animation cycling",
    ]
    
    y_offset = 400
    for line in info_lines:
        text = info_font.render(line, True, WHITE)
        screen.blit(text, (50, y_offset))
        y_offset += 30
    
    # Save screenshot
    pygame.display.flip()
    screenshot_path = "character_animation_showcase.png"
    pygame.image.save(screen, screenshot_path)
    print(f"Screenshot saved to {screenshot_path}")
    
    pygame.quit()
    return screenshot_path

if __name__ == "__main__":
    create_sprite_showcase()
