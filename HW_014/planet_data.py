"""
Planet and Celestial Body Data
This file contains all the constants for the solar system simulation.
DO NOT MODIFY THIS FILE - use these values in your implementation.
"""

# Sun data (stationary at center)
SUN_DATA = {
    "name": "Sun",
    "color": (255, 255, 0),  # Yellow
    "radius": 30
}

# Planet data
# Each planet has: name, color (RGB), visual radius, orbital radius, orbital speed
MERCURY_DATA = {
    "name": "Mercury",
    "color": (169, 169, 169),  # Gray
    "radius": 4,
    "orbital_radius": 60,
    "orbital_speed": 0.04  # Fastest orbit
}

VENUS_DATA = {
    "name": "Venus",
    "color": (255, 198, 73),  # Orange-yellow
    "radius": 7,
    "orbital_radius": 90,
    "orbital_speed": 0.035
}

EARTH_DATA = {
    "name": "Earth",
    "color": (100, 149, 237),  # Blue
    "radius": 8,
    "orbital_radius": 120,
    "orbital_speed": 0.03
}

MARS_DATA = {
    "name": "Mars",
    "color": (188, 39, 50),  # Red
    "radius": 5,
    "orbital_radius": 150,
    "orbital_speed": 0.025
}

JUPITER_DATA = {
    "name": "Jupiter",
    "color": (201, 160, 112),  # Tan/brown
    "radius": 15,
    "orbital_radius": 200,
    "orbital_speed": 0.015
}

SATURN_DATA = {
    "name": "Saturn",
    "color": (218, 165, 32),  # Goldenrod
    "radius": 13,
    "orbital_radius": 250,
    "orbital_speed": 0.012
}

URANUS_DATA = {
    "name": "Uranus",
    "color": (79, 208, 231),  # Light blue
    "radius": 10,
    "orbital_radius": 300,
    "orbital_speed": 0.009
}

NEPTUNE_DATA = {
    "name": "Neptune",
    "color": (63, 84, 186),  # Dark blue
    "radius": 10,
    "orbital_radius": 350,
    "orbital_speed": 0.007  # Slowest orbit
}

# Moon data (orbits Earth)
MOON_DATA = {
    "name": "Moon",
    "color": (200, 200, 200),  # Light gray
    "radius": 3,
    "orbital_radius": 20,  # Distance from Earth
    "orbital_speed": 0.1  # Relatively fast orbit around Earth
}

# List of all planet data for easy iteration
ALL_PLANETS = [
    MERCURY_DATA,
    VENUS_DATA,
    EARTH_DATA,
    MARS_DATA,
    JUPITER_DATA,
    SATURN_DATA,
    URANUS_DATA,
    NEPTUNE_DATA
]
