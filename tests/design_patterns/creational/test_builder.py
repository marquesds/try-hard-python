from app.design_patterns.creational.builder import User, UserBuilder


class TestBuilder:
    def test_should_build_user_with_all_attributes_when_adding_them_all(self) -> None:
        expected_user = User("Lucas", 31, "99999999999", "Test address")
        result_user = (
            UserBuilder()
            .add_name("Lucas")
            .add_age(31)
            .add_phone("99999999999")
            .add_address("Test address")
            .build()
        )

        assert expected_user.name == result_user.name
        assert expected_user.age == result_user.age
        assert expected_user.phone == result_user.phone
        assert expected_user.address == result_user.address

    def test_should_build_user_one_attribute(self) -> None:
        expected_user = User("Lucas")
        result_user = UserBuilder().add_name("Lucas").build()

        assert expected_user.name == result_user.name
        assert expected_user.age == 1
        assert expected_user.phone == ""
        assert expected_user.address == ""

    def test_should_build_user_two_attributes(self) -> None:
        expected_user = User("Lucas", 31)
        result_user = UserBuilder().add_name("Lucas").add_age(31).build()

        assert expected_user.name == result_user.name
        assert expected_user.age == result_user.age
        assert expected_user.phone == ""
        assert expected_user.address == ""

    def test_should_build_user_three_attributes(self) -> None:
        expected_user = User("Lucas", 31, "99999999999")
        result_user = UserBuilder().add_name("Lucas").add_age(31).add_phone("99999999999").build()

        assert expected_user.name == result_user.name
        assert expected_user.age == result_user.age
        assert expected_user.phone == result_user.phone
        assert expected_user.address == ""

    def test_should_build_empty_object_when_no_given_attribute(self) -> None:
        result_user = UserBuilder().build()

        assert result_user.name == ""
        assert result_user.age == 1
        assert result_user.phone == ""
        assert result_user.address == ""
