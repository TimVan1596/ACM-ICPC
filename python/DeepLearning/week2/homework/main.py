# -*- coding:utf-8 -*-
# @Time:2021/4/30 16:39
# @Author:TimVan
# @File:main.py
# @Software:PyCharm
import numpy
import numpy as np

from lr_utils import load_dataset

print("\n")
train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
index = 25
# # plt.imshow(train_set_x_orig[index])
# # # print("train_set_y=" + str(train_set_y)) #你也可以看一下训练集里面的标签是什么样的。
# # #也是可以的
# # plt.show()
# index = 1
# plt.imshow(test_set_x_orig[index])
# plt.show()


# 打印出当前的训练标签值
# 使用np.squeeze的目的是压缩维度，【未压缩】train_set_y[:,index]的值为[1] , 【压缩后】np.squeeze(train_set_y[:,index])的值为1
# print("【使用np.squeeze：" + str(np.squeeze(train_set_y[:,index])) + "，不使用np.squeeze： " + str(train_set_y[:,index]) + "】")
# 只有压缩后的值才能进行解码操作

# print("y=" + str(train_set_y[:, index])
#       + ", it's a " + classes[np.squeeze(train_set_y[:, index])]
#       .decode("utf-8") + "' picture")

# print("type(train_set_y)="+str(type(train_set_y)))
# print("train_set_y="+train_set_y)


# print(np.shape(train_set_x_orig))
# print(np.shape(train_set_y))
# print(np.shape(test_set_x_orig))
# print(np.shape(test_set_y))

m_train = train_set_y.shape[1]  # 训练集里图片的数量。
m_test = test_set_y.shape[1]  # 测试集里图片的数量。
num_px = train_set_x_orig.shape[1]  # 训练、测试集里面的图片的宽度和高度（均为64x64）。

# 现在看一看我们加载的东西的具体情况
# print("训练集的数量: m_train = " + str(m_train))
# print("测试集的数量 : m_test = " + str(m_test))
# print("每张图片的宽/高 : num_px = " + str(num_px))
# print("每张图片的大小 : (" + str(num_px) + ", " + str(num_px) + ", 3)")
# print("训练集_图片的维数 : " + str(train_set_x_orig.shape))
# print("训练集_标签的维数 : " + str(train_set_y.shape))
# print("测试集_图片的维数: " + str(test_set_x_orig.shape))
# print("测试集_标签的维数: " + str(test_set_y.shape))

# 为了方便，我们要把维度为（64，64，3）的numpy数组重新构造为（64 x 64 x 3，1）的数组，
# 要乘以3的原因是每张图片是由64x64像素构成的，而每个像素点由（R，G，B）三原色构成的，所以要乘以3。
# 在此之后，我们的训练和测试数据集是一个numpy数组，【每列代表一个平坦的图像】
# ，应该有m_train和m_test列。
#
# 当你想将形状（a，b，c，d）的矩阵X平铺成形状（b * c * d，a）的矩阵X_flatten时，可以使用以下代码：

# X_flatten = X.reshape(X.shape [0]，-1).T ＃X.T是X的转置
print(train_set_x_orig.shape[0])

# 将训练集的维度降低并转置。
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
# print(train_set_x_flatten.shape)
# print(train_set_x_flatten.shape[0])
# print(train_set_x_flatten)
# 将测试集的维度降低并转置。
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T

# 将数据进行标准化
train_set_x = train_set_x_flatten / 255
test_set_x = test_set_x_flatten / 255


# 建立神经网络的主要步骤是：
# 1、定义模型结构（例如输入特征的数量）
# 2、初始化模型的参数
# 3、循环：
# 3.1 计算当前损失（正向传播）
# 3.2 计算当前梯度（反向传播）
# 3.3 更新参数（梯度下降）
# z=任何大小的标量或numpy数组。
def sigmoid(z):
    # 对sigmoid函数的优化，避免了出现极大的数据溢出
    if z >= 0:
        return 1.0 / (1 + np.exp(-z))
    else:
        return np.exp(z) / (1 + np.exp(z))


# 测试sigmoid()
# print("sigmoid(-1000) = " + str(sigmoid(-10000000)))
# print("sigmoid(0) = " + str(sigmoid(0)))
# print("sigmoid(1000) = " + str(sigmoid(10000000)))
# print("sigmoid(9.2) = " + str(sigmoid(9.2)))


# 此函数为w创建一个维度为（dim，1）的0向量，并将b初始化为0。
# dim = 我们想要的w矢量的大小（或者这种情况下的参数数量）
def initialize_with_zeros(dim):
    w = np.zeros(shape=(dim, 1))
    b = 0
    # 使用断言来确保我要的数据是正确的
    assert (w.shape == (dim, 1))  # w的维度是(dim,1)
    assert (isinstance(b, float) or isinstance(b, int))  # b的类型是float或者是int
    # w  = 维度为（dim，1）的初始化向量。
    # b  = 初始化的标量（对应于偏差）
    return w, b


def propagate(w, b, X, Y):
    """
    实现前向和后向传播的成本函数及其梯度。
    参数：
        w  - 权重，大小不等的数组（num_px * num_px * 3，1）
        b  - 偏差，一个标量
        X  - 矩阵类型为（num_px * num_px * 3，训练数量）
        Y  - 真正的“标签”矢量（如果非猫则为0，如果是猫则为1），矩阵维度为(1,训练数据数量)

    返回：
        cost- 逻辑回归的负对数似然成本
        dw  - 相对于w的损失梯度，因此与w相同的形状
        db  - 相对于b的损失梯度，因此与b的形状相同
    """
    m = X.shape[1]

    # 正向传播
    A = sigmoid(np.dot(w.T, X) + b)  # 计算激活值，请参考公式2。
    cost = (- 1 / m) * np.sum(Y * np.log(A) + (1 - Y) * (np.log(1 - A)))  # 计算成本，请参考公式3和4。

    # 反向传播
    dw = (1 / m) * np.dot(X, (A - Y).T)  # 请参考视频中的偏导公式。
    db = (1 / m) * np.sum(A - Y)  # 请参考视频中的偏导公式。

    # 使用断言确保我的数据是正确的
    assert (dw.shape == w.shape)
    assert (db.dtype == float)
    cost = np.squeeze(cost)
    assert (cost.shape == ())

    # 创建一个字典，把dw和db保存起来。
    grads = {
        "dw": dw,
        "db": db
    }
    return (grads, cost)


# 测试initialize_with_zeros函数
# initialData = initialize_with_zeros(3)
# print(initialData)
# print(initialData[0].shape)
# print(initialData[0])

# a=3*1的列矩阵
a = numpy.array([[1], [2], [3]])
# b=1*3的行矩阵
b = numpy.array([[4, 5, 6]])

print(a.shape)
print(b.shape)

print("a*b =")
print(a * b)
# print("numpy.matmul(a, b) =")
# print(numpy.matmul(a, b))
print("numpy.dot(a, b) =")
print(numpy.dot(a, b))
# print("numpy.cross(a, b) =")
# print(numpy.cross(a, b))
