# -*- coding:utf-8 -*-
# @Time:2020/6/12 12:29
# @Author:TimVan
# @File:函数练习.py
# @Software:PyCharm


# 课堂练习：
# 1.写一个打印一条横线的函数。（提示：横线是若干个“-”组成）
# 2.写一个函数，可以通过输入的参数，打印出自定义行数的横线。（提示：调用上面的函数）
# 3.写一个函数求三个数的和
# 4.写一个函数求三个数的平均值（提示：调用上面的函数）

# 1.写一个打印一条横线的函数。（提示：横线是若干个“-”组成）
def printLine():
    print("-" * 30)


# 2.写一个函数，可以通过输入的参数，打印出自定义行数的横线。（提示：调用上面的函数）
def printMultiplyLine(n):
    i = 0
    for i in range(n):
        printLine()


# 3.写一个函数求三个数的和
def getThreeNumSum(a, b, c):
    return a + b + c


# 4.写一个函数求三个数的平均值（提示：调用上面的函数）
def getThreeNumAvg(a, b, c):
    return getThreeNumSum(a, b, c) / 3


printLine()
lineNum: str = input("请输入行数\n")
printMultiplyLine(int(lineNum))

print(getThreeNumSum(1, 2, 3))
print(getThreeNumAvg(1, 2, 3))
