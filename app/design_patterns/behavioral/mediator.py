"""
Mediator:
    Lets you reduce chaotic dependencies between objects. 
    The pattern restricts direct communications between the objects
    and forces them to collaborate only via a mediator object.
    
See: https://refactoring.guru/design-patterns/mediator
"""
from typing import Protocol


class NotificationComponent(Protocol):
    def send(self, message: str) -> str:
        ...


class Mediator(Protocol):
    def notify(self, sender: NotificationComponent, event: str) -> str:
        ...


class EmailNotificationComponent:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def send(self, message: str) -> str:
        self.mediator.notify(self, "email")
        return message


class SMSNotificationComponent:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def send(self, message: str) -> str:
        self.mediator.notify(self, "sms")
        return message


class NotificationMediator:
    def __init__(self, email: EmailNotificationComponent, sms: SMSNotificationComponent):
        self.email = email
        self.sms = sms

    def notify(self, sender: NotificationComponent, event: str) -> str:
        if event == "email":
            return self.email.send("asdf")

