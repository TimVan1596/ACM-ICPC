# -*- coding:utf-8 -*-
# @Time:2020/5/30 11:41
# @Author:TimVan
# @File:leetcode.py
# @Software:PyCharm

# 单行注释
# print("hello world")

"""
  这个是多行注释
  注意UTF-8的coding
"""
# print("你们好")

# import keyword
# print(keyword.kwlist)

# 格式化输出


"""
    age = 20
    name = 'Tim Van'
    name = 'my name is ' + name
    print(" my age is %d, %s" % (age + 1, name))
    print("Bill", "Jobs", "Jack", sep="-", end="\t")
    print("???", sep="\t")
    print("---")
"""

# 输入
# userName = input("请输入你的用户名\n")
# age = input("请输入您的年龄\n")
# print("您的用户名为%s,年龄为%d" % (userName, int(age)))
# print("type(age) = ", type(age))

# 条件判断
# import random
#
# sex = 'female'
# age = random.randint(-20, 160)
#
# print("性别：", sex)
# print("年龄：%d" % age)
#
# if sex == 'female':
#     print("女性")
# else:
#     print("男性")
#
# if 100 <= age < 150:
#     print("高寿")
# elif 60 <= age < 100:
#     print("老年")
# elif 35 <= age < 60:
#     print("中年")
# elif 18 <= age < 35:
#     print("青年")
# elif 6 <= age < 18:
#     print("少年")
# elif 0 <= age < 6:
#     print("幼年")
# else:
#     print("你是个老妖吧\n")
# import random
# ret = random.randint(0, 2)
# print(ret)

# a = input()
# print(type(a))
# if type(a) == 'str':
#     print("<class 'str'>")
# else:
#     print("none")

# 循环
# sumNum: int = 0
# floor = 1
# ceiling = 100
# for i in range(floor, ceiling + 1, 1):
#     sumNum += i
# print("in for,sum = %d" % sumNum)
#
# sumNum = 0
# i = 0
# while i <= ceiling:
#     sumNum += i
#     i += 1
# print("in for,sum = %d" % sumNum)

# while else 用法
# i = 0
# while i < 5:
#     print("i=%d" % i)
#     i += 1
# else:
#     print("超出边界，此时i=%d" % i)

# print("-"*5)

# 字符串截取
# myStr = "hello world"
# print(myStr[0:5:2])

'''
# List列表的使用
#增
namelist = ["Jack", "Bill", "Steve"]
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()

namelist.append(["Tim", "Pony"])
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()

namelist.extend(["Robin", "Satoshi"])
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()


namelist.insert(1, "Linus")
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()

# 删
del namelist[2]
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()

# 改
namelist[2] = "Jobs"
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()

# 查
name = "Jobs"
if name in namelist:
    print("%s in nameList , index = %d" % (name, namelist.index(name)))
else:
    print("Not Found")

# 列表的升序与降序、反转
namelist.reverse()
print("namelist=>")
i = 0
for i in range(len(namelist)):
    print(namelist[i], end="\t")
print()


ageList = [10, 58, 20, 6, 99]
ageList.sort()
print("-"*15, "经过升序")
print("ageList=>")
i = 0
for i in range(len(ageList)):
    print(ageList[i], end="\t")
print()

ageList.sort(reverse=True)
print("-"*15, "经过降序", "-"*15)
print("ageList=>")
i = 0
for i in range(len(ageList)):
    print(ageList[i], end="\t")
print()

print(ageList[-2])
print(ageList[1:3])
'''

'''
# 元组的相关操作
tup1 = (10,)
tup2 = ('元组', 3.14)
# 连接
tup = tup1 + tup2
print(tup)
'''

