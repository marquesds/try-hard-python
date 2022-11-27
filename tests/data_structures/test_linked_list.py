from app.data_structures.linked_list import DoubleLinkedList


class TestDoubleLinkedList:
    def test_should_add_head_element_through_constructor_when_head_is_none(self) -> None:
        linked_list = DoubleLinkedList(1)
        assert linked_list.head.value == 1
        assert linked_list.head.left is None
        assert linked_list.head.right is None

    def test_should_add_head_element_through_method_add_when_head_is_none(self) -> None:
        linked_list = DoubleLinkedList()
        linked_list.add(1)
        assert linked_list.head.value == 1
        assert linked_list.head.left is None
        assert linked_list.head.right is None

    def test_should_add_node_when_head_exists(self) -> None:
        linked_list = DoubleLinkedList(1)
        linked_list.add(2)
        assert linked_list.head.value == 2
        assert linked_list.head.right.value == 1
        assert linked_list.head.right.left.value == 2

    def test_should_pop_last_element_from_list_with_size_one(self) -> None:
        linked_list = DoubleLinkedList(1)
        linked_list.pop()
        assert linked_list.head is None

    def test_should_pop_last_element_from_multisized_list(self) -> None:
        linked_list = DoubleLinkedList(1)
        linked_list.add(2)
        linked_list.add(3)
        assert linked_list.head.value == 3
        assert linked_list.head.right.value == 2
        assert linked_list.head.right.right.value == 1

        linked_list.pop()
        assert linked_list.head.value == 3
        assert linked_list.head.right.value == 2
        assert linked_list.head.right.right is None

        linked_list.pop()
        assert linked_list.head.value == 3
        assert linked_list.head.right is None

        linked_list.pop()
        assert linked_list.head is None
