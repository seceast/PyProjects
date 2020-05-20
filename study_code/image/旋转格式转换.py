"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 旋转格式转换.py
@time: 2019/10/25 0025 09:44
"""


from PIL import Image


img = Image.open('ludashi.jpg')
# 图片旋转90度
# img.rotate(90).show()

# 格式转换
img.transpose(Image.FLIP_TOP_BOTTOM).show()
img.transpose(Image.FLIP_LEFT_RIGHT).show()