from lib.gui.running import RUN
from appJar import gui
from config import GUI,Allure_GUI
import subprocess, os, re, sys
import logging
from datetime import datetime
logging.basicConfig(filename='myapp.log', level=logging.INFO)
now = datetime.now()
from .scrollPane import ScrollPane
from .subWindowSettings import Settings
from .tabbedFrameTestResults import TestResults

class Gui:
    def __init__(self):
        self.app = gui("Pytest GUI", "900x600")
        logging.info(f' app starts att: {now}')
        self.app.setBg("white")
        self.app.setFont(12)
        ScrollPane(self.app)
        self.app.addButtons(["Run All", "Run selected", "See Report", "Settings", "EXIT"], self.press)
        TestResults(self.app)
        Settings(self.app)
        self.app.go()


    def press(self,button):
        if button == "EXIT":
            logging.info(f' exit from app: {now}')
            os.system('rm -r reports')
            logging.info(f' cleaning report : {now}')
            self.app.stop()

        elif button == "See Report":
            subprocess.Popen(["allure","serve","reports"])

        elif button=="Settings":
            #app.setLabel("settingsLable", "PlaceHolder")
            self.app.showSubWindow(button)

        elif button=="Clear reports directory":
            os.system('rm -r reports')
            logging.info(f' cleaning report : {now}')

        elif button=="Run selected":
            logging.info(f' test run : {now}')
            os.system('rm -r reports')
            logging.info(f' cleaning report : {now}')
            l=self.app.getAllCheckBoxes()
            markedListOfTests=""
            for i in (l):
                if l[i] == True:
                    markedListOfTests= markedListOfTests +" "+str(i)
            os.system('pytest --alluredir=reports '+markedListOfTests+" > out.txt")
            with open("out.txt") as file:
                for string in file:
                    pass
            os.remove("out.txt")
            self.app.setLabel("test_results", string)

        elif button=="Run All":
            logging.info(f' test run : {now}')
            os.system('rm -r reports')
            logging.info(f' cleaning report : {now}')
            os.system('pytest --alluredir=reports  > out.txt')
            with open("out.txt") as file:
                for string in file:
                    pass
            os.remove("out.txt")
            self.app.setLabel("test_results", string)