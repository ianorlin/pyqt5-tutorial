#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        layout = QGridLayout()
        self.setLayout(layout)

        button = QRadioButton("RadioButton 1")
        button.setChecked(True)
        print(button.isChecked())
        layout.addWidget(button, 0, 0)
        button = QRadioButton("RadioButton 2")
        layout.addWidget(button, 0, 1)

    def button_clicked(self, button):
        print("The button was pressed!")

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
