from app.design_patterns.structural.composite import (
    BiologySubject,
    Composite,
    get_biology_subject,
    get_programming_subjects,
)


class TestComposite:
    def test_should_is_composite_be_false_when_leaf_object(self) -> None:
        assert BiologySubject().is_composite() == False

    def test_should_is_composite_be_true_when_composite_object(self) -> None:
        assert Composite().is_composite() == True

    def test_should_add_component_when_composite_object(self) -> None:
        obj1 = Composite()
        obj2 = Composite()
        obj1.add(obj2)

        assert len(obj1._children) == 1
        assert obj1._children[0] == obj2

    def test_should_remove_component_when_composite_object(self) -> None:
        obj1 = Composite()
        obj2 = Composite()
        obj1.add(obj2)

        assert len(obj1._children) == 1
        assert obj1._children[0] == obj2

        obj1.remove(obj2)

        assert len(obj1._children) == 0

    def test_should_get_one_subject_when_leaf(self) -> None:
        assert get_biology_subject() == "Biology"

    def test_should_get_all_children_subjects_when_composite(self) -> None:
        assert get_programming_subjects() == (
            "Programming, OOP, SOLID, Single Responsibility Principle, Open/Closed Principle, "
            "Liskov Substitution Principle, Interface Segregation Principle, Dependency Inversion Principle"
        )
