# -*- coding:utf-8 -*-
# @Time:2020/7/1 13:11
# @Author:TimVan
# @File:1.斐波拉契数列.py
# @Software:PyCharm

# O(n)的斐波拉契数列
def getFiboracciArr(index: int) -> int:
    fibDict = {1: 1, 2: 1}
    current = 2
    while current < index:
        current += 1
        fibDict[current] = fibDict.get(current - 1, 1) + fibDict.get(current - 2, 1)

    return fibDict.get(index, 1)


inputArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for one in inputArr:
    print("%d->" % one, getFiboracciArr(one))
