import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import acivate_fun as act
from generate_data import get_normal_data, get_simple_data
from numpy import seterr

seterr(all='raise')

# 设置常量
# 激活函数的标识字符串
SIGMOID_NAME = 'sigmoid'
TANH_NAME = 'tanh'
RELU_NAME = 'ReLU'


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
    last_cost = 0
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
        A_last = A[net_deep - 1]
        cost_value = cost(A_last, Y)
        if i % 100 == 0:
            accuracy = getAccuracy(A_last, Y)
            x.append(i)
            y.append(accuracy)
            # 打印成本值
            # 打印成本值
            if i % 200 == 0:
                print("第" + str(i) + "次迭代，成本值为："
                      + str(round(cost_value, 10)) + "，准确性为" + str(accuracy) + "%"
                      + "，成本较上次减少" + str((last_cost - cost_value) * (1e6)))
                last_cost = cost_value

        # 后向传播用于梯度下降
        # 倒序计算出
        try:
            dA = -np.divide(Y, A_last + 1e-5) + np.divide(1 - Y, (1 - A_last + 1e-5))
        except FloatingPointError:
            print("np.divide(Y, A_last)")
            print(np.divide(Y, A_last))
            print("1 - Y")
            a = 1 - Y
            print(a)
            print("1 - A_last")
            b = 1 - A_last + 1e-5
            print(b)
            print("np.divide(1 - Y, 1 - A_last)")
            print(np.divide(1 - Y, b))
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
        A = act.sigmoid(Z)
    elif activate == RELU_NAME:
        A = act.ReLU(Z)

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
        sig = act.sigmoid(ZL)
        dZL = dA * sig * (1 - sig)
    elif activate == RELU_NAME:
        dZL = dA * act.d_ReLU(ZL)
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
        temp = np.multiply(np.log(A + 1e-5), Y) + np.multiply((1 - Y), np.log((1 - A) + 1e-5))
    except RuntimeWarning or FloatingPointError:
        a = np.log(A)
        b = np.multiply(np.log(A), Y)
        c = np.log((1 - A) + 1e-5)
        d = np.multiply((1 - Y), np.log((1 - A) + 1e-5))
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

    print("成本cost=" + str(round(cost_value, 10)))
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

    # 1.
    # 初始化参数：
    # 1.1：使用0来初始化参数。
    # 1.2：使用随机数来初始化参数。
    # 1.3：使用抑梯度异常初始化参数（参见视频中的梯度消失和梯度爆炸）。
    # 2.
    # 正则化模型：
    # 2.1：使用二范数对二分类模型正则化，尝试避免过拟合。
    # 2.2：使用随机删除节点的方法精简模型，同样是为了尝试避免过拟合。
    # 3.
    # 梯度校验  ：对模型使用梯度校验，检测它是否在梯度下降的过程中出现误差过大的情况。

    # 从我自己写的生成函数来，初始化训练的数据
    X_shape = 1
    data_X, data_Y = get_normal_data(2000, X_shape=X_shape)
    data_X = np.array(data_X)
    data_Y = np.array(data_Y)

    # data_X = train_x
    # data_Y = train_y

    # 初始化超参数
    net_array = [
        {'neurons': 2, 'activate': TANH_NAME},
        {'neurons': 7, 'activate': TANH_NAME},
        {'neurons': 3, 'activate': TANH_NAME},
        {'neurons': 3, 'activate': TANH_NAME},
        {'neurons': 3, 'activate': TANH_NAME},
        {'neurons': 1, 'activate': SIGMOID_NAME},
    ]
    learning_rate = 0.00075
    random_seed = 1

    print("训练集输入的维度为：" + str(data_X.shape))
    print("训练集输入的维度为：" + str(data_Y.shape))
    print("学习率为：" + str(learning_rate))

    parameter = deep_neural_network(data_X, data_Y, train_times=3000
                                    , net_array=net_array
                                    , learning_rate=learning_rate
                                    , random_seed=random_seed
                                    )

    # 对测试集数据进行评估准确性
    test_X, test_Y = get_normal_data(500, X_shape=X_shape)
    test_X = np.array(test_X)
    test_Y = np.array(test_Y)

    # test_X = test_x
    # test_Y = test_y
    mytest_network(test_X, test_Y, parameter=parameter)

    plt.title("L2-Week1 优化的深层神经网络")
    plt.xlabel("x/times")
    plt.ylabel("准确度")
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    x = parameter.get('x')
    y = parameter.get('y')
    plt.plot(x, y, color='orange')
    plt.show()
