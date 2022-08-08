from app.design_patterns.behavioral.iterator import LinkedList


class TestIterator:
    def test_should_create_linked_list_when_single_element_given(self):
        linked_list = LinkedList("1")
        for item in linked_list:
            assert item.value == "1"

    def test_should_create_linked_list_when_multiple_elements_given(self):
        linked_list = LinkedList("1", LinkedList("2", LinkedList("3", LinkedList("4"))))
        # traverses the entire list, asserting each value
        for i, item in enumerate(linked_list):
            assert item.value == str(i + 1)
