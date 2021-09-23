import numpy as np
import numpy.random
import matplotlib.pyplot as plt


# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
HIDDEN_LAYER_NUM = 4


# 激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


if __name__ == '__main__':
    # 绘图
    plt.title("week3 浅层的神经网络")
    plt.xlabel("x/times")
    plt.ylabel("J")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

    x = []
    y = []

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

    W1 = np.random.uniform(-1, 1, size=(HIDDEN_LAYER_NUM, X.shape[0]))
    b1 = np.random.uniform(-1, 1, size=(HIDDEN_LAYER_NUM, X.shape[1]))

    for i in range(0, 1000, 1):
        print("-" * 15)
        print("开始第{0}轮".format(i + 1))
        print("-" * 15)

        # 初始化大写 W
        print('W1=')
        print(W1)
        print()

        print('b1=')
        print(b1)
        print()

        Z1 = W1.dot(X) + b1
        # print('Z1=')
        # print(Z1)
        # print()

        A1 = np.tanh(Z1)
        # print('A1=')
        # print(A1)
        # print()

        W2 = np.random.uniform(-1, 1, size=(1, HIDDEN_LAYER_NUM))
        # print('W2=')
        # print(W2)
        # print()

        b2 = np.random.uniform(-1, 1, size=(1, X.shape[1]))
        # print('b2=')
        # print(b2)
        # print()

        Z2 = W2.dot(A1) + b2
        # print('Z2=')
        # print(Z2)
        # print()

        A2 = sigmoid(Z2)
        # print('A2=')
        # print(A2)
        # print()

        d_Z2 = A2 - Y
        # print('d_Z2=')
        # print(d_Z2)
        # print()

        d_W2 = (1 / X.shape[1]) * (d_Z2.dot(A1.T))
        # print('d_W2=')
        # print(d_W2)
        # print()

        d_b2 = (1 / X.shape[1]) * np.sum(d_Z2, axis=1, keepdims=True)
        # print('d_b2=')
        # print(d_b2)
        # print()

        d_Z1 = np.multiply((W2.T.dot(d_Z2)), (1 - np.tanh(Z1) * np.tanh(Z1)))
        # print('d_Z1=')
        # print(d_Z1)
        # print()

        d_W1 = (1 / X.shape[1]) * d_Z1.dot(X.T)
        # print('d_W1=')
        # print(d_W1)
        # print()

        d_b1 = np.sum(d_Z1, axis=1, keepdims=True)
        # print('d_b1=')
        # print(d_b1)
        # print()

        print(np.squeeze(A2))
        print(Y)

        # 计算成本
        ret = np.multiply(Y, np.log(A2)) + np.multiply((1 - Y), np.log(1 - A2))
        J = np.squeeze((1 / X.shape[1]) * np.sum(ret, axis=1, keepdims=True))
        print('J=')
        print(J)
        print()

        x.append(i)
        y.append(J)

        W1 = W1 + d_W1
        b1 = b1 + d_b1

    plt.plot(x, y)
    plt.show()
