# 根据提示，在右侧编辑器补充代码，编程计算公式的微分求导。
#
# 其中formula变量保存要求输入一个包含x变量的公式，请通过使用exec()函数将输入的公式转换为 Python 可执行的函数。
#
# 按照微分求导公式编写一个微分求导的函数，参数为：
# （1）待求导的公式；(2)x的值；
# （3）一个足够小的数h，函数返回值为该x点的导数。微分求导公式（h的值取 1E-5 ）如下：
#
#
#
# 将结果保留两位小数输出：
#
# print("%.2f" % output_val)

# coding=utf-8
from math import *

formula = '2*x+x**3'

# def fun(x):
#     return x * x + 2 * x


# 请在此处填写代码
# ********** Begin **********#
real_x = float(input())

h = 1E-5

x = real_x + h
result_plus = eval(formula)
x = real_x - h
result_minus = eval(formula)
derivative = (result_plus - result_minus) / (2 * h)
print("%.2f" % derivative)
# ********** End **********#


