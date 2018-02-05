#!/usr/bin/python
# -*- coding: UTF-8 -*-

i = 1
while i < 10:
    i +=1
    if i%2 >0:   #如果没有加continue ，那么输出的是非双数
        continue #用于跳过这次循环
    print i    #加continue后输出双数


i = 1
while 1:      #从1开始循环
    print i    #打印每次循环得到的数
    i +=1       #每次循环加1
    if i >10:    #如果循环后i的值大于10
        break    #跳出循环