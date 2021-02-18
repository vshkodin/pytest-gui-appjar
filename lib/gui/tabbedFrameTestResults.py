class TestResults:
    def __init__(self,app):
        self.app=app
        self.app.startTabbedFrame("TabbedFrame")
        self.app.startTab("OUTPUT")
        self.app.addLabel("test_results", "")
        self.app.stopTab()
        self.app.stopTabbedFrame()