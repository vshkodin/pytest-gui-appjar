from lib.tools.configManager import configPytest

class settingsLogic:
    def __init__(self,app,button):
        self.app=app
        self.button=button
        self.execute()

    def execute(self):
        if self.button == "modify Paths":
            reply = self.app.textBox("Update value", f"Update testpath")
            if reply is not None:
                configPytest.set('pytest', 'testpaths', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentTestPath", f"TestPath : {configPytest.get('pytest', 'testpaths')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")
        elif self.button == "modify Addops":
            reply = self.app.textBox("Update value", f"Update Addopts")
            if reply is not None:
                configPytest.set('pytest', 'addopts', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentAddopts", f"Addopts : {configPytest.get('pytest', 'addopts')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")

        elif self.button == "modify BaseUrl":
            reply = self.app.textBox("Update value", f"Update BaseUrl")
            if reply is not None:
                configPytest.set('pytest', 'baseurl', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentBaseUrl", f"BaseUrl : {configPytest.get('pytest', 'baseurl')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")

        elif self.button == "modify ChromedriverPath":
            reply = self.app.textBox("Update value", f"Update ChromedriverPath")
            if reply is not None:
                configPytest.set('pytest', 'chromedriverpath', reply)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentChromedriverPath",
                                  f"ChromedriverPath : {configPytest.get('pytest', 'chromedriverpath')}")
                self.app.showSubWindow("Settings")
            else:
                self.app.showSubWindow("Settings")
