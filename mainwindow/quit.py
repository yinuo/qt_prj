#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        # qbtn.sizeHint()显示默认尺寸
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        # 设置窗口的位置和大小
        self.setGeometry(300, 300, 250, 250)
        self.setWindowTitle('Quit button')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())