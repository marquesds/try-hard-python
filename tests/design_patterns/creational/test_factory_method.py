from app.design_patterns.creational.factory_method import (
    deliver_by_car,
    deliver_by_motorcycle,
)


class TestFactoryMethod:
    def test_should_deliver_by_car_when_using_car_creator(self) -> None:
        assert deliver_by_car() == "Delivering by car"

    def test_should_deliver_by_motorcycle_when_using_motorcycle_creator(self) -> None:
        assert deliver_by_motorcycle() == "Delivering by motorcycle"
