"""
Factory Method:
    Provides an interface for creating objects in a superclass,
    but allows subclasses to alter the type of objects that will be created.

See: https://refactoring.guru/design-patterns/factory-method
"""
import abc
from typing import Protocol


class Transport(Protocol):
    def deliver(self) -> str:
        ...


class Car:
    def deliver(self) -> str:
        return "Delivering by car"


class Motorcycle:
    def deliver(self) -> str:
        return "Delivering by motorcycle"


class TransportCreator(abc.ABC):
    @abc.abstractmethod
    def factory_method(self) -> Transport:
        pass

    def proceed_delivery(self) -> str:
        transport = self.factory_method()
        return transport.deliver()


class CarCreator(TransportCreator):
    def factory_method(self) -> Transport:
        return Car()


class MotorcycleCreator(TransportCreator):
    def factory_method(self) -> Transport:
        return Motorcycle()


def deliver_by_car() -> str:
    creator = CarCreator()
    return creator.proceed_delivery()


def deliver_by_motorcycle() -> str:
    creator = MotorcycleCreator()
    return creator.proceed_delivery()
