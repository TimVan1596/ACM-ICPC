import numpy as np
import numpy.random

# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
HIDDEN_LAYER_NUM = 4


# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    # 设置随机种子
    numpy.random.seed(20210922)

    # 初始化大写 X
    X = np.array([
        [20, 11],
        [21, 6],
        [9, 8],
    ])
    print('X=')
    print(X)
    print()

    # 初始化大写Y
    Y = np.array([0, 1])

    # 初始化大写 W
    W1 = np.random.uniform(-1, 1, size=(HIDDEN_LAYER_NUM, X.shape[0]))
    print('W1=')
    print(W1)
    print()

    # 初始化 B
    # b1 = np.random.randint(1, 1, size=(4, 2))
    b1 = np.random.uniform(-1, 1, size=(HIDDEN_LAYER_NUM, X.shape[1]))
    print('b1=')
    print(b1)
    print()

    Z1 = W1.dot(X) + b1
    print('Z1=')
    print(Z1)
    print()

    A1 = np.tanh(Z1)
    print('A1=')
    print(A1)
    print()

    W2 = np.random.uniform(-1, 1, size=(1, HIDDEN_LAYER_NUM))
    print('W2=')
    print(W2)
    print()

    b2 = np.random.uniform(-1, 1, size=(1, X.shape[1]))
    print('b2=')
    print(b2)
    print()

    Z2 = W2.dot(A1) + b2
    print('Z2=')
    print(Z2)
    print()

    A2 = sigmoid(Z2)
    print('A2=')
    print(A2)
    print()

    d_Z2 = A2 - Y
    print('d_Z2=')
    print(d_Z2)
    print()

    d_W2 = (1 / X.shape[1]) * (d_Z2.dot(A1.T))
    print('d_W2=')
    print(d_W2)
    print()

    d_b2 = (1 / X.shape[1]) * np.sum(d_Z2, axis=1, keepdims=True)
    print('d_b2=')
    print(d_b2)
    print()

    print('np.sum(d_Z2, axis=1, keepdims=True)=')
    print(np.sum(d_Z2, axis=1, keepdims=True))
    print()

    print('np.sum(d_Z2, axis=1)=')
    print(np.sum(d_Z2, axis=1))
    print()

    print('np.sum(d_Z2)=')
    print(np.sum(d_Z2))
    print()
