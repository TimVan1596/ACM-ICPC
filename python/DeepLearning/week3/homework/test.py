import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
# LEARNING_RATE = 学习率
HIDDEN_LAYER_NUM = 12
LEARNING_RATE = 1.2


# 激活函数
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


if __name__ == '__main__':
    # 绘图
    plt.title("week3 浅层的神经网络")
    plt.xlabel("x/times")
    plt.ylabel("J")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

    x = []
    y = []
    y1 = []

    # 设置随机种子
    numpy.random.seed(20210922)

    # 初始化大写 X
    X = np.array([
        [220, 1100, 100, 500, 300, 100, 400, 848, 1, 0, 2, 8, 2, 0, 100, 200],
        [221, 600, 120, 600, 1000, 200, 500, 35153, 1, 0, 2, 1, 1, 5, 200, 300],
        [290, 800, 130, 700, 2000, 300, 600, 5245, 1, 0, 3, 2, 3, 9, 300, 400],
    ])
    print('X=')
    print(X)
    print()

    # 初始化大写Y
    Y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1])
    W1 = np.random.randn(HIDDEN_LAYER_NUM, X.shape[0]) * 0.01
    b1 = np.zeros(shape=(HIDDEN_LAYER_NUM, X.shape[1]))
    W2 = np.random.randn(1, HIDDEN_LAYER_NUM) * 0.01
    b2 = np.zeros(shape=(1, X.shape[1]))

    for i in range(0, 40000, 1):

        # Z1 = W1.dot(X) + b1
        Z1 = np.dot(W1, X) + b1
        # print('Z1=')
        # print(Z1)
        # print()

        A1 = np.tanh(Z1)
        # print('A1=')
        # print(A1)
        # print()

        # W2 = np.random.randn(
        #     1, HIDDEN_LAYER_NUM
        # )

        # print('W2=')
        # print(W2)
        # print()

        # print('b2=')
        # print(b2)
        # print()

        # Z2 = W2.dot(A1) + b2
        Z2 = np.dot(W2, A1) + b2
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
        # d_Z1 = np.multiply(np.dot(W2.T, d_Z2), 1 - np.power(A1, 2))
        # print('d_Z1=')
        # print(d_Z1)
        # print()

        d_W1 = (1 / X.shape[1]) * d_Z1.dot(X.T)
        # print('d_W1=')
        # print(d_W1)
        # print()

        # d_b1 = np.sum(d_Z1, axis=1, keepdims=True)
        d_b1 = (1 / X.shape[1]) * np.sum(d_Z1, axis=1, keepdims=True)
        # print('d_b1=')
        # print(d_b1)
        # print()

        # print(np.squeeze(A2))
        # print(Y)

        # 计算成本
        ret = np.multiply(Y, np.log(A2)) + np.multiply((1 - Y), np.log(1 - A2))
        J = np.squeeze((-1 / X.shape[1]) * np.sum(ret, axis=1, keepdims=True))

        logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
        cost = - np.sum(logprobs) / X.shape[1]
        cost = float(np.squeeze(cost))

        # print('J=')
        # print(J)
        # print()

        # x.append(i)
        # y.append(J)

        if i % 50 == 0:
            print("-" * 15)
            print("开始第{0}轮".format(i + 1))
            print("-" * 15)

            # 初始化大写 W
            # print('W1=')
            # print(W1)
            # print()
            #
            # print('b1=')
            # print(b1)
            # print()
            #
            print('J=')
            print(J)
            print()

            x.append(i)
            y.append(J)
            y1.append(cost)

        W1 = W1 - LEARNING_RATE * d_W1
        b1 = b1 - LEARNING_RATE * d_b1
        W2 = W2 - LEARNING_RATE * d_W2
        b2 = b2 - LEARNING_RATE * d_b2

    # plt.plot(x, y)
    plt.plot(x, y1, color='orange')
    plt.show()

    print("-" * 30)
    print("最终结果为")
    print('W=')
    print(W1)
    print()

    print('b1=')
    print(b1)
    print()
