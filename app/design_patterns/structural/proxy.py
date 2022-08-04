"""
Proxy:
    Lets you provide a substitute or placeholder for another object.
    A proxy controls access to the original object, allowing you to perform something
    either before or after the request gets through to the original object.

See: https://refactoring.guru/design-patterns/proxy
"""
from typing import Optional, Protocol


class DatabaseDriver(Protocol):
    def database_name(self) -> Optional[str]:
        ...


class RealDatabaseDriver:
    def database_name(self) -> Optional[str]:
        return "awesome_database"


class ProxyDatabaseDriver:
    def __init__(self, driver: RealDatabaseDriver, has_access: bool = True) -> None:
        self.driver = driver
        self.has_access = has_access

    def database_name(self) -> Optional[str]:
        if self.has_access:
            return self.driver.database_name()
        return None
