import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import random

# 设置常量
# HIDDEN_LAYER_NUM = 隐层的个数
# LEARNING_RATE = 学习率
# NET_DEEP_ARRAY = 神经网络的深度(输入层X为0)对应的神经元个数
# DEFAULT_TRAIN_TIMES = 默认训练次数
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


# 深层神经网络主驱动
def deep_neural_network(X, Y
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
    W, b = initial_parameters(net_deep_array)

    # 暂存每一个深度的参数值
    Z = [0] * net_deep
    A = [0] * net_deep
    # 后向传播用于梯度下降
    dZ = [0] * net_deep
    dW = [0] * net_deep
    db = [0] * net_deep
    dA = [0] * net_deep
    A[0] = X

    # 训练次数
    for i in range(0, train_times, 1):
        # 每次前向传播中的纵向深度
        for L in range(1, net_deep, 1):

            activate = 'tanh'
            # 最后一次使用sigmoid激活函数
            if L == net_deep - 1:
                activate = 'sigmoid'
            # 进行前向传播
            forward_parameter = forward_propagation(A[L - 1], {
                'W': W[L],
                'b': b[L],
            }, activate)
            Z[L] = forward_parameter.get('Z')
            A[L] = forward_parameter.get('A')
            assert (Z[L].shape == (net_deep_array[L], m))

        # 计算成本cost
        cost_value = cost(A[net_deep - 1], Y)
        if i % 20 == 0:
            x.append(i)
            y.append(cost_value)

        if i % 500 == 0:
            print("第", i, "次迭代，成本值为：", np.squeeze(cost_value))

        # 后向传播用于梯度下降
        # 倒序计算出
        dAL = 0
        for L in range(net_deep - 1, 0, -1):
            if L == net_deep - 1:
                dAL = -np.divide(Y, A[net_deep - 1]) + np.divide(1 - Y, 1 - A[net_deep - 1])
                dZL = dAL * sigmoid(Z[net_deep - 1]) * sigmoid(1 - Z[net_deep - 1])
            else:
                dZL = dAL * (1 - (np.tanh(Z[L]) * np.tanh(Z[L])))

            dWL = (1 / m) * (np.dot(dZL, A[L - 1].T))
            dbL = (1 / m) * np.sum(dZL, axis=1, keepdims=True)
            # 提供给下一次的循环
            dAL = np.dot(W[L].T, dZL)

            # 更新参数
            W[L] = W[L] - learning_rate * dWL
            b[L] = b[L] - learning_rate * dbL

    plt.plot(x, y, color='orange')
    plt.show()

    parameter = {
        'W': W,
        'b': b,
        'x': x,
        'y': y,
        'net_deep_array': net_deep_array,
    }
    return parameter


# 前向传播
def forward_propagation(A_Last, parameter, activate='tanh'):
    W = parameter.get('W')
    b = parameter.get('b')

    Z = np.dot(W, A_Last) + b
    if activate == 'tanh':
        A = np.tanh(Z)
    elif activate == 'sigmoid':
        A = sigmoid(Z)

    return {
        'Z': Z,
        'A': A,
    }


# 后向传播
def backward_propagation(dA, Z, A_Last_T, W):
    dZ = dA * sigmoid(Z) * (1 - sigmoid(Z))


# 计算该结果的成本
def cost(A, Y):
    A = np.squeeze(A)
    Y = np.squeeze(Y)
    assert (A.shape[0] == Y.shape[0])
    m = A.shape[0]
    # 这里使用 np.multiply 是因为只有一维所以对应想乘
    # a = np.log(A)
    # b = np.multiply(np.log(A), Y)
    # c = np.log(1 - A)
    # d = np.multiply((1 - Y), np.log(1 - A))

    temp = np.multiply(np.log(A), Y) + np.multiply((1 - Y), np.log(1 - A))
    # 取了一次绝对值
    temp = np.maximum(temp, -temp)
    cost_ret = np.sum(temp) * (-1 / m)
    cost_ret = np.maximum(cost_ret, -cost_ret)

    return float(cost_ret)


# 初始化W和b的参数


def initial_parameters(net_deep_array):
    net_deep = len(net_deep_array)
    W = []
    b = []
    for L in range(net_deep):
        WL = np.random.randn(net_deep_array[L], net_deep_array[L - 1]) * 0.01
        bL = np.zeros(shape=(net_deep_array[L], 1))
        W.append(WL)
        b.append(bL)
    return W, b


# 对深层神经网络得出的结果进行测试
def test_network(X, Y, parameter):
    W = parameter.get('W')
    b = parameter.get('b')
    net_deep_array = parameter.get('net_deep_array')
    net_deep = len(net_deep_array)
    A = X

    # 每次前向传播中的纵向深度
    for L in range(1, net_deep, 1):
        activate = 'tanh'
        # 最后一次使用sigmoid激活函数
        if L == net_deep - 1:
            activate = 'sigmoid'
        # 进行前向传播
        forward_parameter = forward_propagation(A, {
            'W': W[L],
            'b': b[L],
        }, activate)
        A = forward_parameter.get('A')
    # 计算成本cost
    cost_value = cost(A, Y)

    print(numpy.around(np.squeeze(A), 1))
    print(Y)
    m = A.shape[1]
    for i in range(0, A.shape[1]):
        if A[0, i] > 0.5:
            A[0, i] = 1
        else:
            A[0, i] = 0

    print("成本cost=" + str(cost_value))
    print("准确性: " + str(float(np.sum((A == Y)) * 100 / m)) + "%")


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
        x = random.randint(-5, 15)
        y = random.randint(0, 150)
        z = random.randint(0, 150)
        temp = np.exp(x) + 3 * y + z
        result = 1
        if temp < 500:
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
    data_X, data_Y = get_number(5000)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)

    print(data_X.shape)
    print(data_Y.shape)

    parameter = deep_neural_network(data_X, data_Y, train_times=5000)

    # 对测试集数据进行评估准确性
    test_X, test_Y = get_number(15)
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)
    test_network(test_X, test_Y, parameter=parameter)

    plt.title("week4 深层神经网络")
    plt.xlabel("x/times")
    plt.ylabel("损失值（越小越好）")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    x = parameter.get('x')
    y = parameter.get('y')
    plt.plot(x, y, color='orange')
    plt.show()
