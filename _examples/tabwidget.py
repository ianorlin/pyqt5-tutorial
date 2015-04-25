#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        label1 = QLabel("Example content contained in a tab.")
        label2 = QLabel("More example text in the second tab.")

        tabwidget = QTabWidget()
        tabwidget.addTab(label1, "Tab 1")
        tabwidget.addTab(label2, "Tab 2")
        layout.addWidget(tabwidget, 0, 0)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
