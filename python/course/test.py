import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

if __name__ == '__main__':
    x = np.linspace(1, 100, 100)
    y = np.linspace(30, 70, 100)
    v0 = 0
    beta = 0.9

    vv0 = y[0]
    v = []
    vv = []
    for i in range(1, len(y) + 1):
        value = y[i - 1]
        v0 = (beta * v0 + (1 - beta) * value)
        vv0 = (beta * vv0 + (1 - beta) * value)
        v.append(v0 / (1 - (beta ** i)))
        vv.append(vv0)
    plt.xlim(1, 100)
    plt.ylim(1, 100)
    plt.plot(x, y, label='原始')
    plt.scatter(x, v, label='指数加权平均', linewidth=3, color='green')
    plt.plot(x, vv, label='V0=θ0', linewidth=3, color='red')
    plt.legend()
    plt.show()