# # 字典
# myDict = {
#     'name': '一战回忆录',
#     'author': 'Winston Churchill',
#     'price': 99.01
# }
# print(myDict)
# # 取某个值不存在的值
# print(myDict.get("ISBN", '0'))
#
# # 增
# myDict['ISBN'] = '9787806605608'
# print(myDict)
# # 删
# # del 为删除结构本身
# del myDict['price']
# print(myDict)
# # dict.clear()为删除字典中的内容
# myDict.clear()
# print(myDict)
# # 改
# myDict['name'] = '第一次世界大战回忆录'
# print(myDict)
# # 查
# myDict = {
#     'name': '一战回忆录',
#     'author': 'Winston Churchill',
#     'price': 99.01
# }
# print(myDict.keys())
# print(myDict.values())
# print(myDict.items())
#
#
# # for key in myDict.keys():
# #     print(key, '->', myDict[key])
#
# # print("\n", '-' * 8, '枚举', '-' * 8)
# # for index, tup in enumerate(myDict.items()):
# #     print('%d:' % index, tup[0], '->', tup[1])
#
#
# # 打印字典，并返回字典长度
# def printDict(actionName, ourDict):
#     print("\n", '-' * 8, actionName, '-' * 8)
#     for ourIndex, ourTup in enumerate(ourDict.items()):
#         print('%d:' % ourIndex, ourTup[0], '->', ourTup[1])
#     return len(ourDict.keys()), len(ourTup)
#
#
# print("字典长度为:%d,%d" % printDict('函数中枚举', myDict))


# # 局部变量和全局变量
# a = 1718
#
#
# def fun():
#     global a
#     print("in fun(),a=%d" % a)
#     a = 2020
#
#
# def fun1():
#     print("in fun(),a=%d" % a)
#
#
# fun()
# fun1()

# 文件处理
# file = open("word.txt", 'r')
# file.write("blue\nread\nfunction\n")
# word = file.read(50)
# print(word)
# words = file.readlines()
# for i, word in enumerate(words):
#     print("%d:%s" % (i, word))

# word = file.readline()
# print(word)
#
# file.close()

# 错误和异常
# try:
#     print("尝试打开文件")
#     file = open('doc.txt', 'r')
#     print("打开成功")
# # 对可能的异常可以用大括号
# except (IOError, NameError):
#     print("打开失败！未找到doc.txt")
#     try:
#         print(a)
#     except NameError as reason:
#         print("未定义变量a")
#         print("reason:%s" % reason)

# try..except..finally
# import time
#
# try:
#     file = open('word.txt', 'r')
#     try:
#         while True:
#             line = file.readline()
#             if len(line) > 0:
#                 print(line)
#                 time.sleep(1)
#             else:
#                 break
#     except Exception as reason:
#         print("[Wrong]reason:%s" % reason)
#     finally:
#         file.close()
# except Exception as reason:
#     print("[Wrong]reason:%s" % reason)

# &、| 和 and、or 运算符
# 47 = 二进制 101111
# 16 = 二进制 01000
# a = 47
# b = 16
# c = 0
# # 与运算为0
# print("(a & b) =  %d" % (a & b))
# # 或运算为63
# print("(a | b) =  %d" % (a | b))
# # and运算
# print("(a and b) =  %d" % (a and b))
# print("(a > b) & (b > c)=  %s" % ((a > b) & (b > c)))
# print("(a > b) and (b > c)=  %s" % ((a > b) and (b > c)))
# # or运算
# print("(a or b) =  %d" % (a or b))
# print("(c or b) =  %d" % (c or b))

# nums = [3, 3]
# hashmap = {}
# for ind, num in enumerate(nums):
#     hashmap[num] = ind
# print(hashmap)


# print(int(5/4))

# break语句和while..else..
# a = 3
# while a > 0:
#     print("a=%d" % a)
#     a -= 1
#     # break
# else:
#     print("It's in else")

# a = 50
# a //= 3
# print(a)

# 负数取余
# a = 15
# print(a % 10)
# a = -15
# print(a % 10)
# a = -12
# print(a % 10)
# a = -12
# print(a % 4)
# a = -11
# print

# n < (-2 ^ 31)

# print((2 ** 32))

# romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50
#     , 'C': 100, 'D': 500, 'M': 1000
#     , 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
#
# print(romanDict.get('A', 3))

# zip()的使用
# list1 = ["Tim", "Jobs", "Steve", "Bill"]
# list2 = [22, 56, 56, 63]
#
# list3 = ["蒂姆", "乔布斯"]
# zipped = zip(list1, list2, list3)
# print(zipped)
# print(list(zipped))
# print(zip(*list1))
# print("------")
# for one in zip(*list1):
#     print(one)

# set的使用
# list1 = ["Tim", "Tim", 3.14, "Tim"]
# print(set(list1))
# print(len(set(list1)))

# list.pop()的参数
# list1 = ["Tim", "Tim", 3.14, "Tim"]
# a = 2
# a = list1.pop(a)
# print(a)
# print(list1)

# range()的参数
# arr = [10, 6, 58, 6, 2020, 6, 23]
# for i in range(0, 7, 2):
#     # if arr[i] == 6:
#     #     print("删除arr[%d]=%d" % (i, arr[i]))
#     #     arr.pop(i)
#
#     print("---i==%d,arr[i]=%d---" % (i, arr[i]))
#
# print("new arr =", arr)

# # index()和find()
# haystack = "singlyly"
# # needle = "lya"
# needle = ""
# print(haystack.index(needle))
# print(haystack.find(needle))

# 二分查找
# def binaryFind(arr: list, target: int):
#     right = 0
#     left = len(arr) - 1
#     while right <= left:
#         mid = (right + left) // 2
#         print("mid=%d" % mid)
#         midValue = arr[mid]
#         if midValue < target:
#             right = mid + 1
#         elif midValue > target:
#             left = mid - 1
#         else:
#             print("已找到，序号为%d" % mid)
#             return
#     print("未找到")
#
#
# myArr = [0, 6, 26, 51, 424, 2020]
# myTarget = 20000
# binaryFind(myArr, myTarget)

# 已知数组长度进行初始化赋值
# arrLen = 5
# value = 1
# arr = [value] * arrLen
# # arr = [value for i in range(arrLen)]
# for i in range(len(arr)):
#     print(arr[i])

# 二维数组的初始化
# import numpy as np

# 迭代器和生成器
# myList = [13, 55, 2020, 7, 12]
# it = iter(myList)
# for循环
# print(next(it))
# for x in it:
#     print(x)

# import sys
# # while循环
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


# 创建一个迭代器
# 把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()与__next__() 。
# 如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python的构造函数为__init__()
# , 它会在对象初始化的时候执行。更多内容查阅：Python3面向对象
#
# __iter__()方法返回一个特殊的迭代器对象， 这个迭代器对象实现了__next__()方法并通过StopIteration
# 异常标识迭代的完成。
# __next__()方法（Python2里是next()）会返回下一个迭代器对象。
#
# 创建一个返回数字的迭代器，初始值为1，逐步递增1：
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for x in myiter:
#     print(x)

# 生成器
# 在Python中，使用了yield的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，
# 返回yield 的值, 并在下一次执行next()方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。
# 以下实例使用yield实现斐波那契数列：

# import sys
#
# # 生成器函数 - 斐波那契
# def fibonacci(n):
#     a, b, counter = 0, 1, 0
#     while True:
#         if counter > n:
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()

# 使用生成器yield构建斐波拉契数列
# import sys
#
# def yieldFibonacci(n):
#     a, b, count = 1, 1, 0
#     while count < n:
#         yield a
#         x = a
#         a = b
#         b = x+b
#         count += 1
#     return
#
#
# it = yieldFibonacci(10)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

# a = 10
# b = 20
# a, b = b, a + b
# print("a=%d" % a)
# print("b=%d" % b)


