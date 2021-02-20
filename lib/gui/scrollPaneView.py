from lib.tools.testParser import Parser


class ScrollPaneView:
    def __init__(self,app):
        self.app=app
        try:self.app.removeScrollPane("PANE")
        except:pass
        self.app.startScrollPane("PANE",0)
        app.setBg("grey")
        list_tests = Parser()
        for k, i in enumerate(list_tests.collect_tests()):
            self.app.addNamedCheckBox(i, i)
        self.app.stopScrollPane()