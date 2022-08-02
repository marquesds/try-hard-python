"""
Builder:
    Lets you construct complex objects step by step.
    The pattern allows you to produce different types
    and representations of an object using the same construction code.

See: https://refactoring.guru/design-patterns/builder
"""
from __future__ import annotations  # enables using current class as returning type


class UserBuilder:
    def __init__(self) -> None:
        self.name = ""
        self.age = 1
        self.phone = ""
        self.address = ""

    def add_name(self, value: str) -> UserBuilder:
        self.name = value
        return self

    def add_age(self, value: int) -> UserBuilder:
        self.age = value
        return self

    def add_phone(self, value: str) -> UserBuilder:
        self.phone = value
        return self

    def add_address(self, value: str) -> UserBuilder:
        self.address = value
        return self

    def build(self) -> User:
        return User(name=self.name, age=self.age, phone=self.phone, address=self.address)


class User:
    def __init__(self, name: str = "", age: int = 1, phone: str = "", address: str = "") -> None:
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
