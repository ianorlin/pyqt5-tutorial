#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        toolbox = QToolBox()
        layout.addWidget(toolbox, 0, 0)

        label = QLabel()
        toolbox.addItem(label, "Honda")
        label = QLabel()
        toolbox.addItem(label, "Toyota")
        label = QLabel()
        toolbox.addItem(label, "Mercedes")

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
