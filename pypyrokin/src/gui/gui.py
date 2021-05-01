from src.gui.main_window import MainWindow
from src.gui.setup_input_panel import SetupInputPanel


class Gui:
    def __init__(self):
        super().__init__()
        self.setup_input_panel = SetupInputPanel()

        self.main_window = MainWindow(
            setup_input_panel=self.setup_input_panel
        )

    def show(self):
        self.main_window.showMaximized()
