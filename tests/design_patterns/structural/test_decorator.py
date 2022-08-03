from app.design_patterns.structural.decorator import (
    DarkRoast,
    Decaf,
    Expresso,
    Milk,
    Mocha,
    Soy,
)


class TestDecorator:
    def test_should_get_dark_roast_total_price_when_adding_single_condiment(self) -> None:
        assert Milk(DarkRoast()).cost() == 298

    def test_should_get_dark_roast_total_price_when_adding_two_condiment(self) -> None:
        assert Mocha(Milk(DarkRoast())).cost() == 497

    def test_should_get_dark_roast_total_price_when_adding_three_condiment(self) -> None:
        assert Soy(Mocha(Milk(DarkRoast()))).cost() == 846

    def test_should_get_decaf_total_price_when_adding_single_condiment(self) -> None:
        assert Milk(Decaf()).cost() == 398

    def test_should_get_decaf_total_price_when_adding_two_condiment(self) -> None:
        assert Mocha(Milk(Decaf())).cost() == 597

    def test_should_get_decaf_total_price_when_adding_three_condiment(self) -> None:
        assert Soy(Mocha(Milk(Decaf()))).cost() == 946

    def test_should_get_espresso_total_price_when_adding_single_condiment(self) -> None:
        assert Milk(Expresso()).cost() == 198

    def test_should_get_espresso_total_price_when_adding_two_condiment(self) -> None:
        assert Mocha(Milk(Expresso())).cost() == 397

    def test_should_get_espresso_total_price_when_adding_three_condiment(self) -> None:
        assert Soy(Mocha(Milk(Expresso()))).cost() == 746
