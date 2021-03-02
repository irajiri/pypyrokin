from src.gui.main_window import MainWindow


class Gui:
    def __init__(self):
        super().__init__()
        self.main_window = MainWindow()

    def show(self):
        self.main_window.showMaximized()
