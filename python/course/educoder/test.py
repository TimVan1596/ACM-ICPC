# coding:utf-8
from math import sqrt

a = float(input());
b = float(input());
c = float(input())


def roots(a, b, c):
    # 请在此添加代码，求方程 ax^2+bx+c = 0的解,返回由方程根构成的列表,若方程有无数解，返回['inf']
    # ********** Begin *********#
    delta = b * b - 4 * a * c
    if delta < 0:
        return ['inf']
    else:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = ((-b) / a) - x1
        return [x1, x2]


# ********** End **********#
print(roots(a, b, c))
