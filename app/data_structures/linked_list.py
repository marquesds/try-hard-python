from __future__ import annotations

from typing import Any, Optional


class Node:
    def __init__(
        self, value: Any, left: Optional[Node] = None, right: Optional[Node] = None
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class DoubleLinkedList:
    def __init__(self, item: Optional[Any] = None) -> None:
        self.head = Node(item) if item else None

    def add(self, item: Any) -> None:
        if not self.head:
            self.head = Node(item)
        else:
            current = self.head
            self.head = Node(item)
            current.left = self.head
            self.head.right = current

    def pop(self) -> None:
        if not self.head:
            raise RuntimeError("Empty list")
        else:
            cursor = self.head
            while True:
                if cursor.right is None:
                    if cursor.left is None:
                        self.head = None
                    else:
                        cursor.left.right = None
                    break
                cursor = cursor.right
