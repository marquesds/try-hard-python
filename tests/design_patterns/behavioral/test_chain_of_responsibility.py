import pytest

from app.design_patterns.behavioral.chain_of_responsibility import (
    IsNumberHandler,
    LengthHandler,
    is_valid_phone_number,
)


class TestChainOfResponsibility:
    def test_should_not_raise_error_when_valid_phone(self) -> None:
        valid_phone = "11955789014"
        assert is_valid_phone_number(valid_phone) == True

    def test_should_return_false_when_invalid_phone_length(self) -> None:
        valid_phone = "119557890140"
        assert is_valid_phone_number(valid_phone) == False

    def test_should_return_false_when_invalid_phone_length(self) -> None:
        invalid_phone = "119557890140"
        assert is_valid_phone_number(invalid_phone) == False

    def test_should_return_false_when_invalid_phone_number(self) -> None:
        invalid_phone = "A195578901Z"
        assert is_valid_phone_number(invalid_phone) == False

    def test_should_raise_error_when_invalid_phone_length(self) -> None:
        invalid_phone = "119557890140"
        with pytest.raises(RuntimeError) as e:
            LengthHandler().handle(invalid_phone)
        assert str(e.value) == "12 is not a valid length for phone numbers."

    def test_should_raise_error_when_invalid_phone_number(self) -> None:
        invalid_phone = "A195578901Z"
        with pytest.raises(RuntimeError) as e:
            IsNumberHandler().handle(invalid_phone)
        assert str(e.value) == "A195578901Z is not a valid phone number."
