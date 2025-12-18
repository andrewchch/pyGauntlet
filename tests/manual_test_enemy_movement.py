"""
Manual test to visually demonstrate the improved enemy movement
"""
import pygame
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from enemy import Enemy
from player import Player
from wall import Wall
from constants import *

def run_visual_test():
    """
    Create a visual demonstration of enemy movement improvement
    Shows enemies navigating around walls toward the player
    """
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Enemy Movement Test - Navigate Around Walls")
    clock = pygame.time.Clock()
    
    # Create player in center
    player = Player(400, 300)
    
    # Create enemies in various positions with walls blocking direct paths
    enemies = pygame.sprite.Group()
    
    # Enemy 1: Below a horizontal wall (tests vertical blocked -> horizontal movement)
    enemy1 = Enemy(400, 450)
    enemies.add(enemy1)
    
    # Enemy 2: Right of a vertical wall (tests horizontal blocked -> vertical movement)
    enemy2 = Enemy(600, 300)
    enemies.add(enemy2)
    
    # Enemy 3: In a corner (tests multiple blocked directions)
    enemy3 = Enemy(100, 100)
    enemies.add(enemy3)
    
    # Create walls
    walls = pygame.sprite.Group()
    
    # Horizontal wall above enemy1
    for i in range(10, 16):
        wall = Wall(i, 12)
        walls.add(wall)
    
    # Vertical wall left of enemy2
    for i in range(6, 12):
        wall = Wall(16, i)
        walls.add(wall)
    
    # L-shaped wall near enemy3
    for i in range(1, 5):
        wall = Wall(i, 5)
        walls.add(wall)
    for i in range(2, 6):
        wall = Wall(5, i)
        walls.add(wall)
    
    # Game loop
    running = True
    paused = False
    frame_count = 0
    
    font = pygame.font.Font(None, 24)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_ESCAPE:
                    running = False
        
        if not paused:
            # Update enemies
            for enemy in enemies:
                enemy.update(player, walls, None)
            
            frame_count += 1
        
        # Draw everything
        screen.fill(BLACK)
        
        # Draw walls
        for wall in walls:
            pygame.draw.rect(screen, GRAY, wall.rect)
        
        # Draw player
        pygame.draw.rect(screen, BLUE, player.rect)
        
        # Draw enemies
        for enemy in enemies:
            pygame.draw.rect(screen, RED, enemy.rect)
        
        # Draw instructions
        instructions = [
            "Enemy Movement Test - Navigating Around Walls",
            "",
            "BLUE = Player (you)",
            "RED = Enemies (chasing you)",
            "GRAY = Walls (blocking direct paths)",
            "",
            "Watch enemies navigate around walls!",
            "SPACE = Pause/Resume",
            "ESC = Exit",
            f"Frame: {frame_count}"
        ]
        
        y = 10
        for line in instructions:
            text = font.render(line, True, WHITE)
            screen.blit(text, (10, y))
            y += 25
        
        pygame.display.flip()
        clock.tick(60)
        
        # Auto-stop after demonstrating for a bit
        if frame_count >= 300:  # 5 seconds at 60 FPS
            # Take a screenshot
            pygame.image.save(screen, "/tmp/enemy_movement_demo.png")
            print("Screenshot saved to /tmp/enemy_movement_demo.png")
            running = False
    
    pygame.quit()

if __name__ == '__main__':
    run_visual_test()
