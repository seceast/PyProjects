"""
-*- coding: utf-8 -*-
@author: yangyd
@file: learn_image.py
@time: 2019/10/24 0024 17:20
"""

from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('ludashi.jpg')
# 获得图像尺寸:
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%:
im.thumbnakil((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存:
im.save('thumbnail.jpg', 'jpeg')


# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。

# 比如，模糊效果也只需几行代码：


# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('ludashi1.jpg')
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
