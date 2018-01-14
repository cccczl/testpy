#!/usr/bin/python
# -*- coding: UTF-8 -*-

for num in range(10, 20):  # 将mum的值设置为范围10-20之间
    for i in range(2, num):  # 将i的范围设置为2开始，num结束
        print "现在是：", range(2, num)
        print "i是：", i
        if num % i == 0:  #用2到num所有的值除与i，如果结对定于0那么继续运行 j= num/i
            j = num / i
            print '%d 等于 %d * %d' % (num, i, j)
            print '现在j的值', j
            break
    else:
        print num, '是一个质数'
