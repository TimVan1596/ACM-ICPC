# coding:utf-8
from math import sin, cos

delX = 0.001

x = float((2.4))


def diff(f):
    # 请在此添加代码，求出函数f的导数
    # ********** Begin *********#
    return lambda x: (f(x + delX) - f(x - delX)) / (2 * delX)
    # **********  End  *********#


print("%.2f" % (diff(sin)(x)))
