from app.design_patterns.creational.singleton import UniverseAnswer


class TestSingleton:
    def test_should_get_same_id_when_same_instance(self):
        expected_answer = UniverseAnswer()
        result_answer = UniverseAnswer()

        assert id(expected_answer) == id(result_answer)
        assert expected_answer.answer() == result_answer.answer()