# Python3 输入和输出
# 输出格式美化
# Python两种输出值的方式: 表达式语句和 print() 函数。
# 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
# 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
# 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
# str()： 函数返回一个用户易读的表达形式。
# repr()： 产生一个解释器易读的表达形式。
# 例如
# >>> s = 'Hello, Runoob'
# >>> str(s)
# 'Hello, Runoob'
# >>> repr(s)
# "'Hello, Runoob'"
# >>> str(1/7)
# '0.14285714285714285'
# >>> x = 10 * 3.25
# >>> y = 200 * 200
# >>> s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
# >>> print(s)
# x 的值为： 32.5,  y 的值为：40000...
# >>> #  repr() 函数可以转义字符串中的特殊字符
# ... hello = 'hello, runoob\n'
# >>> hellos = repr(hello)
# >>> print(hellos)
# 'hello, runoob\n'
# >>> # repr() 的参数可以是 Python 的任何对象
# ... repr((x, y, ('Google', 'Runoob')))
# "(32.5, 40000, ('Google', 'Runoob'))"
# 格式化输出
# year = '2020年'
# month = 7
# temp = 32.445
# message = "今年是{}的{}月份".format(year, month)
# # 四舍五入
# print(message + "，今天的温度是%.2f°C" % temp)

# Python3 模块
# 在前面的几个章节中我们脚本上是用python解释器来编程，
# 如果你从Python解释器退出再进入，
# 那么你定义的所有的方法和变量就都消失了。
#
# 为此Python提供了一个办法，
# 把这些定义存放在文件中，
# 为一些脚本或者交互式的解释器实例使用，
# 这个文件被称为模块。
#
# 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
# 模块可以被别的程序引入，
# 以使用该模块中的函数等功能。
# 这也是使用python标准库的方法。
#
# 下面是一个使用python标准库中模块的例子。

# !/usr/bin/python3
# 文件名: using_sys.py
# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#     print(i)
#
# print('\n\nPython 路径为：', sys.path, '\n')
#
# import sys
#
# print("引入的命令行")
# for i in sys.argv:
#     print(i)
#
# print("\n\n Python的路径为: %s" % sys.path)

# import 语句
#
# 想使用Python源文件，
# 只需在另一个源文件里执行import 语句，语法如下：
# import module1[, module2[, ... moduleN]
#
# 当解释器遇到import语句，
# 如果模块在当前的搜索路径就会被导入。
# 搜索路径是一个解释器会先进行搜索的所有目录的列表。
# 如想要导入模块support，
# 需要把命令放在脚本的顶端：
#
# support.py文件代码
# # !/usr/bin/python3
# # Filename: support.py
#
# def print_func(par):
#     print("Hello : ", par)
#     return
#
# test.py引入support模块：
# test.py文件代码
# # !/usr/bin/python3
# # Filename: test.py
#
# # 导入模块
# import support
#
# # 现在可以调用模块里包含的函数了
# support.print_func("Runoob")
#
# 以上实例输出结果：
# $ python3 test.py
# Hello: Runoob
#
#
# import tool as t
#
# a = 15
# b = 2020
# mySum = t.add(a, b)
# print("mySum=%d" % mySum)

# 一个模块只会被导入一次，
# 不管你执行了多少次import。
# 这样可以防止导入模块被一遍又一遍地执行。
#
# 当我们使用import语句的时候，
# Python解释器是怎样找到对应的文件的呢？
#
# 这就涉及到Python的搜索路径，
# 搜索路径是由一系列目录名组成的，
# Python解释器就依次从这些目录中去寻找所引入的模块。
#
# 这看起来很像环境变量，
# 事实上，也可以通过定义环境变量的方式来确定搜索路径。
#
# 搜索路径是在Python编译或安装的时候确定的，
# 安装新的库应该也会修改。
# 搜索路径被存储在sys模块中的path变量，
# 做一个简单的实验，在交互式解释器中，输入以下代码：
#
# >>> import sys
# >>> sys.path
# ['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']
# >>>

# import sys
#
# print(sys.path)

