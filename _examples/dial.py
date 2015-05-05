#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Dialog(QWidget):
    def __init__(self):
        super(Dialog, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.slider_changed)
        layout.addWidget(self.dial)

    def slider_changed(self):
        print("Current dial value: %i" % (self.dial.value()))

app = QApplication(sys.argv)

screen = Dialog()
screen.show()

sys.exit(app.exec_())
