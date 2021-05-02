from PySide2.QtWidgets import QWidget, QVBoxLayout, QTabWidget


class PlotPanel(QWidget):
    def __init__(self, *, log=None):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.log = log

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(QWidget(), 'Plot tab')

        self.main_layout.addWidget(self.tab_widget, 4)
        self.main_layout.addWidget(self.log, 1)
