#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        time = QTime()
        time.setHMS(13, 15, 40)

        timeedit = QTimeEdit()
        timeedit.setTime(time)
        layout.addWidget(timeedit, 0, 0)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
