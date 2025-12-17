"""
Main game class
"""
import pygame
from constants import *
from player import Player
from game_map import GameMap
from camera import Camera

class Game:
    """Main game class that manages the game loop"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("pyGauntlet")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize game objects
        self.game_map = GameMap()
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.camera = Camera(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE)
        
        # Sprite groups
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        
        # Shooting cooldown
        self.can_shoot = True
        self.shoot_cooldown = 250  # milliseconds
        self.last_shot_time = 0
        
    def run(self):
        """Main game loop"""
        while self.running:
            current_time = pygame.time.get_ticks()
            
            self.handle_events(current_time)
            self.update(current_time)
            self.draw()
            
            self.clock.tick(FPS)
    
    def handle_events(self, current_time):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shoot(current_time)
    
    def shoot(self, current_time):
        """Fire a projectile"""
        if current_time - self.last_shot_time >= self.shoot_cooldown:
            self.last_shot_time = current_time
            projectile = self.player.shoot()
            self.projectiles.add(projectile)
    
    def update(self, current_time):
        """Update game state"""
        keys = pygame.key.get_pressed()
        
        # Update player
        self.player.update(keys, self.game_map.walls)
        
        # Update camera to follow player
        self.camera.update(self.player)
        
        # Update generators (spawn enemies)
        for generator in self.game_map.generators:
            generator.update(current_time, self.enemies)
        
        # Update enemies
        for enemy in self.enemies:
            enemy.update(self.player, self.game_map.walls, self.game_map)
        
        # Update projectiles
        for projectile in self.projectiles:
            projectile.update(self.game_map.walls, self.enemies)
        
        # Check if player collides with enemy (game over condition could be added)
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            # For now, just reduce enemy count by destroying the enemy
            hit_enemies = pygame.sprite.spritecollide(self.player, self.enemies, True)
    
    def draw(self):
        """Draw the game"""
        self.screen.fill(BLACK)
        
        # Draw walls
        for wall in self.game_map.walls:
            self.screen.blit(wall.image, self.camera.apply(wall))
        
        # Draw generators
        for generator in self.game_map.generators:
            self.screen.blit(generator.image, self.camera.apply(generator))
        
        # Draw enemies
        for enemy in self.enemies:
            self.screen.blit(enemy.image, self.camera.apply(enemy))
        
        # Draw projectiles
        for projectile in self.projectiles:
            self.screen.blit(projectile.image, self.camera.apply(projectile))
        
        # Draw player
        self.screen.blit(self.player.image, self.camera.apply(self.player))
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw UI elements"""
        font = pygame.font.Font(None, 36)
        
        # Draw enemy count
        enemy_text = font.render(f"Enemies: {len(self.enemies)}", True, WHITE)
        self.screen.blit(enemy_text, (10, 10))
