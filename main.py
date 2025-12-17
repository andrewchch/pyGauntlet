"""
pyGauntlet - A Gauntlet II-inspired game
Main entry point for the game
"""
import pygame
from game import Game

def main():
    """Initialize and run the game"""
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()

if __name__ == "__main__":
    main()
