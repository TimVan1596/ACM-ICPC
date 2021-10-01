import numpy as np
import numpy.random
import matplotlib.pyplot as plt

# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
# LEARNING_RATE = 学习率
HIDDEN_LAYER_NUM = 6
LEARNING_RATE = 1.2


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
    # 这里使用 np.multiply 是因为只有一维所以对应想乘
    temp = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
    print(temp.shape)
    print(temp)


# 浅层神经网络主驱动
def shallow_neural_network(X, Y, round=5000):
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

    W1 = np.random.randn(HIDDEN_LAYER_NUM, X.shape[0]) * 0.01
    b1 = np.zeros(shape=(HIDDEN_LAYER_NUM, 1))
    W2 = np.random.randn(1, HIDDEN_LAYER_NUM) * 0.01
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

        d_Z2 = A2 - Y
        d_W2 = (1 / X.shape[1]) * (d_Z2.dot(A1.T))
        d_b2 = (1 / X.shape[1]) * np.sum(d_Z2, axis=1, keepdims=True)
        d_Z1 = np.multiply((W2.T.dot(d_Z2)), (1 - np.tanh(Z1) * np.tanh(Z1)))
        d_W1 = (1 / X.shape[1]) * d_Z1.dot(X.T)
        d_b1 = (1 / X.shape[1]) * np.sum(d_Z1, axis=1, keepdims=True)

        # 计算成本
        ret = np.multiply(Y, np.log(A2)) + np.multiply((1 - Y), np.log(1 - A2))
        J = np.squeeze((-1 / X.shape[1]) * np.sum(ret, axis=1, keepdims=True))

        logprobs = np.multiply(np.log(A2), Y) + np.multiply((1 - Y), np.log(1 - A2))
        cost = - np.sum(logprobs) / X.shape[1]
        cost = float(np.squeeze(cost))

        if i % 50 == 0:
            x.append(i)
            y.append(J)
            y1.append(cost)

        W1 = W1 - LEARNING_RATE * d_W1
        b1 = b1 - LEARNING_RATE * d_b1
        W2 = W2 - LEARNING_RATE * d_W2
        b2 = b2 - LEARNING_RATE * d_b2

    # plt.plot(x, y)
    plt.plot(x, y1, color='orange')
    # plt.show()

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
    cost(A2, Y)


if __name__ == '__main__':
    # 测试集进行学习的次数
    round = 5000

    # 初始化训练的数据
    data_X = np.array([
        [220, 1100, 100, 500, 300, 100, 400, 848, 1, 0, 2, 8, 2, 0, 100, 200],
        [221, 600, 120, 600, 1000, 200, 500, 35153, 1, 0, 2, 1, 1, 5, 200, 300],
        [290, 800, 130, 700, 2000, 300, 600, 5245, 1, 0, 3, 2, 3, 9, 300, 400],
    ])
    data_Y = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1])
    parameter = shallow_neural_network(data_X, data_Y)

    # 初始化测试集的数据
    test_X = np.array([
        [1, 600, 0],
        [2, 300, 4],
        [5, 500, 2]
    ])
    test_Y = np.array([0, 1, 0])
    test_network(test_X, test_Y, parameter=parameter)
