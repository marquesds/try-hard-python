from decimal import Decimal

from app.design_patterns.structural.facade import (
    DecimalSystem,
    Facade,
    FloatSystem,
    IntSystem,
)


class TestFacade:
    def test_should_sum_numbers_when_number_systems_given(self) -> None:
        number_1 = 3.99
        number_2 = 4.58

        facade = Facade(IntSystem(), FloatSystem(), DecimalSystem())

        assert facade.sum_everything(number_1, number_2) == {
            "int": 7,
            "float": 8.57,
            "decimal": Decimal("8.570000000000000284217094304"),
        }
