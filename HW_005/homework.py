###################
# For this classwork/homework, let's create all the missing classes here.
###################


# Create shapes
line = Line("Line1", "Blue", "cm", (0, 0), (3, 4))
rectangle = Rectangle("Rectangle1", "Red", "m", 5, 10)
square = Square("Square1", "Green", "m", 4)
cube = Cube("Cube1", "Yellow", "cm", 3)
sphere = Sphere("Sphere1", "Purple", "m", 2.5)

# Display information for each shape
print(line.display_info())
print(rectangle.display_info())
print(square.display_info())
print(cube.display_info())
print(sphere.display_info())

# Display all shapes
Shape.display_all_shapes()