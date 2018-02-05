#!/usr/bin/python
# -*- coding: UTF-8 -*-

for i in "python":
    if i == 'h':
        continue     #条件满足后继续进行循环
    print i


#for 循环中 int 会报错
var = 10
while var > 0:
    var = var-1
    if var == 5:
        continue
    print "当前变量", var
print "结束"

#for 数值使用范围
for i in range(10):
    if i == 5:
        continue
    print "当前变量是" ,i
print "结束"