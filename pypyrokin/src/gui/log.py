from PySide2.QtWidgets import (QWidget, QVBoxLayout, QTextEdit, QSizePolicy,
                               QGroupBox)


class Log(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

        self.edit = None
        self.main_layout.addWidget(self.groupbox())

    def groupbox(self):
        groupbox = QGroupBox('Log')
        layout = QVBoxLayout()
        groupbox.setLayout(layout)

        self.edit = QTextEdit()
        self.edit.setReadOnly(True)
        self.edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(self.edit)

        return groupbox
