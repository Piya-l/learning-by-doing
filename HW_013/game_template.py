"""
Bouncing Colorful Squares - Game Template
DO NOT MODIFY THIS FILE

This file contains the complete pygame setup and main game loop.
Your task is to implement the BouncingSquare class in bouncing_object.py
"""

import pygame
import sys
from bouncing_object import BouncingSquare

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bouncing Colorful Squares")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# List to store all bouncing squares
squares = []


def get_color_stats():
    """
    Calculate the frequency of each color among all squares.
    Returns a dictionary with color names as keys and counts as values.
    """
    color_count = {}
    for square in squares:
        color_name = square.get_color_name()
        color_count[color_name] = color_count.get(color_name, 0) + 1
    return color_count


def draw_stats(surface):
    """
    Draw the color statistics in the top-right corner.
    """
    stats = get_color_stats()
    font = pygame.font.Font(None, 24)
    
    y_offset = 10
    for color_name, count in sorted(stats.items()):
        text = f"{color_name}: {count}"
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.topright = (SCREEN_WIDTH - 10, y_offset)
        surface.blit(text_surface, text_rect)
        y_offset += 25


def find_square_at_position(x, y):
    """
    Find and return the first square that contains the point (x, y).
    Returns None if no square is found at that position.
    """
    for square in squares:
        if square.contains_point(x, y):
            return square
    return None


# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            
            # Left click: Add new square
            if event.button == 1:  # Left mouse button
                new_square = BouncingSquare(mouse_x, mouse_y, SCREEN_WIDTH, SCREEN_HEIGHT)
                squares.append(new_square)
                print(f"Added new square at ({mouse_x}, {mouse_y})")
            
            # Right click: Remove square
            elif event.button == 3:  # Right mouse button
                square_to_remove = find_square_at_position(mouse_x, mouse_y)
                if square_to_remove:
                    squares.remove(square_to_remove)
                    print(f"Removed square. Total: {len(squares)}")
    
    # Update all squares
    for square in squares:
        square.update()
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw all squares
    for square in squares:
        square.draw(screen)
    
    # Draw statistics
    draw_stats(screen)
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

# Cleanup
pygame.quit()
sys.exit()
