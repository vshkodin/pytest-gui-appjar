from .configManager import configPytest

class Settings:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("Settings", title='Settings', modal=True)
        self.app.addLabel("CurrentTestPath", f" Current testPath : {configPytest.get('pytest','testpaths')}", 0, 0)
        self.app.addLabel("CurrentAddopts", f" Current addopts : {configPytest.get('pytest','addopts')}", 1, 0)
        self.app.addLabel("CurrentBaseUrl", f" Current Base Url : {configPytest.get('pytest','baseurl')}", 2, 0)
        self.app.addLabel("testPath", "Tests path", 3, 0)
        self.app.addButtons(["modify Paths",],self.update, 3, 1)
        self.app.addLabel("addoptsLabel", "Addopts", 4, 0)
        self.app.addButtons(["modify Addops", ], self.update, 4, 1)
        self.app.addLabel("BaseUrlLabel", "Base Url", 5, 0)
        self.app.addButtons(["modify BaseUrl", ], self.update, 5, 1)
        self.app.addButtons(["Close"], self.press, 6, 0, 2)
        self.app.setSize(400, 400)
        self.app.stopSubWindow()

    def update(self,button):
        if button== "modify Paths":
            reply=self.app.textBox("Update value", f"Update testpath")
            if reply is not None:
                configPytest.set('pytest', 'testpaths', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentTestPath", f" Current testPath : {configPytest.get('pytest', 'testpaths')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")
        elif button== "modify Addops":
            reply=self.app.textBox("Update value", f"Update Addopts")
            if reply is not None:
                configPytest.set('pytest', 'addopts', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentAddopts", f" Current addopts : {configPytest.get('pytest', 'addopts')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")

        elif button == "modify BaseUrl":
            reply = self.app.textBox("Update value", f"Update BaseUrl")
            if reply is not None:
                configPytest.set('pytest', 'baseurl', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentBaseUrl", f" Current Base Url : {configPytest.get('pytest','baseurl')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")
    def press(self, button):
        if button == "Close":
            self.app.hideSubWindow("Settings")
