"""
Decorator:
    Lets you attach new behaviors to objects by placing these objects
    inside special wrapper objects that contain the behaviors.

See: https://refactoring.guru/design-patterns/decorator
"""
import abc
from typing import Protocol


class Beverage(Protocol):
    def cost(self) -> int:
        """
        Cost being calculated in cents.
        """
        ...


class DarkRoast:
    def cost(self) -> int:
        return 199


class Decaf:
    def cost(self) -> int:
        return 299


class Expresso:
    def cost(self) -> int:
        return 99


class CondimentDecorator(abc.ABC):
    def __init__(self, beverage: Beverage) -> None:
        self.beverage = beverage

    @abc.abstractmethod
    def cost(self) -> int:
        pass


class Milk(CondimentDecorator):
    def cost(self) -> int:
        return self.beverage.cost() + 99


class Mocha(CondimentDecorator):
    def cost(self) -> int:
        return self.beverage.cost() + 199


class Soy(CondimentDecorator):
    def cost(self) -> int:
        return self.beverage.cost() + 349
