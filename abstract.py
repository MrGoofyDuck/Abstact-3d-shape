import math
import random
from abc import ABC, abstractmethod

# Abstract Base Class
class Shape3D(ABC):
    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

# Sphere subclass
class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.radius ** 3

# Cylinder subclass
class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

# Cube subclass
class Cube(Shape3D):
    def __init__(self, side_length):
        self.side_length = side_length

    def surface_area(self):
        return 6 * self.side_length ** 2

    def volume(self):
        return self.side_length ** 3

# Function to generate random shapes
def generate_random_shape():
    shape_type = random.choice(['Sphere', 'Cylinder', 'Cube'])
    if shape_type == 'Sphere':
        radius = random.randint(1, 10)
        return Sphere(radius)
    elif shape_type == 'Cylinder':
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)
    else:
        side_length = random.randint(1, 10)
        return Cube(side_length)

# Generate a list of 10 random shapes
shapes = [generate_random_shape() for _ in range(10)]

# Display results
for i, shape in enumerate(shapes, start=1):
    shape_name = shape.__class__.__name__
    sa = shape.surface_area()
    vol = shape.volume()
    print(f"Shape {i}: {shape_name}")
    print(f"  Surface Area: {sa:.2f}")
    print(f"  Volume: {vol:.2f}")
    print("-" * 30)
