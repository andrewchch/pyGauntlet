"""
Main game class
"""
import pygame
from constants import *
from player import Player
from game_map import GameMap
from camera import Camera
from menu import Menu

class Game:
    """Main game class that manages the game loop"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("pyGauntlet")
        self.clock = pygame.time.Clock()
        self.running = True
        self.state = STATE_MENU
        
        # Initialize menu
        self.menu = Menu(self.screen)
        
        # Initialize game objects
        self.game_map = GameMap()
        # Place player at a safe starting position
        self.player = Player(PLAYER_START_X * TILE_SIZE, PLAYER_START_Y * TILE_SIZE)
        self.camera = Camera(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE)
        
        # Sprite groups
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        
        # Shooting cooldown
        self.can_shoot = True
        self.shoot_cooldown = 250  # milliseconds
        self.last_shot_time = 0
    
    def reset_game(self):
        """Reset the game to initial state"""
        # Reset player to starting position
        self.player = Player(PLAYER_START_X * TILE_SIZE, PLAYER_START_Y * TILE_SIZE)
        
        # Reset camera
        self.camera = Camera(MAP_WIDTH * TILE_SIZE, MAP_HEIGHT * TILE_SIZE)
        
        # Clear all sprites
        self.enemies.empty()
        self.projectiles.empty()
        
        # Reset shooting cooldown
        self.last_shot_time = 0
        
    def run(self):
        """Main game loop"""
        while self.running:
            current_time = pygame.time.get_ticks()
            
            self.handle_events(current_time)
            
            if self.state == STATE_PLAYING:
                self.update(current_time)
            
            self.draw()
            
            self.clock.tick(FPS)
    
    def handle_events(self, current_time):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == STATE_PLAYING:
                        self.state = STATE_PAUSED
                    elif self.state == STATE_PAUSED:
                        self.state = STATE_PLAYING
                elif self.state == STATE_PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.shoot(current_time)
                elif self.state in (STATE_MENU, STATE_PAUSED, STATE_GAME_OVER):
                    if self.menu.handle_input(event):
                        if self.state == STATE_GAME_OVER:
                            self.reset_game()
                        self.state = STATE_PLAYING
    
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
            projectile.update(self.game_map.walls, self.enemies, self.game_map.generators)
        
        # Check if player collides with enemy and take damage
        hit_enemies = pygame.sprite.spritecollide(self.player, self.enemies, True)
        for enemy in hit_enemies:
            self.player.take_damage(enemy.damage)
            # Check for game over
            if self.player.health <= 0:
                self.state = STATE_GAME_OVER
    
    def draw(self):
        """Draw the game"""
        self.screen.fill(BLACK)
        
        if self.state == STATE_PLAYING or self.state == STATE_PAUSED or self.state == STATE_GAME_OVER:
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
        
        if self.state == STATE_MENU:
            self.menu.draw(is_paused=False, is_game_over=False)
        elif self.state == STATE_PAUSED:
            self.menu.draw(is_paused=True, is_game_over=False)
        elif self.state == STATE_GAME_OVER:
            self.menu.draw(is_paused=False, is_game_over=True)
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw UI elements"""
        font = pygame.font.Font(None, 36)
        
        # Draw player health
        health_text = font.render(f"Health: {self.player.health}", True, WHITE)
        self.screen.blit(health_text, (10, 10))
