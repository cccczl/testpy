#!/usr/bin/python
# -*- coding: UTF-8 -*-

def printname(str):
    "传入字符串"
    print str
    return

printname("在这里传入字符串给函数")
printname("第二次传入字符给函数")

#传递不可变对象

def ChangInt( a ):
    a = 10
    print a

b = 2
ChangInt(b)
print b


#传递可变对象

def ChangName(mylist):
    "修改传入的列表"
    mylist.append([1,2,3,4])
    print "打印内置函数",mylist
    return
mylist = [10,20,30];
ChangName(mylist);
print "打印外置函数" , mylist

#参数传递时顺序不重要python知道按照名次来匹配
#配置默认值，在没有传入参数时输出默认值，设置默认值的应该放在参数的第二个，否则会报错
def nameAge(name="cccczl",age = 30  ):
    print "name", name
    print "age", age
    return
nameAge(age=35,name="zhang")
nameAge(name = "long")
nameAge()

