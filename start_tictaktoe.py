from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import os


class StartMenuTicTakToe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("select_regime.ui", self)
        self.button_pvp.clicked.connect(pvp)
        self.button_pvb.clicked.connect(pvb)


def pvp():
    os.system(r"python tictaktoe\2_player.py")


def pvb():
    os.system(r"python tictaktoe\bot.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenuTicTakToe()
    ex.show()
    sys.exit(app.exec_())