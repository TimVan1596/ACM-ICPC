import numpy as np


# 激活函数
def activate():
    pass


if __name__ == '__main__':
    # 初始化大写 X
    X = np.array([
        [20, 11],
        [21, 6],
        [9, 8],
    ])
    print('X=')
    print(X)
    print()

    # 初始化大写 W
    W1 = np.array([
        [1, 4, 7, 7],
        [2, 5, 8, 6],
        [3, 6, 9, 2],
    ])
    W1 = W1.T
    print('W1=')
    print(W1)
    print()

    # 初始化 B
    # b1 = np.random.randint(1, 1, size=(4, 2))
    b1 = np.zeros((4, 2),dtype=int)
    print('b1=')
    print(b1)
    print()

    Z1 = W1.dot(X) + b1
    print(Z1)
