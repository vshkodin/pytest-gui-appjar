import os,subprocess
from lib.tools.log import log
from lib.tools.cleanReports import clean_report
from lib.tools.resultsGetter import get_results
from lib.tools.testRunner import test_runner
from .scrollPaneView import ScrollPaneView



class ControlButtonsLogic:
    def __init__(self,app,button):
        self.app=app
        self.button=button
        self.execute()

    def execute(self):
        if self.button == "EXIT":
            log.info(f'exit from app')
            clean_report()
            self.app.stop()

        elif self.button == "Collect tests":
            ScrollPaneView(self.app)

        elif self.button == "Create test":
            self.app.showSubWindow('ChooseKindofTestWindow')

        elif self.button == "See Report":
            subprocess.Popen(["allure", "serve", "reports"])

        elif self.button == "Settings":
            self.app.showSubWindow(self.button)

        elif self.button == "Clear reports directory":
            clean_report()

        elif self.button == "Run selected":
            l = self.app.getAllCheckBoxes()
            test_runner([i for i in l if l[i]==True])
            self.app.setLabel("test_results", get_results())

        elif self.button == "Run All":
            test_runner()
            self.app.setLabel("test_results", get_results())