class QuitBus:
    def execute(self):
        self.parent.run = False


quitbus = QuitBus()
