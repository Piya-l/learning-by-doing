# Homework 13: Bouncing Colorful Squares

In this assignment, you'll build an interactive pygame simulation with bouncing, rotating squares. Focus on proper object-oriented design with encapsulation and access control.

## Learning Goals

By completing this assignment, you will practice:
- Designing classes with proper encapsulation (private, protected, public members)
- Managing object state and behavior
- Handling user input events
- Working with collections of objects

## What You Need to Implement

Create a `BouncingSquare` class in `bouncing_object.py` that manages animated squares with these behaviors:

1. Squares bounce off screen edges
2. Each square rotates continuously (some clockwise, some counter-clockwise)
3. Left-click anywhere to spawn a new square
4. Right-click on a square to remove it
5. Display color statistics in the top-right corner

## Class Design Requirements

Your `BouncingSquare` class must follow proper encapsulation principles:

### Private Attributes (use `__` prefix)
These represent internal state that should not be accessed from outside:
- `__x, __y` - current position
- `__velocity_x, __velocity_y` - movement speeds
- `__angle` - rotation angle

### Protected Attributes (use `_` prefix)
These can be inherited by subclasses:
- `_color` - RGB color tuple
- `_color_name` - name of the color
- `_size` - square dimensions (pixels)
- `_rotation_speed` - degrees per frame
- `_rotation_direction` - 1 for clockwise, -1 for counter-clockwise

### Public Methods
- `__init__(x, y, screen_width, screen_height)` - constructor
- `update()` - update position and rotation
- `draw(surface)` - render the square
- `contains_point(px, py)` - check if point is inside square
- `get_color_name()` - return color name for statistics

### Private Methods
Separate internal logic into private helper methods:
- `__bounce_horizontal()` - handle left/right edge collisions
- `__bounce_vertical()` - handle top/bottom edge collisions
- `__update_rotation()` - update rotation angle

### Method Overloading
Support both signatures:
- `update()` - normal update
- `update(speed_multiplier)` - with optional speed multiplier for testing

## Random Properties

Each square should initialize with random values:
- Color: randomly chosen from 8 colors (Red, Green, Blue, Yellow, Cyan, Magenta, Orange, Purple)
- Size: random between 20-60 pixels
- Velocity: random float between -3.0 and 3.0 for both x and y (but never exactly zero)
- Rotation speed: random between 1.0-5.0 degrees per frame
- Rotation direction: randomly choose clockwise or counter-clockwise

## Files Provided

**game_template.py** - Complete pygame framework with window setup, game loop, event handling, and statistics display. Do not modify this file.

**bouncing_object.py** - Template file where you'll write your implementation. See the TODO comments.

## Getting Started

Install dependencies:
```bash
pip install -r requirements.txt
```

Then implement the class following the template, and run:
```bash
python game_template.py
```

## Testing Your Implementation

When working correctly, you should see:
- Window opens with black background
- Left-clicking creates a square at that position
- Squares have different colors, sizes, and move in different directions
- Squares bounce when hitting screen edges
- Squares rotate continuously
- Right-clicking on a square removes it
- Top-right shows color counts (e.g., "Red: 3, Blue: 5")

## Submission

Submit your completed `bouncing_object.py` file via GitHub Classroom. 

Your code must:
- Use proper access modifiers (private `__`, protected `_`)
- Implement all required methods
- Use private helper methods for internal logic
- Not modify `game_template.py`

## Common Pitfalls

Watch out for these mistakes:
- Forgetting to use `__` or `_` prefixes for attributes
- Not handling both horizontal and vertical bouncing
- Improper centering when rotating (squares will orbit instead of spin)
- Using integer division for velocities (causes choppy movement)
- Allowing zero velocity (squares won't move)
- Not updating rotation angle in the update method
