# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
import random

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()
        self.ui.Push1.clicked.connect(self.easy)
        self.ui.Push2.clicked.connect(self.hard)


    def easy(self):

        a = ''
        for i in range(1, 9):
            up = chr(random.randint(65, 90))
            low = chr(random.randint(97, 122))
            spec = chr(random.randint(33, 48))
            list = [up, low, low, up, spec]
            b = random.choice(list)
            a += b
        self.ui.tb1.setText(a)

    def hard(self):
        a = ''
        for i in range(1, 12):
            up = chr(random.randint(65, 90))
            low = chr(random.randint(97, 122))
            spec = chr(random.randint(33, 48))
            list = [up, low, low, up, spec]
            b = random.choice(list)
            a += b
        self.ui.tb1.setText(a)

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec_())
