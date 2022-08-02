"""
Bridge:
    Lets you split a large class or a set of closely related classes
    into two separate hierarchies — abstraction and implementation — which
    can be developed independently of each other.

See: https://refactoring.guru/design-patterns/bridge
"""

from typing import Protocol


class ServerPresenter(Protocol):
    """
    All this file's presenters are considered "interfaces/abstractions"; not following
    the OOP concept about it, but thinking about an user interacting with a system
    (like an app, website, etc).
    """

    def show_user_folder(self) -> str:
        ...


class OperatingSystem:
    """
    All this file's OS are considered the "implementations" because the "interface"
    will call it to show the results to the user.
    """

    def get_user_folder(self) -> str:
        ...


class WebsiteServerPresenter:
    def __init__(self, os: OperatingSystem) -> None:
        self.os = os

    def show_user_folder(self) -> str:
        return self.os.get_user_folder()


class Windows:
    def get_user_folder(self) -> str:
        return "C:/Users/lucas"


class Linux:
    def get_user_folder(self) -> str:
        return "/home/lucas"


def show_windows_user_folder():
    return WebsiteServerPresenter(Windows()).show_user_folder()


def show_linux_user_folder():
    return WebsiteServerPresenter(Linux()).show_user_folder()
