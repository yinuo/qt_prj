#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget
from PyQt5.QtGui import QIcon

class Display(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(500, 400)
        self.center()

        self.btn1 = QPushButton(self)
        self.btn2 = QPushButton(self)
        self.btn3 = QPushButton(self)
        self.btn4 = QPushButton(self)

        self.btn1.setText('小盒子老化')
        self.btn2.setText('单芯片卡老化测试')
        self.btn3.setText('核心板老化测试')
        self.btn4.setText('核心板烧写')

        self.btn1.resize(100, 40)
        self.btn2.resize(100, 40)
        self.btn3.resize(100, 40)
        self.btn4.resize(100, 40)

        self.btn1.move(50, 50)
        self.btn2.move(200, 50)
        self.btn3.move(50, 200)
        self.btn4.move(200, 200)

        self.btn1.clicked.connect(self.begin_shell_test1)
        self.btn2.clicked.connect(self.begin_shell_test2)
        self.btn3.clicked.connect(self.begin_shell_test3)
        self.btn4.clicked.connect(self.begin_shell_test4)

        self.setWindowTitle('Display')
        self.setWindowIcon(QIcon('./2.png'))
        self.show()

    def get_shell(self, name):

        shelldict = {}
        for lines in open("./test-config.ini").readlines():
            lines = lines.strip()
            print(lines)
            if lines != "":
                key = lines.split(" ")[0].replace("[title]=", "")
                value = lines.split(" ")[1].replace("[shell]=", "")
                shelldict.setdefault(key, value)
                print(shelldict)

        #if shelldict.has_key(name):
        if name in shelldict:
            print(shelldict[name])
            shell = shelldict[name]
            self.close()
            os.system(shell)

    def begin_shell_test1(self):
        name = self.btn1.text()
        print(name)
        self.get_shell(name)

    def begin_shell_test2(self):
        name = self.btn2.text()
        print(name)
        self.get_shell(name)

    def begin_shell_test3(self):
        name = self.btn3.text()
        print(name)
        self.get_shell(name)

    def begin_shell_test4(self):
        name = self.btn4.text()
        print(name)
        self.get_shell(name)

    # 控制窗口显示在屏幕中心的方法
    def center(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    ex = Display()

    sys.exit(app.exec_())