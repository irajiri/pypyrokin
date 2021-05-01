from PySide2.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QGroupBox


class SetupInputPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.tab_widget = None
        self.setup_and_inputs_groupbox = self.setup_and_inputs_groupbox()

        self.main_layout.addWidget(self.setup_and_inputs_groupbox)
    
    def setup_and_inputs_groupbox(self):
        groupbox = QGroupBox('Setup and inputs')
        groupbox_layout = QVBoxLayout()
        groupbox.setLayout(groupbox_layout)

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(QWidget(), 'Test tab')

        groupbox_layout.addWidget(self.tab_widget)

        return groupbox


    
