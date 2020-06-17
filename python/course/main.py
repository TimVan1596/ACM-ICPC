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

a = 50
a //= 3
print(a)
