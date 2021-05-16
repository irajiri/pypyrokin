from PySide2.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout,
                               QTabWidget)
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvas, NavigationToolbar2QT as NavigationToolbar)


class Tab:
    @property
    def tab_label(self):
        raise NotImplementedError


class TabWidget(QTabWidget):
    def __init__(self, *, widgets=None):
        super().__init__()
        self.widgets = widgets

        for widget in self.widgets:
            self.addTab(widget, widget.tab_label)


class PlotWidget(QWidget):

    LEFT = 0.08
    RIGHT = 0.965
    TOP = 0.965
    BOTTOM = 0.07

    X_LABEL = 'x_label'
    Y_LABEL = 'y_label'
    X_UNIT = 'unit'
    Y_UNIT = 'unit'

    def __init__(self, order):
        super().__init__()
        self.order = order
        self.figure = Figure()
        self.figure.subplots_adjust(left=self.LEFT,
                                    right=self.RIGHT,
                                    top=self.TOP,
                                    bottom=self.BOTTOM,
                                    )
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.main_layout = QVBoxLayout(self)
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.toolbar)
        self.main_layout.addLayout(self.horizontal_layout)
        self.main_layout.addWidget(self.canvas)
        self.axis = self.figure.add_subplot()

        self.setLayout(self.main_layout)
        self.setContentsMargins(0, 0, 0, 0)

        self.axis.format_coord = self.format_coord

    def format_coord(self, x, y):
        axial, radial = x, y
        text = f'{self.X_LABEL}={axial:.4f} {self.Y_LABEL}={radial:.4f}'

        return text

    def draw(self):
        self.canvas.draw()

    def clear(self):
        self.axis.clear()
        self.set_axis_labels()
        self.draw()

    def grid(self, **kwargs):
        self.axis.grid(**kwargs)

    def set_x_label(self, label):
        self.axis.set_xlabel(label)

    def set_y_label(self, label):
        self.axis.set_ylabel(label)

    def set_axis_equal(self):
        self.axis.set_aspect(aspect='equal', adjustable='box')

    def plot(self, *args, scalex=True, scaley=True,
             xlabel=None, ylabel=None, grid=True, clear=True,
             axis_equal=False, legend=False,
             **kwargs):

        if clear:
            self.axis.clear()

        self.axis.plot(*args, scalex=scalex, scaley=scaley, **kwargs)
        self.grid(b=grid)

        if xlabel is not None:
            self.axis.set_xlabel(xlabel)

        if ylabel is not None:
            self.axis.set_ylabel(ylabel)

        if axis_equal:
            self.set_axis_equal()

        if legend:
            self.axis.legend(loc=0)
