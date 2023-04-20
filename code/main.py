#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###----------1、文件说明----------###
'''
* 说明：代码例程模板
* 时间：2023-4-20 16:03:24
* 文件：
* 作者：whg
* 备注：
'''
import os, sys
from PySide2.QtWidgets import QMainWindow, QApplication
# 多线程使用的库
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QIcon

# 样式库
from qt_material import apply_stylesheet
import qdarkstyle
from qdarkstyle.light.palette import LightPalette

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowIcon(QIcon(os.path.join("logo.ico", "logo.ico")))  # 设置图标
        self.setWindowTitle("代码模板例程")
        # 从文件中加载UI定义
        qfile = QFile(os.path.join("main.ui", "main.ui"))
        qfile.open(QFile.ReadOnly)
        qfile.close()
        # 从UI定义中动态创建一个相应的窗口
        self.ui = QUiLoader().load(qfile)
        self.setCentralWidget(self.ui)

        # 界面
        style = apply_stylesheet(app, theme='dark_blue.xml')
        # style = apply_stylesheet(app, theme='light_teal_500.xml')
        # style = qdarkstyle.load_stylesheet(qt_api='pyside2')
        # style = qdarkstyle.load_stylesheet(qt_api='pyside2', palette=LightPalette())
        self.ui.setStyleSheet(style)
        self.resize(self.ui.size().width(), self.ui.size().height())

    def closeEvent(self, evt):
        '''关闭事件'''
        print('close')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
