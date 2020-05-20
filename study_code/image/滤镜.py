"""
-*- coding: utf-8 -*-
@author: yangyd
@file: 滤镜.py
@time: 2019/10/25 0025 10:48
"""

from PIL import Image, ImageFilter

img = Image.open('ludashi.jpg')
w, h = img.size
# 创建一个图像
img_out = Image.new('RGB', (2 * w, h))
img_out.paste(img, (0, 0,))
img_filter = img.filter(ImageFilter.GaussianBlur)
img_out.paste(img_filter, (w, 0))
img_out.save('new.jpg','JPEG')
img_out.show()
