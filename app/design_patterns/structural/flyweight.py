"""
Flyweight:
    Lets you fit more objects into the available amount of RAM
    by sharing common parts of state between multiple objects
    instead of keeping all of the data in each object.

See: https://refactoring.guru/design-patterns/flyweight
"""
import random
from typing import Dict, List, Protocol


class Shape(Protocol):
    def area(self) -> int:
        ...


class Rectangle:
    """
    The max number of rectangles will be the max number of colors.
    """

    def __init__(self, color: str, x: int = 0, y: int = 0) -> None:
        self.color = color
        self.x = x
        self.y = y

    def area(self) -> int:
        return self.x * self.y


class RectangleFactory:
    _instances: Dict[str, Rectangle] = {}

    def create(self, color: str) -> Rectangle:
        rectangle = self._instances.get(color)
        if not rectangle:
            rectangle = Rectangle(color)
            self._instances[color] = rectangle
        return rectangle


class RectangleFlyweight:
    def __init__(self, factory: RectangleFactory):
        self.factory = factory

    def rectangles(self, number_rectangles: int = 1) -> List[Rectangle]:
        results = []
        for i in range(number_rectangles):
            rectangle = self.factory.create(self.random_color())
            rectangle.x = random.randint(1, 100)
            rectangle.y = random.randint(1, 100)
            results.append(rectangle)
        return results

    def random_color(self) -> str:
        colors = ["Red", "Green", "Blue", "White", "Black"]
        return random.choice(colors)
