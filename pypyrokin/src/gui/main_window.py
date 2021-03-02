from PySide2.QtWidgets import QMainWindow, QSplitter
from PySide2.QtCore import Qt
from pypyrokin import VERSION

TITLE = f'PyPyroKin {VERSION}'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = None

        self.setup_ui()
        self.setWindowTitle(TITLE)

    def setup_ui(self):
        self.main_widget = QSplitter(Qt.Horizontal)