# sys.path 输出是一个列表，
# 其中第一项是空串''，
# 代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），
# 亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。
#
# 因此若像我一样在当前目录下存在与要引入模块同名的文件，
# 就会把要引入的模块屏蔽掉。
#
# 了解了搜索路径的概念，就可以在脚本中修改sys.path来引入一些不在搜索路径中的模块。
# 现在，在解释器的当前目录或者sys.path中的一个目录里面来创建一个fibo.py的文件，代码如下：
# # 斐波那契(fibonacci)数列模块
# def fib(n):  # 定义到 n 的斐波那契数列
#     a, b = 0, 1
#     while b < n:
#         print(b, end=' ')
#         a, b = b, a + b
#     print()
#
# def fib2(n):  # 返回到 n 的斐波那契数列
#     result = []
#     a, b = 0, 1
#     while b < n:
#         result.append(b)
#         a, b = b, a + b
#     return result

# 然后进入Python解释器，使用下面的命令导入这个模块：
# >> > import fibo
#
# 这样做并没有把直接定义在fibo中的函数名称写入到当前符号表里，
# 只是把模块fibo的名字写到了那里。
# 可以使用模块名称来访问函数：
# >> > fibo.fib(1000)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
# 610
# 987
# >> > fibo.fib2(100)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# >> > fibo.__name__
# 'fibo'
# 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
#
# >> > fib = fibo.fib
# >> > fib(500)
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377
#
# import tool as t
#
# add = t.add
# print("name=%s" % t.__name__)
# print("add=%d" % add(15, 21))

# from … import 语句
# Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中，语法如下：
#
# from modname import name1[, name2[, ... nameN]]
# 例如，要导入模块 fibo 的 fib 函数，使用如下语句：
#
# >>> from fibo import fib, fib2
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。
#
#
# from … import * 语句
# 把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：
#
# from modname import *
# 这提供了一个简单的方法来导入一个模块中的所有项目。然而这种声明不该被过多地使用。
#
# from tool import add
#
# print("add=%d" % add(15, 27))

# 深入模块
# 模块除了方法定义，还可以包括可执行的代码。
# 这些代码一般用来初始化这个模块。
# 这些代码只有在第一次被导入时才会被执行。
#
# 每个模块有各自独立的符号表，
# 在模块内部为所有的函数当作全局符号表来使用。
#
# 所以，模块的作者可以放心大胆的在模块内部使用这些全局变量，
# 而不用担心把其他用户的全局变量搞混。
#
# 从另一个方面，当你确实知道你在做什么的话，
# 你也可以通过 modname.itemname 这样的表示法来访问模块内的函数。
#
# 模块是可以导入其他模块的。
# 在一个模块（或者脚本，或者其他地方）的最前面使用 import 来导入一个模块，
# 当然这只是一个惯例，而不是强制的。
# 被导入的模块的名称将被放入当前操作的模块的符号表中。
#
# 还有一种导入的方法，
# 可以使用 import 直接把模块内（函数，变量的）名称导入到当前操作模块。比如:
#
# >>> from fibo import fib, fib2
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# 这种导入的方法不会把被导入的模块的名称放在当前的字符表中
# （所以在这个例子里面，fibo 这个名称是没有定义的）。
#
# 这还有一种方法，可以一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表:
#
# >>> from fibo import *
# >>> fib(500)
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377
# 这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。
# 大多数情况， Python程序员不使用这种方法，
# 因为引入的其它来源的命名，很可能覆盖了已有的定义。

# __name__属性
# 一个模块被另一个程序第一次引入时，
# 其主程序将运行。
# 如果我们想在模块被引入时，
# 模块中的某一程序块不执行，
# 我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
#
# #!/usr/bin/python3
# # Filename: using_name.py
#
# if __name__ == '__main__':
#    print('程序自身在运行')
# else:
#    print('我来自另一模块')
# 运行输出如下：
#
# $ python using_name.py
# 程序自身在运行
# $ python
# >>> import using_name
# 我来自另一模块
# >>>
# 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，
# 表明该模块自身在运行，否则是被引入。
#
# 说明：__name__ 与 __main__ 底下是双下划线，
# _ _ 是这样去掉中间的那个空格。
# import tool
# # 并未引入时，默认为__main__
# print("__name__ = %s" % __name__)
# print("tool.printName() = %s" % tool.printName())

