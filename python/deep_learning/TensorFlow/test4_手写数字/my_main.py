import logging

import tensorflow as tf
from tensorflow import keras

# 设置日志级别
logging.basicConfig(level=logging.NOTSET)


# 对手写数字进行训练（仅完成训练集的部分）
# 思路
# 1、获取训练集
# 2、前向传播：训练集使用三层网络进行训练
# 3、反向传播：获取LOSS并自动求导
# 4、集成：多次迭代

# 获取数据集并进行处理
# @re
def init_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    data_list = [[x_train, y_train], [x_test, y_test]]
    for data in data_list[:]:
        # 预处理步骤：x先归一化到[0,1]，再缩放至[-1,1]
        data[0] = ((tf.convert_to_tensor(data[0], dtype=tf.float32) / 255.0) - 0.5) * 2
    return data_list[0], data_list[1]


if __name__ == '__main__':
    # 暂时仅需训练集
    (x_train, y_train), _ = init_data()
    dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    dataset = dataset.batch(32)
