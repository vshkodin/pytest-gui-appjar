from lib.tools.configManager import configPytest

class SettingsView:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("Settings", title='Settings', modal=True)
        self.app.addLabel("CurrentTestPath", f"TestPath : {configPytest.get('pytest','testpaths')}", 0, 0)
        self.app.addLabel("CurrentAddopts", f"Addopts : {configPytest.get('pytest','addopts')}", 1, 0)
        self.app.addLabel("CurrentBaseUrl", f"BaseUrl : {configPytest.get('pytest','baseurl')}", 2, 0)
        self.app.addLabel("CurrentChromedriverPath", f"ChromedriverPath : {configPytest.get('pytest','chromedriverpath')}", 3, 0)
        #self.app.addLabel("testPath", "Tests path", 4, 0)
        self.app.addButtons(["modify Paths",],self.update, 0, 1)
        #self.app.addLabel("addoptsLabel", "Addopts", 5, 0)
        self.app.addButtons(["modify Addops", ], self.update, 1, 1)
        #self.app.addLabel("BaseUrlLabel", "Base Url", 6, 0)
        self.app.addButtons(["modify BaseUrl", ], self.update, 2, 1)
        #self.app.addLabel("ChromedriverPathLabel", "ChromedriverPath", 7, 0)
        self.app.addButtons(["modify ChromedriverPath", ], self.update, 3, 1)
        self.app.addButtons(["Close"], self.press, 4, 0, 2)
        self.app.setSize(350, 150)
        self.app.stopSubWindow()

    def update(self,button):
        if button== "modify Paths":
            reply=self.app.textBox("Update value", f"Update testpath")
            if reply is not None:
                configPytest.set('pytest', 'testpaths', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentTestPath", f"TestPath : {configPytest.get('pytest', 'testpaths')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")
        elif button== "modify Addops":
            reply=self.app.textBox("Update value", f"Update Addopts")
            if reply is not None:
                configPytest.set('pytest', 'addopts', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentAddopts", f"Addopts : {configPytest.get('pytest', 'addopts')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")

        elif button == "modify BaseUrl":
            reply = self.app.textBox("Update value", f"Update BaseUrl")
            if reply is not None:
                configPytest.set('pytest', 'baseurl', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentBaseUrl", f"BaseUrl : {configPytest.get('pytest','baseurl')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")

        elif button == "modify ChromedriverPath":
            reply = self.app.textBox("Update value", f"Update ChromedriverPath")
            if reply is not None:
                configPytest.set('pytest', 'chromedriverpath', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentChromedriverPath", f"ChromedriverPath : {configPytest.get('pytest', 'chromedriverpath')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")



    def press(self, button):
        if button == "Close":
            self.app.hideSubWindow("Settings")
