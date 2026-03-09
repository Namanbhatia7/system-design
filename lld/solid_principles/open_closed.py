"""
Open/Closed Principle (OCP) - In-Depth Example

Scenario: Calculating the area of different shapes.
"""

import math
from abc import ABC, abstractmethod

# ==========================================
# Bad Practice (Violating OCP)
# ==========================================
class AreaCalculator_Bad:
    """
    This class is not closed for modification. 
    Every time we add a new shape (e.g., Triangle), we have to modify 
    this class to add a new `elif` branch. This breaks OCP!
    """
    def calculate_total_area(self, shapes: list) -> float:
        total = 0.0
        for shape in shapes:
            if shape['type'] == 'circle':
                total += math.pi * shape['radius'] ** 2
            elif shape['type'] == 'rectangle':
                total += shape['width'] * shape['height']
        return total


# ==========================================
# Good Practice (Following OCP)
# ==========================================
class Shape(ABC):
    """
    By creating an abstraction (Shape), we can extend our system
    with new shapes without ever modifying the AreaCalculator.
    """
    @abstractmethod
    def area(self) -> float:
        pass


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


class AreaCalculator:
    """
    This class is closed for modification but open for extension.
    It works for any object that implements the Shape interface.
    """
    def calculate_total_area(self, shapes: list[Shape]) -> float:
        return sum(shape.area() for shape in shapes)


# ==========================================
# Client Code
# ==========================================
if __name__ == "__main__":
    print("=== Open/Closed Principle Demonstration ===\n")

    shapes = [
        Circle(5),
        Rectangle(4, 5)
    ]

    calculator = AreaCalculator()
    total_area = calculator.calculate_total_area(shapes)
    
    print(f"Total Area calculated via OCP compliant code: {total_area:.2f}")

    # Now, if we want to add a Triangle, we don't need to change AreaCalculator!
    # We simply create a `class Triangle(Shape):` and pass it in.
