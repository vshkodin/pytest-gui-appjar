from .configManager import configPytest

class ChooseKindofTest:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("ChooseKindofTestWindow", title='Choose Kind of Test', modal=True)
        self.app.addLabel("infoChoose", "Place holder", 0, 0)
        self.app.addButtons(["API"], self.press, 1)
        self.app.addButtons(["Selenium"], self.press, 2)
        self.app.addButtons(["Appium"], self.press, 3)
        self.app.addButtons(["Back"], self.press, 4)
        #self.app.addButtons(["API", "Selenium", "Appium", "Back"], self.press, 1)
        self.app.setSize(200, 200)
        self.app.stopSubWindow()

    def press(self, button):
        if button == "API":
            self.app.hideSubWindow("ChooseKindofTestWindow")
        elif button == "Selenium":
            self.app.hideSubWindow("ChooseKindofTestWindow")
        elif button == "Appium":
            self.app.hideSubWindow("ChooseKindofTestWindow")
        elif button == "Back":
            self.app.hideSubWindow("ChooseKindofTestWindow")
