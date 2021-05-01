from PySide2.QtWidgets import QMainWindow, QSplitter, QMenuBar, QAction
from PySide2.QtCore import Qt
from PySide2.QtGui import QKeySequence
from pypyrokin import VERSION

TITLE = f'PyPyroKin {VERSION}'


class MainWindow(QMainWindow):
    def __init__(self, *, setup_input_panel=None):
        super().__init__()
        self.setup_input_panel = setup_input_panel

        self.main_widget = None
        self.menu_bar = None
        self.new_menu_action = None

        self.setup_ui()
        self.setWindowTitle(TITLE)

    def setup_ui(self):
        self.main_widget = QSplitter(Qt.Horizontal)
        self.setCentralWidget(self.main_widget)

        self.main_widget.addWidget(self.setup_input_panel)

        self.create_menu_bar()

    def create_menu_bar(self):
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        self.create_file_menu()

    def create_file_menu(self):
        file_menu = self.menu_bar.addMenu('&File')

        self.new_menu_action = QAction('New', self)
        self.new_menu_action.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_N))

        file_menu.addAction(self.new_menu_action)
