import numpy as np


# 激活函数
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


if __name__ == '__main__':
    a = np.array([[1, 2, 3]])
    assert a.shape == (1, 3)

    a = np.squeeze(a)
    print(a.shape)

    ret = sigmoid(np.array([-10000000, -4, -3, -2, -1, 0, 1, 2, 3, 4]))
    print(ret)
