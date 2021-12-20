import math
import numpy as np
from numpy import seterr
import matplotlib.pyplot as plt

import acivate_fun as act
from generate_data import get_normal_data, get_simple_data
import init_utils

seterr(all='raise')

# 设置常量
# 激活函数的标识字符串
SIGMOID_NAME = 'sigmoid'
TANH_NAME = 'tanh'
RELU_NAME = 'ReLU'

# 绘图的参数值
plot_x = []
plot_y = []


# 深层神经网络主驱动
# net_array = 深度数组，如 [{'neurons': 3, 'activate': 'tanh'}]
# learning_rate = 学习率，默认为 0.12
# train_times = 训练次数，默认为 3000
# random_seed = 随机数的种子，默认为 2021
# L2_lmd = L2正则的lambda参数，若L2_lmd<=0，则关闭L2正则
# keep_prob = dropout的范围数，范围在(0,1]，为1代表关闭“随机失活”,默认关闭
# normalizing = 是否归一化处理
def deep_neural_network(X, Y
                        , net_array, learning_rate=0.12
                        , train_times=3000, random_seed=2021
                        , L2_lmd=0.0, keep_prob=1, grad_check=False):
    """
    :param grad_check: 是否进行梯度检测，默认不打开（若打开仅在第一次训练开启）
    """

    # 初始化基本参数
    net_deep = len(net_array)
    net_array[0]['neurons'] = X.shape[0]
    np.random.seed(random_seed)
    m = X.shape[1]
    W, b = initial_parameters(net_array)

    # 对每一个深度的参数进行保存
    Z = [np.array([])] * net_deep
    A = [np.array([])] * net_deep
    D = [np.array([])] * net_deep
    # 后向传播用于梯度下降
    dZ = [0] * net_deep
    dW = [0] * net_deep
    db = [0] * net_deep
    dA = [0] * net_deep
    A[0] = X

    # 训练次数
    last_cost = 0
    for i in range(0, train_times, 1):
        # 正向传播：从第1层到最后一层（第0层为输入层，不算）
        for L in range(1, net_deep, 1):
            activate = net_array[L]['activate']
            # 进行前向传播
            forward_parameter = forward_propagation(A[L - 1], {
                'W': W[L],
                'b': b[L],
            }, activate, keep_prob=keep_prob)
            Z[L] = np.array(forward_parameter.get('Z'))
            A[L] = np.array(forward_parameter.get('A'))
            D[L] = np.array(forward_parameter.get('D'))
            assert (Z[L].shape == (net_array[L]['neurons'], m))
        # 计算cost成本值
        A_last = A[net_deep - 1]
        cost_value = cost(A_last, Y, W, L2_lmd)
        # 日志和绘图
        if i % 100 == 0:
            accuracy = getAccuracy(A_last, Y)
            plot_x.append(i)
            plot_y.append(accuracy)
            # 打印成本值
            if i % 200 == 0:
                print("第" + str(i) + "次迭代，成本值为："
                      + str(round(cost_value, 10)) + "，准确性为" + str(accuracy) + "%"
                      + "，成本较上次减少" + str((last_cost - cost_value) * (1e6)))
                last_cost = cost_value

        # 后向传播：从第1层到最后一层(dA是反向传播的输入)
        dA = -np.divide(Y, A_last + 1e-5) + np.divide(1 - Y, (1 - A_last + 1e-5))
        for L in range(net_deep - 1, 0, -1):
            # keep_prob项:由于L=1时，并不需要计算第0层即输入层的Dropout，因此临时传入1
            parameter_back = backward_propagation(dA, A[L - 1], Z[L], W[L]
                                                  , activate=net_array[L]['activate'], L2_lbd=L2_lmd,
                                                  keep_prob=keep_prob if L != 1 else 1, D_last=D[L - 1])
            dWL = np.array(parameter_back.get('dWL'))
            dbL = np.array(parameter_back.get('dbL'))
            # 提供给下一次循环的AL
            dA = np.array(parameter_back.get('dAL'))
            assert dWL.shape == (net_array[L]['neurons'], net_array[L - 1]['neurons'])

            # 更新参数
            W[L] = W[L] - learning_rate * dWL
            b[L] = b[L] - learning_rate * dbL

    parameter = {
        'W': W,
        'b': b,
        'net_array': net_array,
    }
    return parameter


