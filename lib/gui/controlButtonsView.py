from .controlButtonsLogic import ControlButtonsLogic


class ControlButtonsView:
    def __init__(self, app):
        self.app = app
        self.app.addButtons(["Run All", "Run selected", "Collect tests",
                             "See Report", "Settings",
                             "EXIT"], self.press) #"Create test", "Edit test"

    def press(self, button):
        ControlButtonsLogic(self.app, button)
