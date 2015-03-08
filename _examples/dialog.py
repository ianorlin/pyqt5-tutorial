#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Dialog(QWidget):
    def __init__(self):
        super(Dialog, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel("This is a dialog.")
        layout.addWidget(label, 0, 0)

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        layout.addWidget(buttonbox)

app = QApplication(sys.argv)

screen = Dialog()
screen.show()

sys.exit(app.exec_())
