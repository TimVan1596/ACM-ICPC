# -*- coding:utf-8 -*-
# @Time:2020/5/3011:41
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
userName = input("请输入你的用户名\n")
age = input("请输入您的年龄\n")
print("您的用户名为%s,年龄为%d" % (userName, int(age)))
print("type(age) = ", type(age))
