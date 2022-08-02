from app.design_patterns.creational.abstract_factory import goblin_attack, orc_attack


class TestAbstractFactory:
    def test_should_call_globlin_attack_when_using_goblin_factory(self) -> None:
        assert goblin_attack() == "Goblin attack!"

    def test_should_call_orc_attack_when_using_orc_factory(self) -> None:
        assert orc_attack() == "Orc attack!"
