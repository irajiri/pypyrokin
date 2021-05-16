from src.gui.base import PlotWidget, Tab, TabWidget
from PySide2.QtWidgets import QWidget, QVBoxLayout, QTabWidget

class PlotPanel(QWidget):
    def __init__(self, *, log=None):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.log = log
        self.mlr_widget = MLRPlot(1)

        self.widgets = (self.mlr_widget, )

        self.tab_widget = TabWidget(widgets=self.widgets)

        self.main_layout.addWidget(self.tab_widget, 4)
        self.main_layout.addWidget(self.log, 1)


class MLRPlot(PlotWidget, Tab):
    def __init__(self, order):
        super().__init__(order)

    @property
    def tab_label(self):
        return 'MLR'
    
    def plot(self):
        self.draw()
