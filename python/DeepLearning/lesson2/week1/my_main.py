import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import random
import lr_utils
from generate_data import get_normal_data, get_simple_data

# 设置常量
# 激活函数的标识字符串
SIGMOID_NAME = 'sigmoid'
TANH_NAME = 'tanh'
RELU_NAME = 'ReLU'


# 激活函数
# def sigmoid(x):
#     return 1 / (1 + np.exp(-x))
def sigmoid(inX):
    from numpy import exp
    # return 1.0/(1+exp(-inX))
    # 优化
    return 1.0 / (1 + exp(-inX))


def ReLU(Idata):
    return 1 * (Idata > 0) * Idata


def d_ReLU(x):
    y = (x > 0) * 1
    return y


# 深层神经网络主驱动
# net_array = 深度数组，如 [{'neurons': 3, 'activate': 'tanh'}]
# learning_rate = 学习率，默认为 0.12
# train_times = 训练次数，默认为 3000
# random_seed = 随机数的种子，默认为 2021
def deep_neural_network(X, Y
                        , net_array, learning_rate=0.12
                        , train_times=3000, random_seed=2021):
    # 绘图
    x = []
    y = []

    # 初始化基本参数
    net_deep = len(net_array)
    net_array[0]['neurons'] = X.shape[0]
    numpy.random.seed(random_seed)
    m = X.shape[1]
    W, b = initial_parameters(net_array)

    # 对每一个深度的参数进行保存
    Z = [np.array([])] * net_deep
    A = [np.array([])] * net_deep
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
            activate = net_array[L]['activate']
            # 进行前向传播
            forward_parameter = forward_propagation(A[L - 1], {
                'W': W[L],
                'b': b[L],
            }, activate)
            Z[L] = np.array(forward_parameter.get('Z'))
            A[L] = np.array(forward_parameter.get('A'))
            assert (Z[L].shape == (net_array[L]['neurons'], m))

        # 计算成本cost
        cost_value = cost(A[net_deep - 1], Y)
        if i % 50 == 0:
            x.append(i)
            y.append(cost_value)

            # 打印成本值
            if i % 200 == 0:
                accuracy = getAccuracy(A[net_deep - 1], Y)
                print("第" + str(i) + "次迭代，成本值为："
                      + str(round(cost_value, 5)) + "，准确性为" + str(accuracy) + "%")

        # 后向传播用于梯度下降
        # 倒序计算出
        dA = -np.divide(Y, A[net_deep - 1]) + np.divide(1 - Y, 1 - A[net_deep - 1])
        for L in range(net_deep - 1, 0, -1):
            parameter_back = {}
            activate = net_array[L]['activate']
            parameter_back = backward_propagation(dA, A[L - 1], Z[L], W[L], activate)
            dWL = np.array(parameter_back.get('dWL'))
            dbL = np.array(parameter_back.get('dbL'))
            # 提供给下一次循环的AL
            dAL = np.array(parameter_back.get('dAL'))
            assert dWL.shape == (net_array[L]['neurons'], net_array[L - 1]['neurons'])

            # 更新参数
            W[L] = W[L] - learning_rate * dWL
            b[L] = b[L] - learning_rate * dbL

    parameter = {
        'W': W,
        'b': b,
        'x': x,
        'y': y,
        'net_array': net_array,
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
    elif activate == RELU_NAME:
        A = ReLU(Z)

    return {
        'Z': Z,
        'A': A,
    }


# 反向传播，梯度下降
# 以下L=当前层
# --input：
# dA = 第L层的A的导数
# ZL = 第L层的Z
# A_last = 第L-1层的A
# WL = 第L层的W
# activate = 激活函数类型，'tanh'或'sigmoid'
# --output:
# 字典键值对形式
# dA_last = 第L-1层的A的导数
# dZL = 第L层的Z的导数
# dWL = 第L层的W的导数
# dbL = 第L层的b的导数
def backward_propagation(dA, A_last, ZL, WL, activate=TANH_NAME):
    # m = 样本数量
    global dZL
    m = ZL.shape[1]
    if activate == TANH_NAME:
        dZL = dA * (1 - (pow(np.tanh(ZL), 2)))
    elif activate == SIGMOID_NAME:
        dZL = dA * pow(sigmoid(ZL), 2)
    elif activate == RELU_NAME:
        dZL = dA * d_ReLU(ZL)
    dWL = (1 / m) * (np.dot(dZL, A_last.T))
    dbL = (1 / m) * np.sum(dZL, axis=1, keepdims=True)
    dAL = np.dot(WL.T, dZL)
    return {
        'dA_last': dAL,
        'dZL': dZL,
        'dWL': dWL,
        'dbL': dbL,
    }


# 计算该结果的成本
def cost(A, Y):
    A = np.squeeze(A)
    Y = np.squeeze(Y)
    assert (A.shape[0] == Y.shape[0])
    m = A.shape[0]
    # 这里使用 np.multiply 是因为只有一维所以对应想乘

    try:
        temp = np.multiply(np.log(A), Y) + np.multiply((1 - Y), np.log(1 - A))
    except RuntimeWarning:
        a = np.log(A)
        b = np.multiply(np.log(A), Y)
        c = np.log(1 - A)
        d = np.multiply((1 - Y), np.log(1 - A))
        print(a)
        print(b)
        print(c)
        print(d)
        temp = 0

    # 取了一次绝对值
    temp = np.maximum(temp, -temp)
    cost_ret = np.sum(temp) * (-1 / m)
    cost_ret = np.maximum(cost_ret, -cost_ret)

    return float(cost_ret)


# 初始化W和b的参数
# net_array = 深度数组，如 [{'neurons': 3, 'activate': 'tanh'}]
def initial_parameters(net_array):
    net_deep = len(net_array)
    W = []
    b = []
    for L in range(net_deep):
        WL = np.random.randn(net_array[L]['neurons']
                             , net_array[L - 1]['neurons']) * 0.01
        bL = np.zeros(shape=(net_array[L]['neurons'], 1))
        W.append(WL)
        b.append(bL)
    return W, b


# 对深层神经网络得出的结果进行测试
def mytest_network(X, Y, parameter):
    W = parameter.get('W')
    b = parameter.get('b')
    net_array = parameter.get('net_array')
    net_deep = len(net_array)
    A = X

    # 每次前向传播中的纵向深度
    for L in range(1, net_deep, 1):
        activate = net_array[L]['activate']
        forward_parameter = forward_propagation(A, {
            'W': W[L],
            'b': b[L],
        }, activate)
        A = forward_parameter.get('A')
    # 计算成本cost
    cost_value = cost(A, Y)

    print(numpy.around(np.squeeze(A), 3))
    print(Y)

    accuracy = getAccuracy(A, Y)

    print("成本cost=" + str(round(cost_value, 5)))
    print("准确性: " + str(accuracy) + "%")


# 获取准确性评估，将A转为Y_hat并与Y进行比较，返回准确率
# input：
# A : np.array(1,m)
# Y : np.array(1,m)
# output:
# accuracy (float)
def getAccuracy(A, Y):
    # 获取总样本数
    A_dummy = A.copy()
    m = A_dummy.shape[1]
    for i in range(0, A_dummy.shape[1]):
        if A_dummy[0, i] > 0.5:
            A_dummy[0, i] = 1
        else:
            A_dummy[0, i] = 0
    a = float(np.sum((A_dummy == Y)))
    accuracy = float(np.sum((A_dummy == Y))) * 100 / m
    return accuracy


if __name__ == '__main__':
    # 从给定的猫训练集来初始化输入数据
    # train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = lr_utils.load_dataset()
    #
    # train_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
    # test_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
    #
    # train_x = train_x_flatten / 255
    # train_y = train_set_y
    # test_x = test_x_flatten / 255
    # test_y = test_set_y

    # 从我自己写的生成函数来，初始化训练的数据
    X_shape = 3
    data_X, data_Y = get_simple_data(50000, X_shape=X_shape)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)

    # data_X = train_x
    # data_Y = train_y

    print(data_X.shape)
    print(data_Y.shape)

    # 初始化超参数
    net_array = [
        {'neurons': 2, 'activate': RELU_NAME},
        {'neurons': 7, 'activate': RELU_NAME},
        {'neurons': 1, 'activate': 'sigmoid'},
    ]
    learning_rate = 0.0001

    random_seed = 1
    parameter = deep_neural_network(data_X, data_Y, train_times=3000
                                    , net_array=net_array
                                    , learning_rate=learning_rate
                                    , random_seed=random_seed
                                    )

    # 对测试集数据进行评估准确性
    test_X, test_Y = get_simple_data(500, X_shape=X_shape)
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)

    # test_X = test_x
    # test_Y = test_y
    mytest_network(test_X, test_Y, parameter=parameter)

    plt.title("week4 深层神经网络")
    plt.xlabel("x/times")
    plt.ylabel("损失值（越小越好）")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    x = parameter.get('x')
    y = parameter.get('y')
    plt.plot(x, y, color='orange')
    plt.show()
