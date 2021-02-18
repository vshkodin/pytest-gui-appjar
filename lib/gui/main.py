from lib.gui.running import RUN
from appJar import gui
from config import GUI,Allure_GUI, now,log


from .scrollPane import ScrollPane
from .subWindowSettings import Settings
from .tabbedFrameTestResults import TestResults
from .controlButtons import ControlButtons


class Gui:
    def __init__(self):
        self.app = gui("Pytest GUI", "900x600")
        log.info(f' app starts att: {now}')
        self.app.setBg("white")
        self.app.setFont(12)
        ScrollPane(self.app)
        ControlButtons(self.app)
        TestResults(self.app)
        Settings(self.app)
        self.app.go()