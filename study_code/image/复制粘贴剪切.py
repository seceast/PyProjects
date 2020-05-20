"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 复制粘贴剪切.py
@time: 2019/10/25 0025 09:36
"""


from PIL import Image


img = Image.open('ludashi1.jpg')
# 复制
img_1 = img.copy()
# 剪切
region = img_1.crop((5, 5, 120, 120))

img_2 = img.copy()
# 粘贴
img_2.paste(region, (30, 30))
img_2.show()
