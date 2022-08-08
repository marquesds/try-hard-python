"""
Iterator:
    Lets you traverse elements of a collection without exposing
    its underlying representation (list, stack, tree, etc.).
    
See: https://refactoring.guru/design-patterns/iterator
"""
from __future__ import annotations

from typing import Optional


class LinkedListIterator:
    def __init__(self, head: Optional[LinkedList]) -> None:
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    def __next__(self) -> LinkedList:
        if not self.current:
            raise StopIteration
        else:
            item = self.current
            self.current = self.current.node
            return item


class LinkedList:
    def __init__(self, value: str, node: Optional[LinkedList] = None) -> None:
        self.value = value
        self.node = node

    def __iter__(self) -> LinkedListIterator:
        return LinkedListIterator(self)
