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
