# -*- coding: utf-8 -*-
# @Time    : 2019/3/13 10:17
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: map.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop




import os
import PIL

from multiprocessing import Pool
from PIL import Image

SIZE = (75,75)
SAVE_DIRECTORY = 'thumbs'


def get_image_paths(folder):
    return (os.path.join(folder, f)
            for f in os.listdir(folder)
            if 'png' in f)


def create_thumbnail(filename):
    im = Image.open(filename)
    im.thumbnail(SIZE, Image.ANTIALIAS)
    base, fname = os.path.split(filename)
    save_path = os.path.join(base, SAVE_DIRECTORY, fname)
    im.save(save_path)


if __name__ == '__main__':
    folder = os.path.abspath(
        'image')
    os.mkdir(os.path.join(folder, SAVE_DIRECTORY))

    images = get_image_paths(folder)

    pool = Pool()
    pool.map(create_thumbnail, images)
    pool.close()
    pool.join()
