from appJar import gui
from .scrollPaneView import ScrollPaneView
from .subWindowSettingsView import SettingsView
from .tabbedFrameTestResultsView import TestResultsView
from .controlButtonsView import ControlButtonsView
from lib.tools.log import log
#from .subWindowChooseKindofTestView import ChooseKindofTestView


class Gui:
    def __init__(self):
        self.app = gui("Pytest GUI", "900x600")
        log.info('app starts')
        self.app.setBg("white")
        self.app.setFont(12)
        ScrollPaneView(self.app)
        ControlButtonsView(self.app)
        TestResultsView(self.app)
        SettingsView(self.app)
        #ChooseKindofTestView(self.app)
        self.app.go()