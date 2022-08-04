from app.design_patterns.structural.proxy import ProxyDatabaseDriver, RealDatabaseDriver


class TestProxy:
    def test_should_return_database_name_when_user_has_access(self) -> None:
        proxy_driver = ProxyDatabaseDriver(RealDatabaseDriver(), True)
        assert proxy_driver.database_name() == "awesome_database"

    def test_should_not_return_database_name_when_user_has_not_access(self) -> None:
        proxy_driver = ProxyDatabaseDriver(RealDatabaseDriver(), False)
        assert proxy_driver.database_name() == None
