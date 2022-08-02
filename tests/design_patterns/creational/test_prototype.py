import copy

from app.design_patterns.creational.prototype import StackOverflowAnswer


class TestPrototype:
    def test_should_clone_object_with_all_its_attributes(self):
        expected_object = StackOverflowAnswer("<h1>this answer is right</h1>", True)
        result_object = copy.copy(expected_object)

        assert expected_object.code == result_object.code
        assert expected_object.is_correct == result_object.is_correct
