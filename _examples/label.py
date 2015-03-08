#!/usr/bin/env python3

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("The Story of Dale")
        layout.addWidget(label, 0, 0)

        label = QLabel("Few people could understand Dale's motivation. It wasn't something that was easy to appreciate without the full context, but the full context was lost on Dale as he struggled with what he had done.")
        label.setWordWrap(True)
        layout.addWidget(label, 0, 1)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
