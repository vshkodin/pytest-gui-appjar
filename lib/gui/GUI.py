from lib.gui.running import RUN
from lib.gui.testParser import Parser
from appJar import gui
from config import GUI,Allure_GUI
import subprocess, os, re, sys
import logging
from datetime import datetime
logging.basicConfig(filename='myapp.log', level=logging.INFO)
now = datetime.now()

def run_GUI():
    global app

    # create a GUI variable called
    logging.info(f' app starts att: {now}')
    app = gui("Pytest GUI", "900x600")
    app.setBg("white")
    app.setFont(12)

    # MAIN FRAME (STRAT)
    app.startFrame("MAIN")


    # HEAD
    app.startFrame("HEAD", row=1, column=0)
    #scroll Pane
    app.startScrollPane("PANE")
    app.setBg("grey")
    list_tests=Parser()
    for k, i in enumerate (list_tests.collect_tests()):
        app.addNamedCheckBox(i, i)
    app.stopScrollPane()
    app.stopFrame()


    # MIDDLE FRAME
    app.startFrame("MIDDLE", row=2)
    app.addButtons(["Run All", "Run selected", "See Report", "Settings", "EXIT"], press)
    app.stopFrame()


    # results section TabbedFrame
    app.startTabbedFrame("TabbedFrame")
    app.startTab("OUTPUT")
    app.addLabel("test_results", "")
    app.stopTab()
    app.stopTabbedFrame()


    # settings pop-up
    app.startSubWindow("Settings",title='Settings', modal=True)
    app.addLabel("settingsLable", "")
    app.setSize(400, 400)

    app.stopSubWindow()


    # MAIN FRAME STOP
    app.stopFrame()

    #STRAT APP
    app.go()


def press(button):
    if button == "EXIT":
        logging.info(f' exit from app: {now}')
        os.system('rm -r reports')
        logging.info(f' cleaning report : {now}')
        app.stop()

    elif button == "See Report":
        subprocess.Popen(["allure","serve","reports"])

    elif button=="Settings":
        app.setLabel("settingsLable", "JOPA")
        app.showSubWindow(button)

    elif button=="Clear reports directory":
        os.system('rm -r reports')
        logging.info(f' cleaning report : {now}')

    elif button=="Run selected":
        logging.info(f' test run : {now}')
        os.system('rm -r reports')
        logging.info(f' cleaning report : {now}')
        l=app.getAllCheckBoxes()
        markedListOfTests=""
        for i in (l):
            if l[i] == True:
                markedListOfTests= markedListOfTests +" "+str(i)
        if Allure_GUI: os.system('pytest --alluredir=reports '+markedListOfTests+" > out.txt")
        else: os.system('pytest '+markedListOfTests+" > out.txt")
        with open("out.txt") as file:
            for string in file:
                pass
        os.remove("out.txt")
        app.setLabel("test_results", string)

    elif button=="Run All":
        logging.info(f' test run : {now}')
        os.system('rm -r reports')
        logging.info(f' cleaning report : {now}')
        os.system('pytest --alluredir=reports  > out.txt')
        with open("out.txt") as file:
            for string in file:
                pass
        os.remove("out.txt")
        app.setLabel("test_results", string)