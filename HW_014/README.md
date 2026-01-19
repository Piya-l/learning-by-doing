# Homework 14: Solar System Simulation

Build a realistic orbital animation of our solar system using inheritance and polymorphism. You'll implement a class hierarchy that demonstrates proper OOP design with method overriding and encapsulation.

## Learning Goals

This assignment covers:
- Designing class hierarchies with inheritance
- Implementing polymorphism through method overriding
- Proper use of protected and private attributes
- Applying parametric equations for circular motion

## Assignment Overview

Create a pygame simulation showing the Sun at the center with all 8 planets orbiting around it. Earth should have its own moon orbiting around it. Each celestial body will have accurate colors and relative orbital speeds.

You'll also implement several enhancements: orbital trails showing the path history, size-based speed variation, toggleable labels, and adjustable simulation speed.

## Class Structure

Design three classes with proper inheritance:

```
CelestialBody (base class)
    |
    +-- Planet (derived class)
    |
    +-- Moon (derived class)
```

### CelestialBody (Base Class)

This is your abstract base class for all space objects.

**Protected Attributes** (use `_` prefix):
- `_name` - body's name
- `_color` - RGB color tuple
- `_radius` - visual size for rendering
- `_x, _y` - current screen position

**Public Methods**:
- `__init__(name, color, radius, x, y)` - constructor
- `draw(surface)` - render as a circle
- `draw_label(surface, font, show_labels)` - display name when enabled
- `draw_trail(surface)` - base implementation does nothing (will be overridden)

### Planet Class (Inherits CelestialBody)

Represents a planet orbiting the Sun.

**Additional Protected Attributes**:
- `_orbital_radius` - distance from Sun
- `_orbital_speed` - angular velocity (modified by size)
- `_angle` - current position in orbit

**Private Attributes** (use `__` prefix):
- `__trail` - list storing recent positions
- `__max_trail_length` - maximum trail size (around 80)

**Method Overriding**:
- Override `draw_trail(surface)` to show fading orbital path

**Public Methods**:
- `update(sun_x, sun_y, speed_multiplier=1.0)` - calculate new position using parametric circle equations

**Implementation Notes**:
- Use `super().__init__()` to initialize base class
- Apply size-based speed: multiply base speed by `(10 / radius)`
- Store positions in trail list, keep length under max
- Draw trail with fading effect (older positions more transparent)

### Moon Class (Inherits CelestialBody)

Represents a moon orbiting a planet. Very similar to Planet but orbits around its parent planet instead of the Sun.

**Method Overriding**:
- Override `draw_trail(surface)` same as Planet

**Public Methods**:
- `update(planet_x, planet_y, speed_multiplier=1.0)` - polymorphic method with different center point

Implement similar to Planet but with shorter trail length (around 50 positions).

## Required Features

### Core Requirements
1. Sun stays fixed at screen center
2. All 8 planets (Mercury through Neptune) orbit the Sun
3. Moon orbits Earth as Earth orbits the Sun
4. Use accurate colors and speeds from `planet_data.py`

### Enhancement Requirements
5. **Orbital Trails** - Store 50-100 recent positions, draw with fading transparency
6. **Size-Based Speed** - Smaller planets move faster using formula: `base_speed * (10 / radius)`
7. **Label Toggle** - Press 'L' key to show/hide planet names
8. **Speed Control** - Arrow keys adjust simulation speed from 0.5x to 3.0x

## Files Provided

**solar_system.py** - Complete game loop, event handling, and rendering. Do not modify.

**celestial_bodies.py** - Template file where you implement your three classes.

**planet_data.py** - Constants for all planets (colors, sizes, orbital parameters). Do not modify.

## Getting Started

Install pygame:
```bash
pip install -r requirements.txt
```

Implement the three classes in `celestial_bodies.py`, then run:
```bash
python solar_system.py
```

## Testing Your Work

Your simulation should:
- Show a yellow Sun in the center with 8 colored planets orbiting
- Display the Moon orbiting around Earth
- Show fading trails behind each moving body
- Respond to 'L' key by toggling planet name labels
- Respond to arrow keys by changing animation speed
- Have Mercury orbiting noticeably faster than Jupiter (size-based speed)

## OOP Requirements

Your implementation must demonstrate:
- **Inheritance** - Planet and Moon inherit from CelestialBody
- **Method Overriding** - Both override `draw_trail()` method
- **Polymorphism** - Both have `update()` methods with different parameters
- **Encapsulation** - Use protected (`_`) for inheritable attributes, private (`__`) for internal data
- **Super calls** - Use `super().__init__()` in derived class constructors

## Submission

Submit `celestial_bodies.py` via GitHub Classroom.

Your submission must include:
- All three classes properly implemented
- Correct inheritance relationships
- Method overriding for trails
- Protected and private attributes used appropriately
- All four enhancements working

## Common Mistakes

Be careful to avoid:
- Not importing the `math` module (needed for cos/sin)
- Using integers instead of floats for angles (causes precision loss)
- Making the Moon orbit the Sun instead of Earth
- Forgetting to increment the angle (nothing will move)
- Not calling `super().__init__()` in derived classes
- Confusing degrees and radians (Python's math functions use radians)
