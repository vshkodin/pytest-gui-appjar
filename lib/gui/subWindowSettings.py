from .configManager import configPytest

class Settings:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("Settings", title='Settings', modal=True)
        # app.addLabel("settingsLable", "")
        #self.app.startLabelFrame("Settings")
        # these only affect the labelFrame
        #self.app.setSticky("ew")

        self.app.addLabel("CurrentTestPath", f"Current testPath : {configPytest.get('pytest','testpaths')}", 0, 0)
        self.app.addLabel("testPath", "Tests path", 1, 0)
        self.app.addEntry("testPathField", 1, 1)
        self.app.setEntryDefault("testPathField", configPytest.get('pytest','testpaths'))
        #self.app.addLabel("l2", "Password", 1, 0)
        #self.app.addEntry("Password", 1, 1)
        self.app.addButtons(["Update", "Close"], self.press, 2, 0, 2)
        #self.app.stopLabelFrame()
        # app.addNamedCheckBox(i, i)
        self.app.setSize(400, 400)
        self.app.stopSubWindow()

    def press(self, button):

        if button == "Update":
            oldPath = configPytest.get('pytest', 'testpaths')
            new= self.app.getEntry("testPathField")
            if oldPath != new:
                configPytest.set('pytest', 'testpaths', new)
                with open('pytest.ini', 'w') as f:
                    configPytest.write(f)
                self.app.setLabel("CurrentTestPath", f"Current testPath : {configPytest.get('pytest','testpaths')}")
                self.app.setEntryDefault("testPathField",  configPytest.get('pytest','testpaths'))
                #self.app.hideSubWindow("Settings")
                #self.app.showSubWindow("Settings")


        elif button == "Close":
            self.app.hideSubWindow("Settings")
