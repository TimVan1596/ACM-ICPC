import numpy as np
import h5py
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.python.framework import ops
import tf_utils
import time

#%matplotlib inline #如果你使用的是jupyter notebook取消注释
np.random.seed(1)

if __name__ == '__main__':
    y_hat = tf.constant(36, name="y_hat")  # 定义y_hat为固定值36
    y = tf.constant(39, name="y")  # 定义y为固定值39

    loss = tf.Variable((y - y_hat) ** 2, name="loss")  # 为损失函数创建一个变量

    init = tf.global_variables_initializer()  # 运行之后的初始化(ession.run(init))
    # 损失变量将被初始化并准备计算
    with tf.Session() as session:  # 创建一个session并打印输出
        session.run(init)  # 初始化变量
        print(session.run(loss))  # 打印损失值

