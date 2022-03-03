from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys
import os


class StartMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"img\start_menu.ui", self)
        self.button_snake.clicked.connect(self.snake)
        self.button_tictaktoe.clicked.connect(self.tictaktoe)
        self.button_pong.clicked.connect(self.pong)
        self.button_que.clicked.connect(self.que)

    def snake(self):
        os.system(r"python snake\snake.py")

    def tictaktoe(self):
        os.system(r"python start_tictaktoe.py")

    def pong(self):
        os.system(r"python start_pong.py")

    def que(self):
        os.system(r"python que\que.py")


# активация моего кода


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StartMenu()
    ex.show()
    sys.exit(app.exec_())