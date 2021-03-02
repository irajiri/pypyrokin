import sys
from PySide2.QtWidgets import QApplication

VERSION = '0.1-dev'


def main():
    app = QApplication(sys.argv)

    from src.gui.gui import Gui

    gui = Gui()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
