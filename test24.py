#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

import os

try:
    os.mkdir("test")  # 创建test目录
except IOError:
    print "文件夹已经存在"
os.chdir("test")  # 切换到test 目录下去
with open("long.txt", "wb") as fp:
    fp.write("nihoa\n这里是我建立的文件\n ")
import os

os.chdir("../")
import os

print "切换路径到上级目录", os.getcwd()