# 前向传播
# keep_prob = dropout的范围数，范围在(0,1]，为1代表关闭“随机失活”,默认关闭
def forward_propagation(A_Last, parameter, activate='tanh', keep_prob=1):
    W = parameter.get('W')
    b = parameter.get('b')

    Z = np.dot(W, A_Last) + b
    if activate == 'tanh':
        A = np.tanh(Z)
    elif activate == 'sigmoid':
        A = act.sigmoid(Z)
    elif activate == RELU_NAME:
        A = act.ReLU(Z)

    result = {
        'Z': Z,
        'A': A,
    }

    # 是否dropout
    if 0 < keep_prob < 1:
        # 构造、判断、丢弃、放缩
        D = np.random.rand(A.shape[0], A.shape[1])
        D = D < keep_prob
        A = A * D
        A = A / keep_prob
        result['D'] = D
    return result


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
# keep_prob = dropout的范围数，范围在(0,1]，为1代表关闭“随机失活”,默认关闭
# D_last = 第L-1层的D,dropout的参数
def backward_propagation(dA, A_last, ZL, WL, activate=TANH_NAME, L2_lbd=0.2
                         , keep_prob=1, D_last: np.ndarray = 0):
    # m = 样本数量
    global dZL
    m = ZL.shape[1]
    if activate == TANH_NAME:
        dZL = dA * (1 - (pow(np.tanh(ZL), 2)))
    elif activate == SIGMOID_NAME:
        sig = act.sigmoid(ZL)
        dZL = dA * sig * (1 - sig)
    elif activate == RELU_NAME:
        dZL = dA * act.d_ReLU(ZL)

    dWL = (1 / m) * (np.dot(dZL, A_last.T))
    # 若L2_lbd>0，则开启L2正则项的求导
    if L2_lbd > 0:
        dWL = dWL + (L2_lbd / m) * WL
    dbL = (1 / m) * np.sum(dZL, axis=1, keepdims=True)
    dA = np.dot(WL.T, dZL)

    # 是否dropout
    if 0 < keep_prob < 1:
        assert dA.shape == D_last.shape
        dA *= D_last
        dA /= keep_prob

    return {
        'dA': dA,
        'dZL': dZL,
        'dWL': dWL,
        'dbL': dbL,
    }


# 计算基于交叉熵的成本
def cost_cross(A, Y):
    A = np.squeeze(A)
    Y = np.squeeze(Y)
    assert (A.shape[0] == Y.shape[0])
    m = A.shape[0]
    # 这里使用 np.multiply 是因为只有一维所以对应想乘

    temp = np.multiply(np.log(A + 1e-5), Y) + np.multiply((1 - Y), np.log((1 - A) + 1e-5))

    # 取了一次绝对值
    temp = np.maximum(temp, -temp)
    cost_ret = np.sum(temp) * (-1 / m)
    cost_ret = np.maximum(cost_ret, -cost_ret)

    return float(cost_ret)


# 计算经过L2正则化的成本
# parameters = 训练出来的w1w2w3
def cost(A, Y, W, L2_lbd):
    # 若L2_lmd<=0，则关闭L2正则
    origin_cost = cost_cross(A, Y)
    if L2_lbd <= 0:
        return origin_cost

    m = A.shape[0]
    L2_cost = 0
    for w in W:
        L2_cost = L2_cost + np.sum(np.square(w))
    L2_cost = (L2_lbd / (2 * m)) * L2_cost

    # L2正则化为原成本（交叉熵）+L2项
    return origin_cost + L2_cost


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


# 用测试集对训练结果进行评估
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
    cost_value = cost_cross(A, Y)

    print(np.around(np.squeeze(A), 3))
    print(Y)

    accuracy = getAccuracy(A, Y)

    print("测试集成本cost=" + str(round(cost_value, 10)))
    print("测试集准确性: " + str(accuracy) + "%")


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


# 对传入数据进行归一化处理
# data的shape应该是(x,m)，其中x是特征值的个数，m是样本数量
# 返回归一化结果、u和delta_double
def normalizing(data: np.ndarray):
    # m = 样本数量
    m = data.shape[1]
    # 1.零均值：对每一个特征值分别求均值
    u = (1 / m) * data.sum(axis=1, keepdims=True)
    cache = data - u

    # 2.归一化方差：注意，是先平方再求和，这是为了避免如[-1,0,1]数据造成求和为0，之后产生除以0
    delta_double = (1 / m) * (cache ** 2).sum(axis=1, keepdims=True)
    cache = cache / delta_double
    return cache, u, delta_double


