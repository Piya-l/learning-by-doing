"""
Celestial Bodies Classes - Student Implementation File
TODO: Implement the CelestialBody, Planet, and Moon classes
"""

import pygame
import math


class CelestialBody:
    """
    Base class for all celestial objects (Sun, Planet, Moon).
    
    TODO: Implement this base class that will be inherited by Planet and Moon.
    """
    
    def __init__(self, name, color, radius, x, y):
        """
        Initialize a celestial body.
        
        Args:
            name (str): Name of the celestial body
            color (tuple): RGB color tuple (r, g, b)
            radius (int): Visual radius for drawing
            x (float): Initial x position
            y (float): Initial y position
        
        TODO: Store all parameters as instance variables
        """
        pass  # TODO: Remove and implement
    
    def draw(self, surface):
        """
        Draw the celestial body as a circle on the screen.
        
        Args:
            surface: Pygame surface to draw on
        
        TODO: Use pygame.draw.circle() to draw this body
              Convert x, y to integers for drawing
        """
        pass  # TODO: Remove and implement
    
    def draw_label(self, surface, font, show_labels):
        """
        Draw the name label next to the celestial body.
        
        Args:
            surface: Pygame surface to draw on
            font: Pygame font object
            show_labels (bool): Whether to show labels
        
        TODO: Enhancement 3 - Display the name when show_labels is True
              Render white text and position it next to the body
        """
        pass  # TODO: Remove and implement
    
    def draw_trail(self, surface):
        """
        Draw the orbital trail (can be empty for non-moving bodies like Sun).
        
        Args:
            surface: Pygame surface to draw on
        
        TODO: For CelestialBody base class, this can just pass
              Planet class will override this
        """
        pass  # Can remain pass for base class


class Planet(CelestialBody):
    """
    Represents a planet that orbits the Sun.
    
    TODO: Implement this class that inherits from CelestialBody.
    """
    
    def __init__(self, name, color, radius, orbital_radius, orbital_speed):
        """
        Initialize a planet.
        
        Args:
            name (str): Planet name
            color (tuple): RGB color
            radius (int): Visual size
            orbital_radius (int): Distance from Sun
            orbital_speed (float): Angular velocity in radians per frame
        
        TODO: 
            1. Call parent __init__ with name, color, radius, and initial position (0, 0)
            2. Store orbital_radius and orbital_speed as instance variables
            3. Initialize self.angle to 0 (starting angle)
            4. Enhancement 1: Initialize self.trail as an empty list
            5. Enhancement 2: Adjust orbital_speed based on radius (smaller = faster)
        
        Hint: Use super().__init__() to call the parent constructor
        Hint for Enhancement 2: self.orbital_speed = orbital_speed * (10 / self.radius)
        """
        pass  # TODO: Remove and implement
    
    def update(self, sun_x, sun_y, speed_multiplier=1.0):
        """
        Update the planet's position based on orbital motion around the Sun.
        
        Args:
            sun_x (float): X position of the Sun
            sun_y (float): Y position of the Sun
            speed_multiplier (float): Speed multiplier for Enhancement 4 (default 1.0)
        
        TODO:
            1. Increment self.angle by self.orbital_speed * speed_multiplier
            2. Calculate new x position: sun_x + orbital_radius * cos(angle)
            3. Calculate new y position: sun_y + orbital_radius * sin(angle)
            4. Enhancement 1: Append current (x, y) to self.trail list
            5. Enhancement 1: Keep trail limited to last 50-100 positions
        
        Hint: Use math.cos() and math.sin()
        Hint for trail: if len(self.trail) > 80: self.trail.pop(0)
        Hint for Enhancement 4: self.angle += self.orbital_speed * speed_multiplier
        """
        pass  # TODO: Remove and implement
    
    def draw_trail(self, surface):
        """
        Draw the orbital trail behind the planet.
        
        Args:
            surface: Pygame surface to draw on
        
        TODO: Enhancement 1
            Loop through self.trail and draw semi-transparent circles
            Older positions should be more transparent
        
        Hint: Use pygame.draw.circle() with smaller radius for trail dots
              Calculate alpha/opacity based on position in trail list
        """
        pass  # TODO: Remove and implement


class Moon(CelestialBody):
    """
    Represents a moon that orbits a planet.
    
    TODO: Implement this class that inherits from CelestialBody.
    """
    
    def __init__(self, name, color, radius, orbital_radius, orbital_speed):
        """
        Initialize a moon.
        
        Args:
            name (str): Moon name
            color (tuple): RGB color
            radius (int): Visual size
            orbital_radius (int): Distance from parent planet
            orbital_speed (float): Angular velocity in radians per frame
        
        TODO:
            1. Call parent __init__ with name, color, radius, and initial position (0, 0)
            2. Store orbital_radius and orbital_speed as instance variables
            3. Initialize self.angle to 0 (starting angle)
            4. Enhancement 1: Initialize self.trail as an empty list (same as Planet)
        """
        pass  # TODO: Remove and implement
    
    def update(self, planet_x, planet_y, speed_multiplier=1.0):
        """
        Update the moon's position based on orbital motion around its parent planet.
        
        Args:
            planet_x (float): X position of the planet
            planet_y (float): Y position of the planet
            speed_multiplier (float): Speed multiplier for Enhancement 4 (default 1.0)
        
        TODO:
            1. Increment self.angle by self.orbital_speed * speed_multiplier
            2. Calculate new x position: planet_x + orbital_radius * cos(angle)
            3. Calculate new y position: planet_y + orbital_radius * sin(angle)
            4. Enhancement 1: Append current (x, y) to self.trail (same as Planet)
        
        Hint for Enhancement 4: self.angle += self.orbital_speed * speed_multiplier
        """
        pass  # TODO: Remove and implement
    
    def draw_trail(self, surface):
        """
        Draw the orbital trail behind the moon.
        
        Args:
            surface: Pygame surface to draw on
        
        TODO: Enhancement 1 - Same as Planet.draw_trail()
        """
        pass  # TODO: Remove and implement
