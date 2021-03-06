from src.gui.main_window import MainWindow
from src.gui.setup_input_panel import SetupInputPanel
from src.gui.plot_panel import PlotPanel
from src.gui.log import Log


class Gui:
    def __init__(self):
        super().__init__()
        self.setup_input_panel = SetupInputPanel()
        self.log = Log()
        self.plot_panel = PlotPanel(log=self.log)

        self.main_window = MainWindow(
            setup_input_panel=self.setup_input_panel,
            plot_panel=self.plot_panel
        )

    def show(self):
        self.main_window.showMaximized()
