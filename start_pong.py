from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import os


class StartMenuPong(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("pong_regim.ui", self)
        self.button_pvp.clicked.connect(pvp)
        self.button_pvb.clicked.connect(pvb)


def pvp():
    os.system(r"python pong\2_player.py")


def pvb():
    os.system(r"python pong\bot.py")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenuPong()
    ex.show()
    sys.exit(app.exec_())