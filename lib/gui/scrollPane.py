from lib.gui.testParser import Parser


class ScrollPane:
    def __init__(self,app):
        self.app=app
        self.app.startScrollPane("PANE")
        app.setBg("grey")
        list_tests = Parser()
        for k, i in enumerate(list_tests.collect_tests()):
            self.app.addNamedCheckBox(i, i)
        self.app.stopScrollPane()