# 已知u和delta_double进行归一化输入
def normalizing_full(data: np.ndarray, u, delta_double):
    assert data.shape[0] == u.shape[0]
    assert data.shape[0] == delta_double.shape[0]

    cache = data - u
    cache = cache / delta_double
    return cache, u, delta_double


# 梯度检验
def grad_check(fun, d_fun, x, theta=1e-4, epsilon=1e-3):
    """
    :param fun:原函数
    :param d_fun:导函数
    :param x:自变量的求导点
    :param theta:变化值
    :param epsilon:误差精度
    :return: 返回是否正常和diff
        第一步、首先需要给出原函数、导函数、自变量的求导点和精度epsilon
        第二步、分别求出梯度值和求导值
        第三步、求出diff并与epsilon对比，返回是否正常和diff
    """

    # 计算L2正则
    def l2(val):
        return (val ** 2) ** 0.5

    # 手动计算梯度
    def grad():
        first = fun(x + theta)
        second = fun(x - theta)
        return (first - second) / (2 * theta)

    gradient = grad()
    derivation = d_fun(x)
    print("gradient=", gradient)
    print("derivation=", derivation)

    diff = l2(gradient - derivation) / (l2(gradient) + l2(derivation))
    return diff < epsilon, diff


# x = 数据集，y=对应的结果
def split_data(x, y, t=1):
    # 首先判断x和y的长度是否匹配
    assert x.shape[1] == y.shape[1]
    m = x.shape[1]

    state = np.random.get_state()
    np.random.shuffle(x.T)
    np.random.set_state(state)
    np.random.shuffle(y.T)

    x_list = []
    y_list = []
    max_k = math.ceil(x.shape[1] / t)
    for i in range(max_k):
        start = i * t
        end = start + t if (start + t) <= m else None
        x_list.append(x[:, start:end])
        y_list.append(y[:, start:end])
    return x_list, y_list


# matplotlib.pyplot的设置
def pyplot_init():
    plt.title("L2-Week2 改善深层神经网络")
    plt.xlabel("x/times")
    plt.ylabel("准确度")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    plt.plot(plot_x, plot_y, color='orange')
    plt.show()


if __name__ == '__main__':
    # 1. 分割数据集
    # 2. 优化梯度下降算法：
    #     2.1 不使用任何优化算法
    #     2.2 mini-batch梯度下降法
    #     2.3 使用具有动量的梯度下降算法
    #     2.4 使用Adam算法

    # 导入官方给的例子
    train_X, train_Y, test_X, test_Y = init_utils.load_dataset(is_plot=False)

    X_shape = 1
    data_X, data_Y = get_normal_data(2000, X_shape=X_shape)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)

    data_X = train_X
    data_Y = train_Y

    # 初始化超参数
    # net_array = 神经网络描述数组，第0项实际为输入值的特征数，不起作用
    net_array = [
        {'neurons': 2, 'activate': TANH_NAME},
        {'neurons': 7, 'activate': TANH_NAME},
        {'neurons': 3, 'activate': TANH_NAME},
        {'neurons': 1, 'activate': SIGMOID_NAME},
    ]
    learning_rate = 0.034
    random_seed = 1

    print("训练集输入的维度为：" + str(data_X.shape))
    print("训练集输入的维度为：" + str(data_Y.shape))
    print("学习率为：" + str(learning_rate))

    # 对训练集进行归一化输入
    new_data_X, u, delta_double = normalizing(data=data_X)

    parameter = deep_neural_network(new_data_X, data_Y, train_times=4000
                                    , net_array=net_array
                                    , learning_rate=learning_rate
                                    , random_seed=random_seed
                                    , L2_lmd=0.2
                                    , keep_prob=0.5
                                    , grad_check=False
                                    )

    # 对测试集数据进行评估准确性
    # test_X, test_Y = get_normal_data(500, X_shape=X_shape)
    # test_X = np.array(test_X)
    # test_Y = np.array(test_Y)

    # 对测试集进行归一化输入
    new_test_X, u, delta_double = normalizing_full(data=test_X, u=u, delta_double=delta_double)
    mytest_network(new_test_X, test_Y, parameter=parameter)

    # 绘图最终的结果
    pyplot_init()
