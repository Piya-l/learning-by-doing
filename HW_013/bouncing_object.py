"""
Bouncing Square Class - Student Implementation File
TODO: Implement the BouncingSquare class according to the assignment specifications
"""

import pygame
import random

# Color palette for squares
COLORS = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "Orange": (255, 165, 0),
    "Purple": (128, 0, 128)
}


class BouncingSquare:
    """
    Represents a bouncing, rotating square in the game.
    
    TODO: Implement all methods below according to the README instructions.
    """
    
    def __init__(self, x, y, screen_width, screen_height):
        """
        Initialize a new bouncing square.
        
        Args:
            x (int): Initial x position (where user clicked)
            y (int): Initial y position (where user clicked)
            screen_width (int): Width of the game screen
            screen_height (int): Height of the game screen
        
        TODO: Initialize the following attributes:
            - self.x, self.y: Position
            - self.screen_width, self.screen_height: Screen boundaries
            - self.color: Random color from COLORS dictionary (RGB tuple)
            - self.color_name: Name of the color (string key from COLORS)
            - self.size: Random size between 20 and 60
            - self.velocity_x: Random speed between -3.0 and 3.0 (not zero)
            - self.velocity_y: Random speed between -3.0 and 3.0 (not zero)
            - self.angle: Starting rotation angle (0)
            - self.rotation_speed: Random speed between 1.0 and 5.0
            - self.rotation_direction: Random choice (1 or -1)
        """
        pass  # TODO: Remove this and implement
    
    def update(self):
        """
        Update the square's position and rotation.
        
        TODO: Implement the following:
            1. Update x and y position using velocity
            2. Check for collisions with screen edges and bounce
               - If x goes out of bounds, reverse velocity_x
               - If y goes out of bounds, reverse velocity_y
            3. Update the rotation angle
            4. Keep angle within 0-360 degrees range
        """
        pass  # TODO: Remove this and implement
    
    def draw(self, surface):
        """
        Draw the square on the given surface.
        
        Args:
            surface: Pygame surface to draw on
        
        TODO: Implement the following:
            1. Create a pygame.Surface for the square
            2. Fill it with self.color
            3. Rotate the surface using pygame.transform.rotate()
            4. Get the rect and center it at the square's position
            5. Blit (draw) the rotated surface onto the screen
        
        Hint: See the README for example code
        """
        pass  # TODO: Remove this and implement
    
    def contains_point(self, px, py):
        """
        Check if a point (px, py) is inside this square's bounding box.
        
        Args:
            px (int): X coordinate of the point
            py (int): Y coordinate of the point
        
        Returns:
            bool: True if point is inside the square, False otherwise
        
        TODO: Implement point-in-rectangle detection
        """
        pass  # TODO: Remove this and implement
    
    def get_color_name(self):
        """
        Get the name of this square's color.
        
        Returns:
            str: The color name (e.g., "Red", "Blue")
        
        TODO: Return self.color_name
        """
        pass  # TODO: Remove this and implement
