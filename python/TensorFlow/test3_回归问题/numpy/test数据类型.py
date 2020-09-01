# -*- coding:utf-8 -*-
# @Time:2020/9/1 5:37
# @Author:TimVan
# @File:test数据类型.py
# @Software:PyCharm
import numpy as np


def testNdarray():
    # dt = np.dtype(np.int_)
    # print(dt)
    x = np.empty([3, 2], dtype=int)
    print(x)


if __name__ == '__main__':
    testNdarray()
