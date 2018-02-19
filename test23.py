#!/usr/bin/python
# -*- coding: UTF-8 -*-

fp = open("zhang.txt","wb")

#fp.close() #用来关闭文件
print "文件名：", fp.name
print "文件是否关闭：", fp.closed
print "访问模式：", fp.mode
print "末尾是否强制加空格：", fp.softspace

fp.write("www.noatin.com!\nVery good site!\n ")
fp.close()

fo = open( "zhang.txt" , "r+")
str = fo.read(8)
print "这里是从文件中读出的数据：", str

postion = fo.tell()
print "当前文件位置",postion

fp.close()