# dir() 函数
# 内置的函数 dir() 可以找到模块内定义的所有名称。以一个字符串列表的形式返回:
#
# import tool as t, sys
#
# print(dir(t))
# print(dir(sys))

# >>> import fibo, sys
# >>> dir(fibo)
# ['__name__', 'fib', 'fib2']
# >>> dir(sys)
# ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
#  '__package__', '__stderr__', '__stdin__', '__stdout__',
#  '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
#  '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
#  'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
#  'call_tracing', 'callstats', 'copyright', 'displayhook',
#  'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
#  'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
#  'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
#  'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
#  'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
#  'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
#  'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
#  'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
#  'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
#  'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
#  'thread_info', 'version', 'version_info', 'warnoptions']
# 如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
#
# import tool as t
#
# add = t.add
# a = 5
# print(dir())
# del a
# print(dir())

# >>> a = [1, 2, 3, 4, 5]
# >>> import fibo
# >>> fib = fibo.fib
# >>> dir() # 得到一个当前模块中定义的属性列表
# ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
# >>> a = 5 # 建立一个新的变量 'a'
# >>> dir()
# ['__builtins__', '__doc__', '__name__', 'a', 'sys']
# >>>
# >>> del a # 删除变量名a
# >>>
# >>> dir()
# ['__builtins__', '__doc__', '__name__', 'sys']
# >>>

# 标准模块
# Python 本身带着一些标准的模块库，
# 在 Python 库参考文档中将会介绍到（就是后面的"库参考文档"）。
#
# 有些模块直接被构建在解析器里，
# 这些虽然不是一些语言内置的功能，
# 但是他却能很高效的使用，
# 甚至是系统级调用也没问题。
#
# 这些组件会根据不同的操作系统进行不同形式的配置，
# 比如 winreg 这个模块就只会提供给 Windows 系统。
#
# 应该注意到这有一个特别的模块 sys ，
# 它内置在每一个 Python 解析器中。
# 变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串:
#
# >>> import sys
# >>> sys.ps1
# '>>> '
# >>> sys.ps2
# '... '
# >>> sys.ps1 = 'C> '
# C> print('Runoob!')
# Runoob!
# C>
# import sys
# from os import path
#
# print(sys.path[0])
# print(path)
#
# f = open("test\main.txt", "r")
# # f.writelines(['大家好\n', '我是Python3\n', '根地址:' + sys.path[0]+'\n'])
# # str = f.read()
# str = f.readlines()
# print('str=%s'%str)
# f.close()

# Python3 os文件和目录方法
# Python3 os.access() 方法
#
# 概述
# os.access() 方法使用当前的uid/gid尝试访问路径。
# 大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。
# GID为GroupId，即组ID，用来标识用户组的唯一标识符
# UID为UserId，即用户ID，用来标识每个用户的唯一标示符
# 语法
# access()方法语法格式如下：
#
# os.access(path, mode);
# 参数
# path -- 要用来检测是否有访问权限的路径。
#
# mode -- mode为F_OK，测试存在的路径，
# 或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
#
# os.F_OK: 作为access()的mode参数，测试path是否存在。
# os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
# os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
# os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
# 返回值
# 如果允许访问返回 True , 否则返回False。
#
# 实例
# 以下实例演示了 access() 方法的使用：
#
# #!/usr/bin/python3
#
# import os, sys
#
# # 假定 /tmp/foo.txt 文件存在，并有读写权限
#
# ret = os.access("/tmp/foo.txt", os.F_OK)
# print ("F_OK - 返回值 %s"% ret)
#
# ret = os.access("/tmp/foo.txt", os.R_OK)
# print ("R_OK - 返回值 %s"% ret)
#
# ret = os.access("/tmp/foo.txt", os.W_OK)
# print ("W_OK - 返回值 %s"% ret)
#
# ret = os.access("/tmp/foo.txt", os.X_OK)
# print ("X_OK - 返回值 %s"% ret)
# 执行以上程序输出结果为：
#
# F_OK - 返回值 True
# R_OK - 返回值 True
# W_OK - 返回值 True
# X_OK - 返回值 False
#
# import sys, os
#
# path = "test\copy.txt"
# ret = os.access(path, os.F_OK)
# print("{}的os.F_OK={}".format(path, ret))
#
# path = "test\\test.txt"
# ret = os.access(path, os.F_OK)
# print("{}的os.F_OK={}".format(path, ret))
#
# path = "test\copy.txt"
# ret = os.access(path, os.X_OK)
# print("{}的os.X_OK={}".format(path, ret))

