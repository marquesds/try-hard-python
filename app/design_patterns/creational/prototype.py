"""
Prototype:
    Lets you copy existing objects without making your code dependent on their classes.
    
See: https://refactoring.guru/design-patterns/prototype
"""
from __future__ import annotations  # enables using current class as returning type
import copy


class StackOverflowAnswer:
    def __init__(self, code: str, is_correct: bool) -> None:
        self.code = code
        self.is_correct = is_correct

    def __clone__(self) -> StackOverflowAnswer:
        new_code = copy.copy(self.code)
        new_is_correct = copy.copy(self.is_correct)

        new_answer = self.__class__(new_code, new_is_correct)
        return new_answer
