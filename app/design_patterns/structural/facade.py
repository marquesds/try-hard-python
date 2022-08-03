"""
Facade:
    Provides a simplified interface to a library, a framework,
    or any other complex set of classes.

See: https://refactoring.guru/design-patterns/facade
"""
from decimal import Decimal
from numbers import Number
from typing import Dict


class NumberSystem:
    def sum(self, first_number: Number, second_number: Number) -> Number:
        ...


class IntSystem:
    def sum(self, first_number: int, second_number: int) -> int:
        return int(first_number) + int(second_number)


class FloatSystem:
    def sum(self, first_number: float, second_number: float) -> float:
        return float(first_number) + float(second_number)


class DecimalSystem:
    def sum(self, first_number: Decimal, second_number: Decimal) -> Decimal:
        return Decimal(first_number) + Decimal(second_number)


class Facade:
    def __init__(
        self,
        number_system_1: NumberSystem,
        number_system_2: NumberSystem,
        number_system_3: NumberSystem,
    ) -> None:
        self.number_system_1 = number_system_1
        self.number_system_2 = number_system_2
        self.number_system_3 = number_system_3

    def sum_everything(self, first_number: Number, second_number: Number) -> Dict[str, Number]:
        return {
            "int": self.number_system_1.sum(first_number, second_number),
            "float": self.number_system_2.sum(first_number, second_number),
            "decimal": self.number_system_3.sum(first_number, second_number),
        }
