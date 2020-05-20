# -*- coding: utf-8 -*-
# __author__ = yangyd 
# File: test.py
# Create time: 2020/5/12 0012 16:23


# from PyQt5.Qt import *
import sys
from PyQt5.Qt import *


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.resize(500, 500)
        self.setMouseTracking(True)  # 设置鼠标跟踪
        self.label = QLabel(self)
        self.label.setText('跟随鼠标移动')

    def mouseMoveEvent(self, mv: QMouseEvent):
        # pos = mv.localPos()获取鼠标相对于主窗口的位置
        # lab = self.findChild(QLabel)
        self.label.move(mv.localPos().x(), mv.localPos().y())

    def set_label(self, label_text):
        self.label.setText(label_text)


app = QApplication(sys.argv)

win = MyWidget()
win.set_label("大家一起学python")

win.show()
sys.exit(app.exec_())
