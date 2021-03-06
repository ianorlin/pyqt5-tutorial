#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        button = QRadioButton("Brazil")
        button.setChecked(True)
        layout.addWidget(button, 0, 0)

        button = QRadioButton("Argentina")
        layout.addWidget(button, 0, 1)

        button = QRadioButton("Ecuador")
        layout.addWidget(button, 0, 2)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
