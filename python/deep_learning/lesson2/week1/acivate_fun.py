import numpy as np
import math


# 激活函数

# sigmoid函数
def sigmoid(x):
    x_ravel = x.ravel()  # 将numpy数组展平
    length = len(x_ravel)
    y = []
    for index in range(length):
        curr = x_ravel[index]
        if curr >= 0:
            a = math.exp(-curr)
            y.append(1.0 / (1 + a))
        else:
            a = math.exp(curr)
            y.append(a / (a + 1))

    return np.array(y).reshape(x.shape)


# sigmoid函数
def d_sigmoid(x):
    return pow(sigmoid(x), 2)


# relu函数
def ReLU(x):
    return 1 * (x > 0) * x


def d_ReLU(x):
    y = (x > 0) * 1
    return y


if __name__ == '__main__':
    arr = np.array([
        [19, 44]
        , [20, -21]
        , [10, -3]
    ])

    print(arr.shape)
    print(ReLU(arr))
    print(d_ReLU(arr))
