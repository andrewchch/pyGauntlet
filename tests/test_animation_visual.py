"""
Visual test for animated character sprite
Run this to see the animations in action
"""
import pygame
import sys
from entities.character import AnimatedCharacter
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Character Animation Test")
    clock = pygame.time.Clock()
    
    # Create animated character in center of screen
    sprite_path = '../resources/sprites/character-spritesheet.png'
    char = AnimatedCharacter(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, sprite_path)
    
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        # Handle input
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT]:
            dx = -1
        elif keys[pygame.K_RIGHT]:
            dx = 1
        
        if keys[pygame.K_UP]:
            dy = -1
        elif keys[pygame.K_DOWN]:
            dy = 1
        
        # Update animation
        char.set_direction(dx, dy)
        char.update_animation()
        
        # Move character
        speed = 3
        char.rect.x += dx * speed
        char.rect.y += dy * speed
        
        # Draw
        screen.fill(BLACK)
        screen.blit(char.image, char.rect)
        
        # Draw instructions
        font = pygame.font.Font(None, 24)
        text = font.render("Use arrow keys to move. ESC to quit.", True, WHITE)
        screen.blit(text, (10, 10))
        
        # Draw direction info
        direction_names = {0: "UP", 1: "LEFT", 2: "DOWN", 3: "RIGHT"}
        dir_text = font.render(f"Direction: {direction_names[char.current_direction]}", True, WHITE)
        screen.blit(dir_text, (10, 40))
        
        frame_text = font.render(f"Frame: {int(char.animation_frame)}", True, WHITE)
        screen.blit(frame_text, (10, 70))
        
        moving_text = font.render(f"Moving: {char.is_moving}", True, WHITE)
        screen.blit(moving_text, (10, 100))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
