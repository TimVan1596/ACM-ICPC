import logging

import pandas as pd
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
def init_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    x_train /= 255.0
    # logging.debug(pd.Series(y_train))
    logging.debug(x_train[0].shape)
    logging.debug('\n {}'.format(pd.DataFrame(x_train[0])))
    return (x_train, y_train), (x_test, y_test)


if __name__ == '__main__':
    # 暂时仅需训练集
    (x_train, y_train), _ = init_data()
