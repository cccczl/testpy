#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = []   ##建立空列表
list.append('google')
list.append('baidu')
list.append('nihao')
list.append('no')
blist = ['yi','er','san','si']

print list
print "这个是最大值的元素", max(list)
print "这个是最小值的元素", min(list)
print list.pop(0)
#print list.insert(1,'1111')
print list.extend(blist)
print list

for x in list:
    print len(x)
