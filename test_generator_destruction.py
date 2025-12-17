"""
Test script to verify generator destruction mechanics
"""
import pygame
import os
os.environ['SDL_VIDEODRIVER'] = 'dummy'

from generator import Generator
from projectile import Projectile
from constants import TILE_SIZE

def test_generator_destruction():
    """Test that generators are destroyed after 3 hits"""
    print("="*60)
    print("Testing Generator Destruction Mechanics")
    print("="*60)
    
    pygame.init()
    
    # Test 1: Generator starts with 3 health
    print("\nTest 1: Generator initial health...")
    gen = Generator(5, 5)
    assert gen.health == 3, f"Expected health 3, got {gen.health}"
    print("✓ Generator starts with 3 health")
    
    # Test 2: Generator takes damage
    print("\nTest 2: Generator takes damage...")
    generators = pygame.sprite.Group()
    generators.add(gen)
    gen.take_damage()
    assert gen.health == 2, f"Expected health 2 after 1 hit, got {gen.health}"
    assert gen.alive(), "Generator should still be alive after 1 hit"
    print("✓ Generator health reduced to 2 after 1 hit")
    
    # Test 3: Generator takes second damage
    print("\nTest 3: Generator takes more damage...")
    gen.take_damage()
    assert gen.health == 1, f"Expected health 1 after 2 hits, got {gen.health}"
    assert gen.alive(), "Generator should still be alive after 2 hits"
    print("✓ Generator health reduced to 1 after 2 hits")
    
    # Test 4: Generator destroyed after 3rd hit
    print("\nTest 4: Generator destroyed after 3rd hit...")
    gen.take_damage()
    assert gen.health == 0, f"Expected health 0 after 3 hits, got {gen.health}"
    assert not gen.alive(), "Generator should be destroyed after 3 hits"
    print("✓ Generator destroyed after 3 hits")
    
    # Test 5: Projectile damages generator
    print("\nTest 5: Projectile damages generator...")
    gen2 = Generator(10, 10)
    generators = pygame.sprite.Group()
    generators.add(gen2)
    
    walls = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    
    # Create projectile aimed at generator
    proj = Projectile(gen2.rect.centerx - 20, gen2.rect.centery, (1, 0))
    
    # Move projectile to hit generator
    for _ in range(10):
        proj.update(walls, enemies, generators)
        if not gen2.alive():
            break
    
    # After one pass, generator should have 2 health left
    assert gen2.health < 3, "Generator should have taken at least one hit"
    print(f"✓ Projectile damages generator (health: {gen2.health})")
    
    # Test 6: Multiple projectile hits destroy generator
    print("\nTest 6: Multiple projectile hits destroy generator...")
    gen3 = Generator(15, 15)
    generators3 = pygame.sprite.Group()
    generators3.add(gen3)
    
    # Fire 3 projectiles to destroy generator
    for i in range(3):
        proj = Projectile(gen3.rect.centerx, gen3.rect.centery, (1, 0))
        proj.update(walls, enemies, generators3)
        print(f"  Hit {i+1}: Generator health = {gen3.health}")
    
    assert gen3.health == 0, f"Expected health 0 after 3 projectile hits, got {gen3.health}"
    assert not gen3.alive(), "Generator should be destroyed after 3 projectile hits"
    print("✓ Generator destroyed after 3 projectile hits")
    
    print("\n" + "="*60)
    print("All Generator Destruction Tests Passed! ✓")
    print("="*60)
    
    pygame.quit()

if __name__ == "__main__":
    test_generator_destruction()
