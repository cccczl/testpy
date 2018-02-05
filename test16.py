#!/usr/bin/python
# -*- coding: UTF-8 -*-

tup1 = (12, 34, 56)
tup2 = ('abc', 'xyz')
tup4 = ('all',)     #单个元组中的元素要加，号。
tup3 = tup1 + tup2 + tup4
print tup3


#将元组转换为列表，进行分拣，看他的类型是什么，然后分到新的列表中。
alist = list(tup3)  #将元组转换为列表后操作
intlist = []
strlist = []
for x in alist:
    if type(x) is int:
        x = x +10
        intlist.append(x)
    else:
        x = x.capitalize()
        strlist.append(x)

print intlist
print strlist
print "这里是循环后的" ,alist


del tup3  #元组只能被全部删除。不能单独修改其中的元素