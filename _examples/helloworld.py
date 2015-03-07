#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Hello")

        label = QLabel("Hello, World!")

        layout = QGridLayout()
        layout.addWidget(label, 0, 0)

        self.setLayout(layout)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
