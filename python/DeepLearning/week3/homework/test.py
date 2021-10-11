import numpy as np
import numpy.random
import matplotlib.pyplot as plt

import random
import math

# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
# LEARNING_RATE = 学习率
HIDDEN_LAYER_NUM = 8
LEARNING_RATE = 0.8


# 激活函数
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


# 进行前向传播，即给数据得出结果
def forward_propagation(X, parameter):
    W1 = parameter.get('W1')
    b1 = parameter.get('b1')
    W2 = parameter.get('W2')
    b2 = parameter.get('b2')

    Z1 = np.dot(W1, X) + b1
    A1 = np.tanh(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    return {
        'Z1': Z1,
        'A1': A1,
        'Z2': Z2,
        'A2': A2,
    }


# 计算该结果的成本
def cost(A2, Y):
    A2 = np.squeeze(A2)
    Y = np.squeeze(Y)
    assert (A2.shape[0] == Y.shape[0])
    # 这里使用 np.multiply 是因为只有一维所以对应想乘
    temp = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
    # 取了一次绝对值
    temp = np.maximum(temp, -temp)
    cost_ret = np.sum(temp) * (1 / A2.shape[0])
    return float(cost_ret)


# 浅层神经网络主驱动
def shallow_neural_network(X, Y, round=5000):
    # 绘图
    plt.title("week3 浅层的神经网络")
    plt.xlabel("x/times")
    plt.ylabel("损失值（越小越好）")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置

    x = []
    y = []
    y1 = []

    # 设置随机种子
    numpy.random.seed(20210922)

    W1 = np.random.randn(HIDDEN_LAYER_NUM, X.shape[0]) * 0.001
    b1 = np.zeros(shape=(HIDDEN_LAYER_NUM, 1))
    W2 = np.random.randn(1, HIDDEN_LAYER_NUM) * 0.001
    b2 = np.zeros(shape=(1, 1))

    for i in range(0, round, 1):
        # 进行前向传播
        forward_parameter = forward_propagation(X, {
            'W1': W1,
            'b1': b1,
            'W2': W2,
            'b2': b2,
        })
        A1 = forward_parameter.get('A1')
        Z1 = forward_parameter.get('Z1')
        A2 = forward_parameter.get('A2')
        cost_value = cost(A2, Y)

        d_Z2 = A2 - Y
        d_W2 = (1 / X.shape[1]) * (d_Z2.dot(A1.T))
        d_b2 = (1 / X.shape[1]) * np.sum(d_Z2, axis=1, keepdims=True)
        d_Z1 = np.multiply((W2.T.dot(d_Z2)), (1 - np.tanh(Z1) * np.tanh(Z1)))
        d_W1 = (1 / X.shape[1]) * d_Z1.dot(X.T)
        d_b1 = (1 / X.shape[1]) * np.sum(d_Z1, axis=1, keepdims=True)

        if i % 50 == 0:
            x.append(i)
            y.append(cost_value)
            if i % 200 == 0:
                print("第", i, "次迭代，成本值为：", np.squeeze(cost_value))

        W1 = W1 - LEARNING_RATE * d_W1
        b1 = b1 - LEARNING_RATE * d_b1
        W2 = W2 - LEARNING_RATE * d_W2
        b2 = b2 - LEARNING_RATE * d_b2

    # plt.plot(x, y)
    plt.plot(x, y, color='orange')
    plt.show()

    parameter = {
        'W1': W1,
        'b1': b1,
        'W2': W2,
        'b2': b2,
    }
    return parameter


# 对浅层神经网络得出的结果进行测试
def test_network(X, Y, parameter):
    forward_parameter = forward_propagation(X, parameter)
    A2 = forward_parameter.get('A2')
    cost_value = cost(A2, Y)
    print(X)
    print(A2)
    print(Y)
    print("cost_value=" + str(cost_value))


def load_planar_dataset():
    np.random.seed(1)
    m = 400  # number of examples
    N = int(m / 2)  # number of points per class
    D = 2  # dimensionality
    X = np.zeros((m, D))  # data matrix where each row is a single example
    Y = np.zeros((m, 1), dtype='uint8')  # labels vector (0 for red, 1 for blue)
    a = 4  # maximum ray of the flower

    for j in range(2):
        ix = range(N * j, N * (j + 1))
        t = np.linspace(j * 3.12, (j + 1) * 3.12, N) + np.random.randn(N) * 0.2  # theta
        r = a * np.sin(4 * t) + np.random.randn(N) * 0.2  # radius
        X[ix] = np.c_[r * np.sin(t), r * np.cos(t)]
        Y[ix] = j

    X = X.T
    Y = Y.T

    return X, Y


# 获得数据
# num = 样本数量
def get_number(num):
    X = [
        [],
        [],
        []
    ]
    Y = []
    i = 0
    for i in range(num):
        x = random.randint(0, 40)
        y = random.randint(0, 100)
        z = random.randint(0, 100)
        temp = math.pow(x, 2) - 3 * y - 3 * z
        result = 1
        if temp < 0:
            result = 0
        X[0].append(x)
        X[1].append(y)
        X[2].append(z)
        Y.append(result)
        # print("-- 当 i =" + str(i))
        # print("x=" + str(x))
        # print("y=" + str(y))
        # print("z=" + str(z))
        # print("temp=" + str(temp))
        # print("result=" + str(result))
        # print("-" * 10)
    return X, Y


if __name__ == '__main__':
    # 测试集进行学习的次数

    # 初始化训练的数据
    # data_X = np.array([
    #     [220, 1100, 100, 500, 300, 100, 400, 848, 1, 0, 2, 8, 2, 0, 100, 200],
    #     [221, 600, 120, 600, 1000, 200, 500, 35153, 1, 0, 2, 1, 1, 5, 200, 300],
    #     [290, 800, 130, 700, 2000, 300, 600, 5245, 1, 0, 3, 2, 3, 9, 300, 400],
    # ])
    # data_Y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1])

    data_X, data_Y = get_number(4000)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)
    print(data_X.shape)
    print(data_Y.shape)

    parameter = shallow_neural_network(data_X, data_Y, round=3500)

    # 初始化测试集的数据
    test_X, test_Y = get_number(10)
    # test_X = [
    #     [0, 10],
    #     [100, 100],
    #     [100, 1000],
    # ]
    # test_Y = [0, 1]
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)
    test_network(test_X, test_Y, parameter=parameter)
