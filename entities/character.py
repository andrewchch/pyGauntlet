"""
Animated character class using sprite sheet animations
"""
import pygame
from typing import Tuple, List
import os


class AnimatedCharacter(pygame.sprite.Sprite):
    """
    Character with sprite-based walking animations in four directions.
    
    Uses LPC (Liberated Pixel Cup) sprite sheet format where:
    - Row 0: Walk Up (9 frames)
    - Row 1: Walk Left (9 frames)
    - Row 2: Walk Down (9 frames)
    - Row 3: Walk Right (9 frames)
    Each frame is 64x64 pixels.
    """
    
    # Direction constants mapping to sprite sheet rows
    DIRECTION_UP = 0
    DIRECTION_LEFT = 1
    DIRECTION_DOWN = 2
    DIRECTION_RIGHT = 3
    
    def __init__(self, x: int, y: int, sprite_sheet_path: str, 
                 frame_size: int = 64, animation_speed: float = 0.15):
        """
        Initialize animated character.
        
        Args:
            x: Initial x position in pixels
            y: Initial y position in pixels
            sprite_sheet_path: Path to sprite sheet image file
            frame_size: Size of each frame in pixels (default 64x64)
            animation_speed: Animation speed multiplier (frames per update call)
        """
        super().__init__()
        
        self.frame_size = frame_size
        self.animation_speed = animation_speed
        self.animation_frame = 0.0  # Float for smooth animation
        self.current_direction = self.DIRECTION_DOWN  # Default facing down
        self.is_moving = False
        
        # Load sprite sheet
        self.sprite_sheet = self._load_sprite_sheet(sprite_sheet_path)
        
        # Extract animation frames for each direction
        self.animations = {
            self.DIRECTION_UP: self._extract_frames(0, 9),
            self.DIRECTION_LEFT: self._extract_frames(1, 9),
            self.DIRECTION_DOWN: self._extract_frames(2, 9),
            self.DIRECTION_RIGHT: self._extract_frames(3, 9),
        }
        
        # Set initial image and rect
        self.image = self.animations[self.current_direction][0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def _load_sprite_sheet(self, path: str) -> pygame.Surface:
        """
        Load sprite sheet from file.
        
        Args:
            path: Path to sprite sheet image
            
        Returns:
            Loaded sprite sheet surface
            
        Raises:
            FileNotFoundError: If sprite sheet file doesn't exist
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Sprite sheet not found: {path}")
        
        sprite_sheet = pygame.image.load(path).convert_alpha()
        return sprite_sheet
    
    def _extract_frames(self, row: int, num_frames: int) -> List[pygame.Surface]:
        """
        Extract animation frames from a specific row in the sprite sheet.
        
        Args:
            row: Row number in sprite sheet
            num_frames: Number of frames to extract from the row
            
        Returns:
            List of frame surfaces
        """
        frames = []
        y_offset = row * self.frame_size
        
        for col in range(num_frames):
            x_offset = col * self.frame_size
            
            # Create a subsurface for this frame
            frame = pygame.Surface((self.frame_size, self.frame_size), pygame.SRCALPHA)
            frame.blit(self.sprite_sheet, (0, 0), 
                      (x_offset, y_offset, self.frame_size, self.frame_size))
            frames.append(frame)
        
        return frames
    
    def set_direction(self, dx: int, dy: int) -> None:
        """
        Set character direction based on movement deltas.
        
        Args:
            dx: Horizontal movement delta (-1, 0, or 1)
            dy: Vertical movement delta (-1, 0, or 1)
        """
        # Prioritize vertical movement for direction
        if dy < 0:
            self.current_direction = self.DIRECTION_UP
        elif dy > 0:
            self.current_direction = self.DIRECTION_DOWN
        elif dx < 0:
            self.current_direction = self.DIRECTION_LEFT
        elif dx > 0:
            self.current_direction = self.DIRECTION_RIGHT
        
        # Update moving state
        self.is_moving = (dx != 0 or dy != 0)
    
    def update_animation(self) -> None:
        """
        Update the animation frame.
        
        Should be called each frame to advance the animation.
        Uses idle frame (frame 0) when not moving.
        """
        frames = self.animations[self.current_direction]
        
        if self.is_moving:
            # Advance animation frame
            self.animation_frame += self.animation_speed
            
            # Wrap around when we reach the end
            if self.animation_frame >= len(frames):
                self.animation_frame = 0.0
            
            # Get current frame index
            frame_index = int(self.animation_frame)
            self.image = frames[frame_index]
        else:
            # Use idle frame (first frame) when not moving
            self.animation_frame = 0.0
            self.image = frames[0]
    
    def get_current_frame(self) -> pygame.Surface:
        """
        Get the current animation frame.
        
        Returns:
            Current frame surface
        """
        return self.image