# Python3 错误和异常
# 作为 Python 初学者，在刚学习 Python 编程时，
# 经常会看到一些报错信息，在前面我们没有提及，这章节我们会专门介绍。
#
# Python 有两种错误很容易辨认：语法错误和异常。
# Python assert（断言）用于判断一个表达式，
# 在表达式条件为 false 的时候触发异常。
#
# 语法错误
# Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例
# >>> while True print('Hello world')
#   File "<stdin>", line 1, in ?
#     while True print('Hello world')
#                    ^
# SyntaxError: invalid syntax
# 这个例子中，函数 print() 被检查到有错误，
# 是它前面缺少了一个冒号 : 。
#
# 语法分析器指出了出错的一行，
# 并且在最先找到的错误的位置标记了一个小小的箭头。

# 异常
# 即便 Python 程序的语法是正确的，在运行它的时候，
# 也有可能发生错误。运行期检测到的错误被称为异常。
#
# 大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:
#
# 实例

# >>> 10 * (1/0)             # 0 不能作为除数，触发异常
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# ZeroDivisionError: division by zero
# >>> (10/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# >>>

# >>> 4 + spam*3             # spam 未定义，触发异常
# Traceback (most recent call last):
#   File "<stdin>", line 1, in ?
# NameError: name 'spam' is not defined
# PyDev console: starting.
# Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:37:02) [MSC v.1924 64 bit (AMD64)] on win32
# hello*3
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# NameError: name 'hello' is not defined


# >>> '2' + 2               # int 不能与 str 相加，触发异常
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str
# '1'+2
# Traceback (most recent call last):
#   File "<input>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str

# 异常以不同的类型出现，
# 这些类型都作为信息的一部分打印出来:
# 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。
#
# 错误信息的前面部分显示了异常发生的上下文，
# 并以调用栈的形式显示具体信息。

# 异常处理
# try/except
# 异常捕捉可以使用 try/except 语句。


# a = 2020
# def test():
#     # global a
#     a = 33
#     print("in test(),a={}".format(a))
#
# test()
# print("in outer, a={}".format(a))

# list = [2020, '天青釉汝窑', True]
# print(list)
# myEnum = enumerate(list, start=10)
# for i, content in myEnum:
#     print("{} : {}".format(i, content))

#
# 以下例子中，让用户输入一个合法的整数，
# 但是允许用户中断这个程序
# （使用 Control-C 或者操作系统提供的方法）。
# 用户中断的信息会引发一个 KeyboardInterrupt 异常。
#
# while True:
#     try:
#         x = int(input("请输入一个数字: "))
#         break
#     except ValueError:
#         print("您输入的不是数字，请再次尝试输入！")
# try 语句按照如下方式工作；
#
# 首先，执行 try 子句
# （在关键字 try 和关键字 except 之间的语句）。
#
# 如果没有异常发生，
# 忽略 except 子句，try 子句执行后结束。
#
# 如果在执行 try 子句的过程中发生了异常，
# 那么 try 子句余下的部分将被忽略。
# 如果异常的类型和 except 之后的名称相符，
# 那么对应的 except 子句将被执行。
#
# 如果一个异常没有与任何的 except 匹配，
# 那么这个异常将会传递给上层的 try 中。

