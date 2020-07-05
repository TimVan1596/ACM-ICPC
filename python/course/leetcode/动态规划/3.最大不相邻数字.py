# -*- coding:utf-8 -*-
# @Time:2020/7/5 16:11
# @Author:TimVan
# @File:3.最大不相邻数字.py
# @Software:PyCharm

# 3.最大不相邻数字
# 给一组数列，选出其中不相邻的一组数字，返回选出数字相加的最大值
def getMaxNonAdjacent(arr: list) -> int:
    arrLen = len(arr)
    opt = [0] * arrLen
    opt[0] = arr[0]
    print("opt[%d] = %d" % (0, opt[0]))
    i = 1
    while i < arrLen:
        # 第二个数特殊处理
        if i == 1:
            opt[1] = max(arr[0], arr[1])
        else:
            opt[i] = max(opt[i - 2] + arr[i], opt[i - 1])
        print("opt[%d] = %d" % (i, opt[i]))
        i += 1
    return opt[arrLen - 1]


inputArr = [
    [1, 2, 4, 1, 7, 8, 3],
    [99, 1, 99, 1, 99, 1000],
    [4, 1, 1, 9, 1],
]
for one in inputArr:
    print("-> %d" % getMaxNonAdjacent(one))
