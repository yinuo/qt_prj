#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
import PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui imort QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAction = QAction(QIcon('title.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)




if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
