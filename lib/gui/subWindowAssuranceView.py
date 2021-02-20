class AssuranceView:
    def __init__(self,app):
        self.app=app
        self.app.startSubWindow("Assurance", title='Assurance', modal=True)
        self.app.addLabel("info", "Are you sure?", 0, 0)

        self.app.addButtons(["Yes", "No"], self.press, 1, 0, 2)
        self.app.setSize(200, 200)
        self.app.stopSubWindow()

    def press(self, button):
        if button == "Yes":
            self.app.hideSubWindow("Assurance")
            self.app.showSubWindow('Settings')
            self.app.YesNoStatus=True
        elif button == "No":
            self.app.hideSubWindow("Assurance")
            self.app.showSubWindow('Settings')
            self.app.YesNoStatus=False
