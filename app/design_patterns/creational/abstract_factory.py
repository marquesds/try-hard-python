"""
Abstract Factory:
    Lets you produce families of related objects without specifying their concrete classes.

See: https://refactoring.guru/design-patterns/abstract-factory
"""
import abc
from typing import Protocol


class Monster(Protocol):
    def attack(self) -> str:
        ...


class Goblin:
    def attack(self):
        return "Goblin attack!"


class Orc:
    def attack(self):
        return "Orc attack!"


class MonsterFactory(abc.ABC):
    @abc.abstractmethod
    def create_monster(self) -> Monster:
        pass


class GoblinFactory(MonsterFactory):
    def create_monster(self) -> Monster:
        return Goblin()


class OrcFactory(MonsterFactory):
    def create_monster(self) -> Monster:
        return Orc()


def attack(factory: MonsterFactory) -> str:
    monster: Monster = factory.create_monster()
    return monster.attack()


def goblin_attack() -> str:
    return attack(GoblinFactory())


def orc_attack() -> str:
    return attack(OrcFactory())
