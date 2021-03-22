# -*- coding: utf-8 -*-

import os
import shutil

path = "F:/迅雷下载"     # 当前路径的所有文件
files = os.listdir(path)

for f in files:
    # f.png
    # ./png
    folder_name = "F:/迅雷下载" +'/' +f.split('.')[-1]
    if not os.path.exists(folder_name):
        # makefolder()
        os.makedirs(folder_name)
        # movefolder()
        shutil.move(path + '/' + f, folder_name)
    else:
        shutil.move(path +'/' +f, folder_name)