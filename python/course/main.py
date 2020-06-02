# -*- coding:utf-8 -*-
# @Time:2020/5/30 11:41
# @Author:TimVan
# @File:main.py
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

for i in range(0,5,2):
    print(i)


