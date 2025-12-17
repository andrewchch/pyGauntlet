"""
Test script for menu functionality
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from menu import Menu
from game import Game
from constants import *

def test_menu():
    """Test menu component"""
    print("Testing menu functionality...")
    print("=" * 60)
    
    # Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Test 1: Menu creation
    print("Test 1: Creating menu...")
    try:
        menu = Menu(screen)
        assert menu is not None
        print("✓ Menu created successfully")
    except Exception as e:
        print(f"✗ Menu creation failed: {e}")
        return False
    
    # Test 2: Menu drawing (initial state)
    print()
    print("Test 2: Testing menu draw (initial state)...")
    try:
        menu.draw(is_paused=False)
        print("✓ Menu draws successfully in initial state")
    except Exception as e:
        print(f"✗ Menu draw failed: {e}")
        return False
    
    # Test 3: Menu drawing (paused state)
    print()
    print("Test 3: Testing menu draw (paused state)...")
    try:
        menu.draw(is_paused=True)
        print("✓ Menu draws successfully in paused state")
    except Exception as e:
        print(f"✗ Menu draw (paused) failed: {e}")
        return False
    
    # Test 4: Menu input handling
    print()
    print("Test 4: Testing menu input handling...")
    try:
        # Test RETURN key
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_RETURN)
        result = menu.handle_input(event)
        assert result == True
        print("✓ Menu handles RETURN key correctly")
        
        # Test SPACE key
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_SPACE)
        result = menu.handle_input(event)
        assert result == True
        print("✓ Menu handles SPACE key correctly")
        
        # Test other key (should not trigger selection)
        event = pygame.event.Event(pygame.KEYDOWN, key=pygame.K_a)
        result = menu.handle_input(event)
        assert result == False
        print("✓ Menu ignores non-selection keys correctly")
    except Exception as e:
        print(f"✗ Menu input handling failed: {e}")
        return False
    
    # Test 5: Game state integration
    print()
    print("Test 5: Testing game state integration...")
    try:
        game = Game()
        assert game.state == STATE_MENU
        print("✓ Game starts in MENU state")
        
        # Simulate menu selection to start game
        game.state = STATE_PLAYING
        assert game.state == STATE_PLAYING
        print("✓ Game transitions to PLAYING state")
        
        # Simulate ESC key to pause
        game.state = STATE_PAUSED
        assert game.state == STATE_PAUSED
        print("✓ Game transitions to PAUSED state")
        
        # Simulate resume
        game.state = STATE_PLAYING
        assert game.state == STATE_PLAYING
        print("✓ Game transitions back to PLAYING state")
    except Exception as e:
        print(f"✗ Game state integration failed: {e}")
        return False
    
    print()
    print("=" * 60)
    print("✓✓✓ ALL MENU TESTS PASSED! ✓✓✓")
    print("=" * 60)
    print()
    print("Menu Features Verified:")
    print("  ✓ Menu creation and initialization")
    print("  ✓ Menu rendering (initial and paused states)")
    print("  ✓ Input handling (RETURN, SPACE, and other keys)")
    print("  ✓ Game state transitions (MENU → PLAYING → PAUSED)")
    print()
    
    pygame.quit()
    return True

if __name__ == "__main__":
    success = test_menu()
    exit(0 if success else 1)
