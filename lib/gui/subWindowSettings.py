

class Settings:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("Settings", title='Settings', modal=True)
        # app.addLabel("settingsLable", "")
        self.app.startLabelFrame("Login Details")
        # these only affect the labelFrame
        self.app.setSticky("ew")
        self.app.addLabel("l1", "Name", 0, 0)
        self.app.addEntry("Name", 0, 1)
        self.app.addLabel("l2", "Password", 1, 0)
        self.app.addEntry("Password", 1, 1)
        self.app.addButtons(["Submit", "Cancel"], None, 2, 0, 2)
        self.app.stopLabelFrame()
        # app.addNamedCheckBox(i, i)
        self.app.setSize(400, 400)

        self.app.stopSubWindow()