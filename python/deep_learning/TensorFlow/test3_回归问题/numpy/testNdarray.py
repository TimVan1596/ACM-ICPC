# -*- coding:utf-8 -*-
# @Time:2020/8/31 19:54
# @Author:TimVan
# @File:testNdarray.py
# @Software:PyCharm
import numpy as np


def testNdarray():
    a = np.array([19, 55])
    print(a, end="\n------\n")
    a = np.array([[19, 55, 0], [2020, 8, 31]])
    print(a, end="\n------\n")
    # 设置最小维度
    a = np.array([[19, 55, 0], [2020, 8, 31]], ndmin=3)
    print(a, end="\n------\n")
    # 设置dType
    a = np.array([[19, 55, 0], [2020, 8, 31]], ndmin=3, dtype=complex)
    print(a, end="\n------\n")


if __name__ == '__main__':
    testNdarray()
