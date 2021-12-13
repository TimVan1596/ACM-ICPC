import numpy
from matplotlib import pyplot as plt
import numpy as np
import math


# 将字符串按空格转list
def str_to_list(str):
    cache = str.split()
    if '.' in str:
        return [float(elem) for elem in cache]
    else:
        return [int(elem) for elem in cache]


# 获取数据
def get_data(t_str, P_str):
    t = str_to_list(t_str)
    P = str_to_list(P_str)
    return t, P


# 初始化matplotlib.pyplot
# y是真实值的list，f是拟合后的list
def initial_plt(x, y, xx, f, is_show=True):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel('t/min 时间')
    plt.ylabel('P 所占产物的百分比')
    plt.title('插值')

    plt.scatter(x, y, linewidth=2, color='orange', label='真实')
    plt.plot(xx, f, linewidth=2, color='dodgerblue', label='三次样条')
    # plt.scatter(xx, f, linewidth=3, color='green', label='样条取点')

    plt.legend(loc='upper left')
    plt.savefig("result_2.png")
    if is_show:
        plt.show()


# num是自变量
def solve(x: int, y: float, M: list, j: int, num: int):
    M_j = M[j]
    M_j1 = M[j + 1]

    x_j = x[j]
    x_j1 = x[j + 1]

    y_j = y[j]
    y_j1 = y[j + 1]

    temp1 = (M_j * ((x_j1 - num) ** 3)) / 60
    temp2 = (M_j1 * ((num - x_j) ** 3)) / 60
    temp3 = (y_j - (M_j * 100) / 6) * ((x_j1 - num) / 10)
    temp4 = (y_j1 - (M_j1 * 100) / 6) * ((num - x_j) / 10)

    sum_v = temp1 + temp2 + temp3 + temp4
    return sum_v


if __name__ == '__main__':

    M = [0, -0.0020125, -0.00075, -0.0006875, 0]
    x = [0, 10, 20, 30, 40]
    y = [0, 2.16, 3.44, 4.15, 4.51]
    n = len(M) - 1
    xx = []
    fx = []
    for i in range(0, 41):
        j = int(i / 10)
        if j >= 4:
            j = 3
        value = solve(num=i, j=j, M=M, x=x, y=y)
        xx.append(i)
        fx.append(value)

    # print(fx)

    # 图表设置
    initial_plt(x, y, xx, fx, is_show=True)
