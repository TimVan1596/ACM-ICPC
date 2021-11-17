# coding:utf-8
import math
from math import sqrt


def Vieta():
    # 请在此输入代码
    # ********** Begin *********#
    # i=0,1的a值为1
    a = math.sqrt(2) / 2
    yield a
    while True:
        a = math.sqrt((1 + a) / 2)
        yield a


# **********  End  *********#

N = int(input())
v = Vieta();
p = 1.0

for i in range(N + 1):
    # 请在此输入代码
    # ********** Begin *********#
    p *= next(v)
    # **********  End  *********#

print("%.6f" % (2.0 / p))
