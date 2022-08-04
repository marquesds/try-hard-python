from app.design_patterns.structural.flyweight import (
    Rectangle,
    RectangleFactory,
    RectangleFlyweight,
)


class TestFlyweight:
    def test_should_calculate_the_right_area(self):
        rectangle = Rectangle("BLUE", 5, 10)
        assert rectangle.area() == 50

    def test_shoud_create_rectangle_based_on_its_color(self):
        rectangle = RectangleFactory().create("BLACK")
        assert rectangle.color == "BLACK"

    def test_shoud_not_repeat_rectangle_creation_based_when_it_has_same_color(self):
        obj1 = RectangleFactory().create("BLACK")
        obj2 = RectangleFactory().create("BLACK")

        assert id(obj1) == id(obj2)

    def test_should_return_same_id_when_rectangle_has_same_color(self):
        rectangles = RectangleFlyweight(RectangleFactory()).rectangles(20)

        assert len(rectangles) == 20
        # This will ensure there will not be more rectangles than colors
        assert len(set(rectangles)) <= 5
