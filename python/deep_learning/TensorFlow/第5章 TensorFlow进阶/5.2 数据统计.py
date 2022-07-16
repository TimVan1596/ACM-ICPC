### 5.2 数据统计
import keras.losses
import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    # ##### 5.2.1 向量范数
    #
    # 向量范数(Vector Norm)是表征向量“长度”的一种度量方法，它可以推广到张量上在
    #  TensorFlow 中，可以通过 tf.norm(x, ord)求解张量的 L1、L2、∞等范数，
    #  其中参数ord 指定为 1、2 时计算 L1、L2 范数，指定为 np.inf 时计算∞ −范数
    # x = tf.ones([2, 2])
    # # 计算L1范数, 即绝对值之和, L1=4.0
    # print(tf.norm(x, ord=1))
    # # 计算L2范数, 即所有元素的平方和再开根号, L2=2.0
    # print(tf.norm(x, ord=2))
    # # 计算无穷范数, 即绝对值的最大值, 无穷范数=1
    # print(tf.norm(x, ord=np.inf))

    #     5.2.2 最值、均值、和
    # 通过 tf.reduce_max、tf.reduce_min、tf.reduce_mean、tf.reduce_sum 函数
    # 可以求解张量 在某个维度上的最大、最小、均值、和，也可以求全局最大、最小、均值、和信息。
    # 这样的操作相当于减维，因此用reduce前缀
    #
    # -通过 tf.reduce_max 函数实现最大值(axis 纵0横1)
    # x = tf.constant([[1, 2, 3], [4, 5, 6]])
    # tf.Tensor([4 5 6], shape=(3,), dtype=int32)
    # print(tf.reduce_max(x, axis=0))
    # tf.Tensor([3 6], shape=(2,), dtype=int32)
    # print(tf.reduce_max(x, axis=1))
    # 当不指定 axis 参数时，tf.reduce_*函数会求解出全局元素的最大、最小、均值、和等 数据
    # tf.Tensor(1, shape=(), dtype=int32)
    # print(tf.reduce_min(x))
    # # tf.Tensor(6, shape=(), dtype=int32)
    # print(tf.reduce_max(x))
    # # tf.Tensor(3.5, shape=(), dtype=float32)
    # print(tf.reduce_mean(tf.cast(x, dtype=tf.float32)))

    # 通过 tf.reduce_mean 在样本数维度上计算均值
    out = tf.random.normal([4, 10])
    y = tf.constant([1, 2, 2, 0])
    y = tf.one_hot(y, depth=10)
    loss = keras.losses.mse(y, out)
    loss = tf.reduce_mean(loss)
    # 计算误差
    print(loss)

    # 求和函数 tf.reduce_sum(x, axis)，它可以求解张量在 axis 轴上所有 特征的和(axis 纵0横1)
    x = tf.constant([[1, 2, 3], [4, 5, 6]])
    # tf.Tensor([6 15], shape=(2,), dtype=int32)
    print(tf.reduce_sum(x, axis=-1))

    # 通过 tf.argmax(x, axis)和 tf.argmin(x, axis)可以求解在 axis 轴上，x 的最大值、最小值所 在的索引号
    # tf.Tensor([2 2], shape=(2,), dtype=int64)
    print(tf.argmax(x, axis=-1))
