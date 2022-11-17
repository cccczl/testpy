#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 分拣本数组中的数

numbers = [12, 37, 28, 49, 3, 8, 5]   # 分拣本数组中的数
envn = []  # 两位数的放这个里
odd = []  #一位数的放这里
while numbers:   #循环开始 len得到数组的长度，小于0时循环停止
    number = numbers.pop()   # number等于每次删除numbers的最后一位数，pop()方法去删除
    t = len(str(number))   # 用str将删除的数转换成文本，用len取得它的位数
    if (t >= 2):  #如何t的位数大于或等于2，那么加入到这行envn
        envn.append(number)
    else:         #如果相反那么放到odd 这行
        odd.append(number)
print(envn, odd)  #打印出分拣后的数

#用for 循环重写上面的数值分拣
numbers = [12, 37, 28, 49, 3, 8, 5]
envn = []
odd =[]
for number in numbers:
    t = len(str(number))
    if (t >=2):
        envn.append(number)
    else:
        odd.append(number)
print(envn, odd)