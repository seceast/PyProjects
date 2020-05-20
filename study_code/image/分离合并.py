"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 分离合并.py
@time: 2019/10/25 0025 10:44
"""


from PIL import Image


img1 = Image.open('ludashi.jpg')
img2 = Image.open('ludashi1.jpg')

img2 = img2.resize(img1.size)

# 分离
r1,g1,b1 = img1.split()
r2,g2,b2 = img2.split()

# 合并
tmp = [r1,g2,b1]
img = Image.merge("RGB", tmp)
img.show()