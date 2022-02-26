### 4.4 创建张量
# 可以通过多种方式创建张量,如从 Python 列表对象创建，从Numpy 数组创建，或者创建采样自某种已知分布的张量等。
# 4.4.1 从数组、列表对象创建
# 4.4.2 创建全 0 或全 1 张量
# 4.4.3 创建自定义数值张量
# 4.4.4 创建已知分布的张量
# 4.4.5 创建序列

import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    # 4.4.1 从数组、列表对象创建
    arr = [1, 7, 0, 2]
    arr2 = np.array([[2, 2], [2, 6]])
    a = tf.constant(arr)
    a2 = tf.constant(arr2)
    print(a)
    print(a2)

    # 4.4.2 创建全 0 或全 1 张量
    # 通过tf.zeros(); 和; tf.ones(); 即可创建任意形状，且内容全; 0; 或全; 1; 的张量。
    a = tf.zeros([2])
    a2 = tf.ones([2, 3])
    print(a)
    print(a2)
    a2 = tf.ones_like(arr2)
    print(a2)

    # 4.4.3 创建自定义数值张量
    # 通过tf.fill(shape, value)可以创建全为自定义数值 value 的张量，形状由 shape 参数指定。
    a = tf.fill(dims=[2], value=-1)
    print(a)

    # 4.4.4 创建已知分布的张量
    # 通过 tf.random.normal(shape, mean=0.0, stddev=1.0)可以创建形状为 shape，均值为 mean，
    # 标准差为 stddev 的正态分布𝒩(mean,stddev2)。
    # 通过 tf.random.uniform(shape, minval=0, maxval=None, dtype=tf.float32)
    # 可以创建采样自[minval, maxval)区间的均匀分布的张量。
    # 如果需要均匀采样整形类型的数据，必须指定采样区间的最大值 maxval 参数，同时指 定数据类型为 tf.int*型。
    a = tf.random.normal([2, 2], mean=10, stddev=3)
    print(a)
    a = tf.random.uniform([2, 2], minval=0, maxval=10, dtype=tf.int32)
    print(a)

    # 4.4.5 创建序列
    # 通过tf.range(start, limit, delta=1)
    print(tf.range(0, 10, 2))
