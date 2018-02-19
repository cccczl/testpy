#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

os.mkdir("test") #创建test目录
os.chdir("test") #切换到test 目录下去
#创建long.txt 并支持写入
fp = open("long.txt","wb")
fp.write("nihoa\n这里是我建立的文件\n ")
fp.close()

print "在test目录下",os.getcwd()

os.chdir("../")
print "切换路径到上级目录",os.getcwd()