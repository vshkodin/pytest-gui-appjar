from lib.tools.testCollection import TestCollection


class ScrollPaneView:
    def __init__(self,app):
        self.app=app
        try:self.app.removeScrollPane("PANE")
        except:pass
        self.app.startScrollPane("PANE",0)
        app.setBg("grey")
        list_tests = TestCollection()
        for k, i in enumerate(list_tests.collect_tests()):
            if "run status" in i or "there are"in i:continue
            self.app.addNamedCheckBox(i, i)
        self.app.stopScrollPane()