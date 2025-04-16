import abc
import random
import math

class Shape3D(abc.ABC):
    @abc.abstractmethod
    def surface_area(self):
        pass
    
    @abc.abstractmethod
    def volume(self):
        pass

class Sphere(Shape3D):
    def __init__(self, radius):
        self.radius = radius
    
    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
    
    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Cylinder(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)
    
    def volume(self):
        return math.pi * self.radius ** 2 * self.height

class Cube(Shape3D):
    def __init__(self, side_length):
        self.side_length = side_length
    
    def surface_area(self):
        return 6 * self.side_length ** 2
    
    def volume(self):
        return self.side_length ** 3

def generate_random_shape():
    shape_type = random.choice([Sphere, Cylinder, Cube])
    
    if shape_type == Sphere:
        radius = random.randint(1, 10)
        return Sphere(radius)
    
    elif shape_type == Cylinder:
        radius = random.randint(1, 10)
        height = random.randint(5, 20)
        return Cylinder(radius, height)
    
    elif shape_type == Cube:
        side_length = random.randint(1, 10)
        return Cube(side_length)

shapes = [generate_random_shape() for _ in range(10)]

for shape in shapes:
    shape_name = shape.__class__.__name__
    print(f"Shape: {shape_name}")
    print(f"Surface Area: {shape.surface_area():.2f}")
    print(f"Volume: {shape.volume():.2f}\n")
