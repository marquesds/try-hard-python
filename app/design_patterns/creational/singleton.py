"""
Singleton:
    Lets you ensure that a class has only one instance,
    while providing a global access point to this instance.

See: https://refactoring.guru/design-patterns/singleton
"""
import random


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UniverseAnswer(metaclass=SingletonMeta):
    def __init__(self):
        self.random_number = random.randint(0, 100)

    def answer(self):
        return id(self) + self.random_number
