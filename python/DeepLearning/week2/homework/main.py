# -*- coding:utf-8 -*-
# @Time:2021/4/30 16:39
# @Author:TimVan
# @File:main.py
# @Software:PyCharm
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

print("y=" + str(train_set_y[:, index])
      + ", it's a " + classes[np.squeeze(train_set_y[:, index])]
      .decode("utf-8") + "' picture")

# print("type(train_set_y)="+str(type(train_set_y)))
# print("train_set_y="+train_set_y)


print(np.shape(train_set_x_orig))
print(np.shape(train_set_y))
print(np.shape(test_set_x_orig))
print(np.shape(test_set_y))

m_train = train_set_y.shape[1]  # 训练集里图片的数量。
m_test = test_set_y.shape[1]  # 测试集里图片的数量。
num_px = train_set_x_orig.shape[1]  # 训练、测试集里面的图片的宽度和高度（均为64x64）。

# 现在看一看我们加载的东西的具体情况
print("训练集的数量: m_train = " + str(m_train))
print("测试集的数量 : m_test = " + str(m_test))
print("每张图片的宽/高 : num_px = " + str(num_px))
print("每张图片的大小 : (" + str(num_px) + ", " + str(num_px) + ", 3)")
print("训练集_图片的维数 : " + str(train_set_x_orig.shape))
print("训练集_标签的维数 : " + str(train_set_y.shape))
print("测试集_图片的维数: " + str(test_set_x_orig.shape))
print("测试集_标签的维数: " + str(test_set_y.shape))

# 为了方便，我们要把维度为（64，64，3）的numpy数组重新构造为（64 x 64 x 3，1）的数组，
# 要乘以3的原因是每张图片是由64x64像素构成的，而每个像素点由（R，G，B）三原色构成的，所以要乘以3。
# 在此之后，我们的训练和测试数据集是一个numpy数组，【每列代表一个平坦的图像】
# ，应该有m_train和m_test列。
#
# 当你想将形状（a，b，c，d）的矩阵X平铺成形状（b * c * d，a）的矩阵X_flatten时，可以使用以下代码：

# X_flatten = X.reshape(X.shape [0]，-1).T ＃X.T是X的转置
# 将训练集的维度降低并转置。
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
# 将测试集的维度降低并转置。
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
