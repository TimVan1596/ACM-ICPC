import numpy as np


# 激活函数
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


if __name__ == '__main__':
    np.random.seed(1)
    A1 = np.random.randn(1, 3)
    print(A1)

    D1 = np.random.rand(A1.shape[0], A1.shape[1])
    print(D1)
    keep_prob = 0.5
    D1 = D1 < keep_prob
    print(D1)

    A1 = A1 * D1
    # A1 = A1 / keep_prob
    print(A1)
