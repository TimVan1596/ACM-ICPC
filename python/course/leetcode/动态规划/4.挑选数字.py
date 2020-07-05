# -*- coding:utf-8 -*-
# @Time:2020/7/5 18:37
# @Author:TimVan
# @File:4.挑选数字.py
# @Software:PyCharm

# 挑选数字
# 给定一组数字，若可挑选某些数字使得它们相加符合目标，则返回true，否则返回false

def isConformTarget(num: int, target: int) -> bool:

    return True

def isConformTargetDriver(arr: list, target: int) -> bool:

    return True


inputArr = [
    ([1, 2, 4, 1, 7, 8, 3], 5),
    ([99, 1, 99, 1, 99, 1000], 3),
    ([4, 1, 1, 9, 1], 10),
]
for one in inputArr:
    print("-> %s" % isConformTarget(one[0], one[1]))
