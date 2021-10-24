# 1. 初始化参数：
# 	1.1：使用0来初始化参数。
# 	1.2：使用随机数来初始化参数。
# 	1.3：使用抑梯度异常初始化参数（参见视频中的梯度消失和梯度爆炸）。
# 2. 正则化模型：
# 	2.1：使用二范数对二分类模型正则化，尝试避免过拟合。
# 	2.2：使用随机删除节点的方法精简模型，同样是为了尝试避免过拟合。
# 3. 梯度校验  ：对模型使用梯度校验，检测它是否在梯度下降的过程中出现误差过大的情况。


import numpy as np
import matplotlib.pyplot as plt
import sklearn
import sklearn.datasets
import init_utils  # 第一部分，初始化
import reg_utils  # 第二部分，正则化
import gc_utils  # 第三部分，梯度校验


def model(X, Y, learning_rate=0.01, num_iterations=15000, print_cost=True, initialization="he", is_polt=True):
    """
    实现一个三层的神经网络：LINEAR ->RELU -> LINEAR -> RELU -> LINEAR -> SIGMOID

    参数：
        X - 输入的数据，维度为(2, 要训练/测试的数量)
        Y - 标签，【0 | 1】，维度为(1，对应的是输入的数据的标签)
        learning_rate - 学习速率
        num_iterations - 迭代的次数
        print_cost - 是否打印成本值，每迭代1000次打印一次
        initialization - 字符串类型，初始化的类型【"zeros" | "random" | "he"】
        is_polt - 是否绘制梯度下降的曲线图
    返回
        parameters - 学习后的参数
    """
    grads = {}
    costs = []
    m = X.shape[1]
    layers_dims = [X.shape[0], 10, 5, 1]

    # 选择初始化参数的类型
    if initialization == "zeros":
        pass
        # parameters = initialize_parameters_zeros(layers_dims)
    elif initialization == "random":
        pass
        # parameters = initialize_parameters_random(layers_dims)
    elif initialization == "he":
        pass
        # parameters = initialize_parameters_he(layers_dims)
    else:
        print("错误的初始化参数！程序退出")
        exit

    # 开始学习
    for i in range(0, num_iterations):
        # 前向传播
        a3, cache = init_utils.forward_propagation(X, parameters)

        # 计算成本
        cost = init_utils.compute_loss(a3, Y)

        # 反向传播
        grads = init_utils.backward_propagation(X, Y, cache)

        # 更新参数
        parameters = init_utils.update_parameters(parameters, grads, learning_rate)

        # 记录成本
        if i % 1000 == 0:
            costs.append(cost)
            # 打印成本
            if print_cost:
                print("第" + str(i) + "次迭代，成本值为：" + str(cost))

    # 学习完毕，绘制成本曲线
    if is_polt:
        plt.plot(costs)
        plt.ylabel('cost')
        plt.xlabel('iterations (per hundreds)')
        plt.title("Learning rate =" + str(learning_rate))
        plt.show()

    # 返回学习完毕后的参数
    return parameters


def initialize_parameters_zeros(layers_dims):
    """
    将模型的参数全部设置为0

    参数：
        layers_dims - 列表，模型的层数和对应每一层的节点的数量
    返回
        parameters - 包含了所有W和b的字典
            W1 - 权重矩阵，维度为（layers_dims[1], layers_dims[0]）
            b1 - 偏置向量，维度为（layers_dims[1],1）
            ···
            WL - 权重矩阵，维度为（layers_dims[L], layers_dims[L -1]）
            bL - 偏置向量，维度为（layers_dims[L],1）
    """
    parameters = {}

    L = len(layers_dims)  # 网络层数

    for l in range(1, L):
        parameters["W" + str(l)] = np.zeros((layers_dims[l], layers_dims[l - 1]))
        parameters["b" + str(l)] = np.zeros((layers_dims[l], 1))

        # 使用断言确保我的数据格式是正确的
        assert (parameters["W" + str(l)].shape == (layers_dims[l], layers_dims[l - 1]))
        assert (parameters["b" + str(l)].shape == (layers_dims[l], 1))

    return parameters


if __name__ == '__main__':
    # %matplotlib inline #如果你使用的是Jupyter Notebook，请取消注释。
    # plt.rcParams['figure.figsize'] = (5, 5)  # set default size of plots
    # plt.rcParams['image.interpolation'] = 'nearest'
    # plt.rcParams['image.cmap'] = 'gray'
    # train_X, train_Y, test_X, test_Y = init_utils.load_dataset(is_plot=True)
    # plt.show()

    parameters = initialize_parameters_zeros([3, 2, 1])
    print("W1 = " + str(parameters["W1"]))
    print("b1 = " + str(parameters["b1"]))
    print("W2 = " + str(parameters["W2"]))
    print("b2 = " + str(parameters["b2"]))

