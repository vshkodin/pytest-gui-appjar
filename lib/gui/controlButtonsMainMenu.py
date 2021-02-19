import os,subprocess
from .log import log, now
from .scrollPane import ScrollPane


class ControlButtonsClass:
    def __init__(self,app,button):
        self.app=app
        self.button=button
        self.execute()

    def execute(self):
        if self.button == "EXIT":
            log.info(f' exit from app: {now}')
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')
            self.app.stop()

        elif self.button == "Collect tests":
            ScrollPane(self.app)

        elif self.button == "Create test":
            self.app.showSubWindow('ChooseKindofTestWindow')

        elif self.button == "See Report":
            subprocess.Popen(["allure", "serve", "reports"])

        elif self.button == "Settings":
            self.app.showSubWindow(self.button)

        elif self.button == "Clear reports directory":
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')

        elif self.button == "Run selected":
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

        elif self.button == "Run All":
            log.info(f' test run : {now}')
            os.system('rm -r reports')
            log.info(f' cleaning report : {now}')
            os.system('pytest --alluredir=reports  > out.txt')
            with open("out.txt") as file:
                for string in file:
                    pass
            os.remove("out.txt")
            self.app.setLabel("test_results", string)