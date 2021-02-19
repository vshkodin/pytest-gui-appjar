from .controlButtonsMainMenu import ControlButtonsClass


class ControlButtons:
    def __init__(self, app):
        self.app = app
        self.app.addButtons(["Run All", "Run selected", "Collect tests",
                             "See Report", "Create test", "Edit test", "Settings",
                             "EXIT"], self.press)

    def press(self, button):
        ControlButtonsClass(self.app, button)
