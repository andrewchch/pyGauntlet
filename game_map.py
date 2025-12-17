"""
Game map class
"""
import pygame
from constants import *
from wall import Wall
from generator import Generator

class GameMap:
    """Manages the game map layout"""
    
    def __init__(self):
        self.width = MAP_WIDTH
        self.height = MAP_HEIGHT
        self.walls = pygame.sprite.Group()
        self.generators = pygame.sprite.Group()
        self.create_map()
    
    def create_map(self):
        """Create the initial map layout"""
        # Create border walls
        for x in range(self.width):
            self.walls.add(Wall(x, 0))
            self.walls.add(Wall(x, self.height - 1))
        
        for y in range(self.height):
            self.walls.add(Wall(0, y))
            self.walls.add(Wall(self.width - 1, y))
        
        # Add some interior walls to create rooms/corridors
        # Horizontal walls
        for x in range(10, 20):
            self.walls.add(Wall(x, 10))
            self.walls.add(Wall(x, 20))
        
        for x in range(25, 35):
            self.walls.add(Wall(x, 15))
        
        # Vertical walls
        for y in range(5, 15):
            self.walls.add(Wall(20, y))
        
        for y in range(18, 25):
            self.walls.add(Wall(30, y))
        
        # Add generators in corners and middle areas
        self.generators.add(Generator(5, 5))
        self.generators.add(Generator(35, 5))
        self.generators.add(Generator(5, 25))
        self.generators.add(Generator(35, 25))
    
    def get_tile_at(self, x, y):
        """Get tile type at world coordinates"""
        tile_x = x // TILE_SIZE
        tile_y = y // TILE_SIZE
        
        for wall in self.walls:
            if wall.rect.x // TILE_SIZE == tile_x and wall.rect.y // TILE_SIZE == tile_y:
                return 'wall'
        
        return 'floor'
