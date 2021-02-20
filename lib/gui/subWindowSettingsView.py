from lib.tools.configManager import configPytest
from .settingsLogic import settingsLogic
class SettingsView:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("Settings", title='Settings', modal=True)
        self.app.addLabel("CurrentTestPath", f"TestPath : {configPytest.get('pytest','testpaths')}", 0, 0)
        self.app.addLabel("CurrentAddopts", f"Addopts : {configPytest.get('pytest','addopts')}", 1, 0)
        self.app.addLabel("CurrentBaseUrl", f"BaseUrl : {configPytest.get('pytest','baseurl')}", 2, 0)
        self.app.addLabel("CurrentChromedriverPath", f"ChromedriverPath : {configPytest.get('pytest','chromedriverpath')}", 3, 0)
        self.app.addButtons(["modify Paths",],self.update, 0, 1)
        self.app.addButtons(["modify Addops", ], self.update, 1, 1)
        self.app.addButtons(["modify BaseUrl", ], self.update, 2, 1)
        self.app.addButtons(["modify ChromedriverPath", ], self.update, 3, 1)
        self.app.addButtons(["Close"], self.press, 4, 0, 2)
        self.app.setSize(350, 150)
        self.app.stopSubWindow()


    def update(self,button):
        settingsLogic(self.app,button)


    def press(self, button):
        if button == "Close":
            self.app.hideSubWindow("Settings")
