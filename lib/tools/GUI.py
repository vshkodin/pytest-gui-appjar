from lib.tools.running import RUN
from lib.tools.directoryCleaning import reports_cleaning
from lib.tools.testParser import Parser
from appJar import gui
from config import GUI
import subprocess, os, re, sys

counter=0

def run_GUI():
    global app,counter
    app = gui("Pytest GUI", "800x600")
    app.setBg("white")
    app.setFont(12)
    app.startScrollPane("PANE")
    list_tests=Parser()
    for k, i in enumerate (list_tests.collect_tests()):
        app.addNamedCheckBox(i, i)
    app.stopScrollPane()
    app.addButtons(["Run tests", "Run reports", "Clear reports directory", "EXIT"], press)
    app.startTabbedFrame("TabbedFrame")
    app.startTab("OUTPUT")
    app.addLabel("test_results", "")
    app.stopTab()
    app.stopTabbedFrame()
    app.go()

def press(button):
    global app, counter
    if button == "EXIT":
        app.stop()

    elif button=="Run reports":
        subprocess.Popen(["allure","serve","reports"])

    elif button=="Clear reports directory":
        reports_cleaning()

    elif button=="Run tests":
        reports_cleaning()
        l=app.getAllCheckBoxes()
        markedListOfTests=""
        for i in (l):
            if l[i] == True:
                markedListOfTests= markedListOfTests +" "+str(i)
        os.system('pytest'+markedListOfTests+" > out.txt")
        with open("out.txt") as file:
            for string in file:
                pass
        os.remove("out.txt")
        app.setLabel("test_results", string)
