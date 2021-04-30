# -*- coding:utf-8 -*-
# @Time:2021/4/30 16:39
# @Author:TimVan
# @File:main.py
# @Software:PyCharm

import numpy as np

from lr_utils import load_dataset

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
print("y=" + str(train_set_y[:, index]) + ", it's a "
      + classes[np.squeeze(train_set_y[:, index])]
      .decode("utf-8") + "' picture")
