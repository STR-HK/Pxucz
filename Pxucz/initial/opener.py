import sys
import time

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtCore import Qt, QTimer, QCoreApplication

from Pxucz.initial.set_variables import INITIAL_LOADER_TEXT
from Pxucz.utils import global_variables


class LoadingUI(QWidget):
    def __init__(self, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.loglabel = QLabel("", self)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.setLogLabelText())
        self.timer.setInterval(10)
        self.timer.start()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pxucz_Loader")
        self.resize(self.size_x, self.size_y)

        layout = QVBoxLayout()
        layout.addWidget(self.loglabel)
        self.setLayout(layout)

    def setLogLabelText(self):
        print(global_variables.get_var(INITIAL_LOADER_TEXT))
        self.loglabel.setText(global_variables.get_var(INITIAL_LOADER_TEXT))


def window_shower(size_x: int, size_y: int):
    loadingWin = LoadingUI(size_x=size_x, size_y=size_y)
    loadingWin.show()
    return loadingWin


global app


def start(size_x: int, size_y: int):
    global app
    app = QApplication(sys.argv)
    loadingWin = window_shower(size_x, size_y)
    sys.exit(app.exec())


def off():
    app.exec()
