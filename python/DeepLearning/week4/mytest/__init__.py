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
def forward_propagation(A_Last, parameter):
    W = parameter.get('W')
    b = parameter.get('b')

    Z = np.dot(W, A_Last) + b
    A = np.tanh(Z)

    return {
        'Z': Z,
        'A': A,
    }


# 计算该结果的成本
def cost(A, Y):
    A = np.squeeze(A)
    Y = np.squeeze(Y)
    assert (A.shape[0] == Y.shape[0])
    # 这里使用 np.multiply 是因为只有一维所以对应想乘
    temp = np.multiply(np.log(A), Y) + np.multiply((1 - Y), np.log(1 - A))
    # 取了一次绝对值
    temp = np.maximum(temp, -temp)
    cost_ret = np.sum(temp) * (1 / A.shape[0])
    return float(cost_ret)


# 浅层神经网络主驱动
def shallow_neural_network(X, Y
                           , net_deep_array=[0, 6, 1], learning_rate=LEARNING_RATE
                           , train_times=DEFAULT_TRAIN_TIMES, random_seed=RANDOM_SEED):
    # 绘图
    plt.title("week4 深层神经网络")
    plt.xlabel("x/times")
    plt.ylabel("损失值（越小越好）")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    x = []
    y = []

    # 初始化基本参数
    net_deep = len(net_deep_array)
    net_deep_array[0] = X.shape[0]
    numpy.random.seed(random_seed)
    m = X.shape[1]

    # 暂存每一个深度的参数值
    W = [np.array([])]
    b = [np.array([])]
    Z = [np.array([])]
    A = [X]
    # 后向传播用于梯度下降
    dZ = [np.array([])]
    dW = [np.array([])]
    db = [np.array([])]
    dA = [np.array([])]

    # 训练次数
    for i in range(0, train_times, 1):
        # 每次前向传播中的纵向深度
        for L in range(1, net_deep, 1):
            # 初始化参数W和B
            if i == 0:
                W.append(np.array([]))
                b.append(np.array([]))
                Z.append(np.array([]))
                A.append(np.array([]))
                dW.append(np.array([]))
                db.append(np.array([]))
                dZ.append(np.array([]))
                dA.append(np.array([]))
                W[L] = np.random.randn(net_deep_array[L], net_deep_array[L - 1]) * 0.01
                b[L] = np.zeros(shape=(net_deep_array[L], 1))
            # 进行前向传播
            forward_parameter = forward_propagation(A[L - 1], {
                'W': W[L],
                'b': b[L],
            })
            Z[L] = forward_parameter.get('Z')
            A[L] = forward_parameter.get('A')

        # 计算成本cost
        cost_value = cost(A[net_deep - 1], Y)
        if i % 50 == 0:
            x.append(i)
            y.append(cost_value)

        # 后向传播用于梯度下降
        # 倒序计算出
        dA[net_deep - 1] = np.multiply(
            (-1) * Y / A[net_deep - 1] + (1 - Y) / (1 - A[net_deep - 1])
            , (1 - np.tanh(Z[net_deep - 1]) * np.tanh(Z[net_deep - 1])))
        for L in range(net_deep - 1, 0, -1):
            dZ[L] = np.multiply(dA[L], (1 - np.tanh(Z[L]) * np.tanh(Z[L])))
            dW[L] = (1 / m) * (np.dot(dZ[L], A[net_deep - 1].T))
            db[L] = (1 / m) * np.sum(dZ[L], axis=1, keepdims=True)
            dA[L - 1] = np.dot(W[L].T, dZ[L])
            # 更新参数
            W[L] = W[L] - learning_rate * dW[L]
            b[L] = b[L] - learning_rate * db[L]

    # plt.plot(x, y)
    plt.plot(x, y, color='orange')
    plt.show()

    parameter = {
        'W': W,
        'b': b,
    }
    return parameter


# 对浅层神经网络得出的结果进行测试
def test_network(X, Y, parameter):
    W = parameter.get('W')
    b = parameter.get('b')
    A = [X]
    net_deep = len(W)
    for L in range(1, net_deep, 1):
        # 初始化参数W和B
        # 进行前向传播
        forward_parameter = forward_propagation(A[L - 1], {
            'W': W[L],
            'b': b[L],
        })
        A.append(np.array([]))
        A[L] = forward_parameter.get('A')
    # 计算成本cost
    cost_value = cost(A[net_deep - 1], Y)

    print(A[net_deep - 1])
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
    data_X, data_Y = get_number(5000)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)

    print(data_X.shape)
    print(data_Y.shape)

    parameter = shallow_neural_network(data_X, data_Y, train_times=5000)

    # 初始化测试集的数据
    test_X, test_Y = get_number(10)
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)
    test_network(test_X, test_Y, parameter=parameter)