# while True:
#     try:
#         a = int(input("请输入一个数字\n"))
#         break
#     except ValueError as reason:
#         print("您输入的并非数字")
#

# 一个 try 语句可能包含多个except子句，
# 分别来处理不同的特定的异常。
# 最多只有一个分支会被执行。
#
# 处理程序将只针对对应的 try 子句中的异常进行处理，
# 而不是其他的 try 的处理程序中的异常。
#
# 一个except子句可以同时处理多个异常，
# 这些异常将被放在一个括号里成为一个元组，例如:
#
# except (RuntimeError, TypeError, NameError):
#     pass
# 最后一个except子句可以忽略异常的名称，
# 它将被当作通配符使用。
# 你可以使用这种方法打印一个错误信息，
# 然后再次把异常抛出。
#
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise

import sys

# # {0}{1}.format
# name = 'Cleopatra VII'
# nation = 'Egypt(Ptolemaic Dynasty)'
# myStr = '{0}:{0} lived in {1}'.format(name, nation)
# print(myStr)


# try:
#     f = open('word.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError:
#     print("OS Error:{}")
# except ValueError as result:
#     print("格式转换错误:{0}".format(result))
# except:
#     print("Unexpected error:{0}".format(sys.exc_info()[0]))

# # 类和对象
# class Student:
#     # 姓名
#     name: ''
#     no: ''
#     age = 0
#     score = -1
#
#     def __init__(self, name, no, age):
#         self.age = age
#         self.name = name
#         self.no = no
#         score = -1
#
#     # 打印信息
#     def printInfo(self):
#         print("-" * 15)
#         print("姓名:{0}".format(self.name))
#         print("学号:{0}".format(self.no))
#         print("年龄:{0}".format(self.age))
#         if self.score < 0:
#             print("未录入成绩")
#         else:
#             print("成绩:{0}".format(self.score))
#         print("-" * 15)
#
#     # 打印信息
#     def setScore(self, score):
#         self.score = score
#
#     @classmethod
#     def ViewInfo(cls):
#         print("类名：Student")
#
#     def __test(self, name):
#         print("测试私有方法,name={}".format(name))
#
#     def testPrivate(self):
#         self.__test("testPrivate")
#
# # 姓名 学号 年龄
# stu1 = Student('Tim', '20200803', 20)
# # stu1.printInfo()
# # stu1.setScore(95)
# # stu1.printInfo()
# # stu1.score = 90
# # stu1.printInfo()
# stu1.testPrivate()
# Student.ViewInfo()
#
# # print(10 / 3)

# class Car:
#     price = 300000
#
#     def __init__(self, name):
#         self.name = name
#         self.color = '  '
#
#     def setColor(self, color):
#         self.color = color
#
#     def printInfo(self):
#         print("我是汽车：{0}".format(self.name))
#
#
# # 子类 电动车
# class ECar(Car):
#     def __init__(self, name):
#         super().__init__(name)
#         self.batterySize = 0
#
#     def printInfo(self):
#         print("我是电动车：{0}，电池容量是{1}公里".format(self.name, self.batterySize))
#
#
# tesla = ECar('特斯拉')
# tesla.batterySize = 300
# tesla.printInfo()

# Python3 命名空间和作用域
# 命名空间的生命周期：
# 命名空间的生命周期取决于对象的作用域，
# 如果对象执行完成，
# 则该命名空间的生命周期就结束。
# 因此，
# 我们无法从外部命名空间访问内部命名空间的对象。
#
# 实例
# var1 是全局名称
# var1 = 5
#
#
# def some_func():
#     # var2 是局部名称
#     var2 = 6
#
#     def some_inner_func():
#         # var3 是内嵌的局部名称
#         var3 = 7
