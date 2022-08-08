"""
Command:
    Turns a request into a stand-alone object that contains all information about the request.
    This transformation lets you pass requests as a method arguments,
    delay or queue a request's execution, and support undoable operations.

See: https://refactoring.guru/design-patterns/command
"""
from typing import Protocol


class Command(Protocol):
    def execute(self) -> str:
        ...


class CopyCommand:
    def __init__(self, copied_text: str) -> None:
        self.copied_text = copied_text

    def execute(self) -> str:
        return f"Text {self.copied_text} copied to clipboard."


class PasteCommand:
    def execute(self) -> str:
        return "Lorem Ipsum"


class Application:
    def execute(self, command: Command) -> str:
        return command.execute()


def execute_copy_command() -> str:
    command = CopyCommand("Lorem Ipsum")
    return command.execute()


def execute_paste_command() -> str:
    command = PasteCommand()
    return command.execute()
