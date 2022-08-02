from app.design_patterns.structural.bridge import (
    show_linux_user_folder,
    show_windows_user_folder,
)


class TestBridge:
    def test_should_show_windows_user_folder_when_using_windows_implementation(self):
        assert show_windows_user_folder() == "C:/Users/lucas"

    def test_should_show_linux_user_folder_when_using_linux_implementation(self):
        assert show_linux_user_folder() == "/home/lucas"
