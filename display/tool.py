#!/usr/bin/env python
# -*- coding:UTF-8 -*-

from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
#from PyQt5.QtGui import QIcon

import sys, os


#enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
class MyTable(QTableWidget):
    def __init__(self, parent=None):
        super(MyTable, self).__init__(parent)

        self.setWindowTitle("test tool")
        self.setWindowIcon(QIcon('title.png'))
        self.resize(1000, 800)
        self.center()

        self.linedict = {}
        linelist = open("./test-config.ini").readlines()
        for i, line in enumerate(linelist):
            key = str(i)
            value = line.strip().split('-')[1].replace("[shell]=", "")
            self.linedict.setdefault(key, value)
        rows = len(linelist)

        #create table
        self.setColumnCount(2)
        self.setRowCount(rows)
        self.setColumnWidth(0, 530)
        self.setColumnWidth(1, 430)

        self.setFont(QFont("Times", 14))
        #set table can not change
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.settableHeader()
        self.settableHeaderFontColor()
        self.inputcelldata(linelist)

        self.show()

    def settableHeader(self):
        columnname = ['项目名称', '是否测试']
        self.setHorizontalHeaderLabels(columnname)

    def settableHeaderFontColor(self):
        for x in range(self.columnCount()):
            headItem = self.horizontalHeaderItem(x) # 获得水平方向表头的Item对象
            headItem.setFont(QFont("song", 22, QFont.Bold))

    def inputcelldata(self, linelist):
        for row_number, row_data in enumerate(linelist):
            if row_data != "":
                self.setRowHeight(row_number, 60)
                data1 = row_data.strip().split('-')[0].replace("[title]=", "")
                print(data1)
                self.setItem(row_number, 0, QTableWidgetItem(data1))
                self.setCellWidget(row_number, 1, self.buttonForRow(str(row_number)))

    def viewTable(self, id):
        if id in self.linedict:
#            print self.linedict[id]
            self.close()
            os.system(self.linedict[id])

    def buttonForRow(self, id):
        widget = QWidget()
        viewBtn = QPushButton('启动')
        viewBtn.clicked.connect(lambda: self.viewTable(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(viewBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)#设置左侧、顶部、右侧和底部边距，以便在布局周围使用。
        widget.setLayout(hLayout)
        return widget

    #控制窗口显示在屏幕中心的方法
    def center(self):
        # 获得窗口s
        qr = self.frameGeometry()
        # 获得屏幕中心点
        cp = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myTable = MyTable()
 #   myTable.show()

    app.exit(app.exec_())
