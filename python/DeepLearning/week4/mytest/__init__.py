import numpy as np
import numpy.random
import matplotlib.pyplot as plt
from get_data import get_number

# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
# LEARNING_RATE = 学习率
# NET_DEEP_ARRAY = 神经网络的深度(输入层X为0)对应的神经元个数
# DEFAULT_TRAIN_TIMES = 默认训练次数
HIDDEN_LAYER_NUM = 5
LEARNING_RATE = 1.2
NET_DEEP_ARRAY = []
DEFAULT_TRAIN_TIMES = 5000
# RANDOM_SEED = 随机数的种子
RANDOM_SEED = 2021


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
def shallow_neural_network(X, Y
                           , net_deep_array=[0, 3, 5, 4, 2], learning_rate=LEARNING_RATE
                           , train_times=DEFAULT_TRAIN_TIMES, random_seed=RANDOM_SEED):
    # 绘图
    plt.title("week4 深层神经网络")
    plt.xlabel("x/times")
    plt.ylabel("损失值（越小越好）")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    x = []
    y = []
    y1 = []

    # 初始化基本参数
    net_deep = len(net_deep_array)
    net_deep_array[0] = X.shape[0]
    numpy.random.seed(random_seed)

    W1 = np.random.randn(HIDDEN_LAYER_NUM, X.shape[0]) * 0.01
    b1 = np.zeros(shape=(HIDDEN_LAYER_NUM, 1))
    W2 = np.random.randn(1, HIDDEN_LAYER_NUM) * 0.01
    b2 = np.zeros(shape=(1, 1))

    # 训练次数
    for i in range(0, train_times, 1):

        # 每次中的纵向深度
        for L in range(1, net_deep, 1):
            # 初始化参数W和B
            if L == 1:
                W = np.random.randn(net_deep_array[1], net_deep_array[1]) * 0.01
                b = np.zeros(shape=(net_deep_array[1], 1))

            # 进行前向传播
            forward_parameter = forward_propagation(X, {
                'W': W,
                'b': b,
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


if __name__ == '__main__':
    # 测试集进行学习的次数

    # 初始化训练的数据
    data_X, data_Y = get_number(10000)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)

    print(data_X.shape)
    print(data_Y.shape)

    parameter = shallow_neural_network(data_X, data_Y)

    # 初始化测试集的数据
    test_X, test_Y = get_number(8)
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)
    test_network(test_X, test_Y, parameter=parameter)
