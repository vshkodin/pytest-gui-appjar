import os,subprocess
from datetime import datetime
from config import now,log



class ControlButtons:
    def __init__(self,app):
        self.app=app
        self.app.addButtons(["Run All", "Run selected", "See Report", "Settings", "EXIT"], self.press)

    def press(self, button):
        if button == "EXIT":
            log.info(f' exit from app: {now}')
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')
            self.app.stop()

        elif button == "See Report":
            subprocess.Popen(["allure", "serve", "reports"])

        elif button == "Settings":
            # app.setLabel("settingsLable", "PlaceHolder")
            self.app.showSubWindow(button)

        elif button == "Clear reports directory":
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')

        elif button == "Run selected":
            log.info(f' test run : {now}')
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')
            l = self.app.getAllCheckBoxes()
            markedListOfTests = ""
            for i in (l):
                if l[i] == True:
                    markedListOfTests = markedListOfTests + " " + str(i)
            os.system('pytest --alluredir=reports ' + markedListOfTests + " > out.txt")
            with open("out.txt") as file:
                for string in file:
                    pass
            os.remove("out.txt")
            self.app.setLabel("test_results", string)

        elif button == "Run All":
            log.info(f' test run : {now}')
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')
            os.system('pytest --alluredir=reports  > out.txt')
            with open("out.txt") as file:
                for string in file:
                    pass
            os.remove("out.txt")
            self.app.setLabel("test_results", string)