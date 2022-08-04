"""
Chain of Responsibility:
    Lets you pass requests along a chain of handlers.
    Upon receiving a request, each handler decides either to process
    the request or to pass it to the next handler in the chain.

See: https://refactoring.guru/design-patterns/chain-of-responsibility
"""
from __future__ import annotations

import abc
from typing import Optional, Protocol


class Handler:
    _next_handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: str) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class LengthHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if len(request) != 11:
            raise RuntimeError(f"{len(request)} is not a valid length for phone numbers.")
        return super().handle(request)


class IsNumberHandler(Handler):
    def handle(self, request: str) -> Optional[str]:
        if not request.isdigit():
            raise RuntimeError(f"{request} is not a valid phone number.")
        return super().handle(request)


def is_valid_phone_number(phone_number: str) -> bool:
    handler = Handler()
    length_handler = LengthHandler()
    is_number_handler = IsNumberHandler()

    length_handler.set_next(is_number_handler)
    handler.set_next(length_handler)

    try:
        handler.handle(phone_number)
    except RuntimeError as e:
        print(f"Error. Message: {str(e)}")
        return False
    return True
