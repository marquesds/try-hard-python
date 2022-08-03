"""
Composite:
    Lets you compose objects into tree structures and then
    work with these structures as if they were individual objects.

See: https://refactoring.guru/design-patterns/composite
"""
from __future__ import annotations

import abc
from typing import List, Optional, Union


class Subject(abc.ABC):
    @property
    def parent(self) -> Optional[Subject]:
        return self._parent

    @parent.setter
    def parent(self, parent: Optional[Subject]):
        self._parent = parent

    def is_composite(self) -> bool:
        return False

    @abc.abstractmethod
    def get_name(self) -> Optional[str]:
        pass

    def get_subject(self) -> Optional[str]:
        return self.get_name()


class Leaf(Subject):
    def get_name(self) -> Optional[str]:
        pass


class Composite(Subject):
    def __init__(self) -> None:
        self._children: List[Subject] = []

    def add(self, component: Subject) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Subject) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def get_name(self) -> Optional[str]:
        pass

    def get_subject(self) -> Optional[str]:
        results = [self.get_name()] if self.get_name() else []
        for child in self._children:
            results.append(child.get_subject())
        return ", ".join(results)


class BiologySubject(Leaf):
    def get_name(self) -> Optional[str]:
        return "Biology"


class SRPSubject(Leaf):
    def get_name(self) -> Optional[str]:
        return "Single Responsibility Principle"


class OCPSubject(Leaf):
    def get_name(self) -> Optional[str]:
        return "Open/Closed Principle"


class LSPSubject(Leaf):
    def get_name(self) -> Optional[str]:
        return "Liskov Substitution Principle"


class ISPSubject(Leaf):
    def get_name(self) -> Optional[str]:
        return "Interface Segregation Principle"


class DIPSubject(Leaf):
    def get_name(self) -> Optional[str]:
        return "Dependency Inversion Principle"


class SOLIDSubject(Composite):
    def get_name(self) -> Optional[str]:
        return "SOLID"


class OOPSubject(Composite):
    def get_name(self) -> Optional[str]:
        return "OOP"


class ProgrammingSubject(Composite):
    def get_name(self) -> Optional[str]:
        return "Programming"


def get_biology_subject() -> Optional[str]:
    return BiologySubject().get_subject()


def get_programming_subjects() -> Optional[str]:
    composite = Composite()

    solid = SOLIDSubject()
    solid.add(SRPSubject())
    solid.add(OCPSubject())
    solid.add(LSPSubject())
    solid.add(ISPSubject())
    solid.add(DIPSubject())

    oop = OOPSubject()
    oop.add(solid)

    programming = ProgrammingSubject()
    programming.add(oop)

    composite.add(programming)
    return composite.get_subject()


if __name__ == "__main__":
    print(get_programming_subjects())
