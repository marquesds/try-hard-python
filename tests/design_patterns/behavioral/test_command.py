from app.design_patterns.behavioral.command import (
    execute_copy_command,
    execute_paste_command,
)


class TestCommand:
    def test_should_execute_copy_command_when_using_copy_function(self) -> None:
        assert execute_copy_command() == "Text Lorem Ipsum copied to clipboard."

    def test_should_execute_paste_command_when_using_paste_function(self) -> None:
        assert execute_paste_command() == "Lorem Ipsum"
