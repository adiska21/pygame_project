from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import os


class StartMenuTicTakToe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("tictaktoe_regim.ui", self)
        self.button_pvp.clicked.connect(pvp())
        self.button_pvb.clicked.connect(pvb())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenuTicTakToe()
    ex.show()
    sys.exit(app.exec_())