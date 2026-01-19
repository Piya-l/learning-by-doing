"""
Solar System Simulation - Main Program
DO NOT MODIFY THIS FILE

This file contains the pygame setup and main game loop.
Your task is to implement the classes in celestial_bodies.py
"""

import pygame
import sys
from celestial_bodies import CelestialBody, Planet, Moon
from planet_data import (
    SUN_DATA, ALL_PLANETS, MOON_DATA, EARTH_DATA
)

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARK_GRAY = (30, 30, 30)

# Setup display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Label toggle flag
show_labels = False

# Font for labels
label_font = pygame.font.Font(None, 20)

# Speed multiplier for Enhancement 4
speed_multiplier = 1.0  # Default speed (1.0x)



# Sun position (center of screen)
sun_x = SCREEN_WIDTH // 2
sun_y = SCREEN_HEIGHT // 2

# Create the Sun
sun = CelestialBody(
    SUN_DATA["name"],
    SUN_DATA["color"],
    SUN_DATA["radius"],
    sun_x,
    sun_y
)

# Create all planets
planets = []
for planet_data in ALL_PLANETS:
    planet = Planet(
        planet_data["name"],
        planet_data["color"],
        planet_data["radius"],
        planet_data["orbital_radius"],
        planet_data["orbital_speed"]
    )
    planets.append(planet)

# Create Earth's moon
# Find Earth in the planets list
earth = None
for planet in planets:
    if planet.name == EARTH_DATA["name"]:
        earth = planet
        break

# Create moon that orbits Earth
moon = Moon(
    MOON_DATA["name"],
    MOON_DATA["color"],
    MOON_DATA["radius"],
    MOON_DATA["orbital_radius"],
    MOON_DATA["orbital_speed"]
)

# Font for displaying info
font = pygame.font.Font(None, 24)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_l:
                show_labels = not show_labels
                print(f"Labels: {'ON' if show_labels else 'OFF'}")
            elif event.key == pygame.K_UP:
                speed_multiplier = min(3.0, speed_multiplier + 0.25)
                print(f"Speed: {speed_multiplier:.2f}x")
            elif event.key == pygame.K_DOWN:
                speed_multiplier = max(0.5, speed_multiplier - 0.25)
                print(f"Speed: {speed_multiplier:.2f}x")
    
    # Update all planets
    for planet in planets:
        planet.update(sun_x, sun_y, speed_multiplier)
    
    # Update moon (orbits around Earth)
    if earth:
        moon.update(earth.x, earth.y, speed_multiplier)
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw orbital paths (optional visual guides)
    for planet in planets:
        pygame.draw.circle(screen, DARK_GRAY, (sun_x, sun_y), planet.orbital_radius, 1)
    
    # Draw Earth's moon orbital path
    if earth:
        pygame.draw.circle(screen, DARK_GRAY, (int(earth.x), int(earth.y)), MOON_DATA["orbital_radius"], 1)
    
    # Draw the Sun
    sun.draw(screen)
    sun.draw_label(screen, label_font, show_labels)
    
    # Draw all planets
    for planet in planets:
        planet.draw_trail(screen)
        planet.draw(screen)
        planet.draw_label(screen, label_font, show_labels)
    
    # Draw the Moon
    moon.draw_trail(screen)
    moon.draw(screen)
    moon.draw_label(screen, label_font, show_labels)
    
    # Draw title
    title_text = font.render("Solar System Simulation", True, WHITE)
    screen.blit(title_text, (10, 10))
    
    # Draw instructions
    instruction_text = label_font.render("ESC: exit | L: toggle labels | UP/DOWN: speed", True, WHITE)
    screen.blit(instruction_text, (10, 40))
    
    # Update display
    pygame.display.flip()
    
    # Control frame rate
    clock.tick(FPS)

# Cleanup
pygame.quit()
sys.exit()
