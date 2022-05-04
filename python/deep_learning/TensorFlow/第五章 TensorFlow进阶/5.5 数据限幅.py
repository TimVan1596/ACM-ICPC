import os

import keras.datasets.imdb
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.5 数据限幅
    # 1. 通过 tf.maximum(x, a)实现数据的下限幅，即𝑥 ∈ [𝑎, +∞)；
    # 2. 可以通过 tf.minimum(x, a)实现数据的上限幅，即𝑥 ∈ (−∞,𝑎]
    # 3. 通过组合 tf.maximum(x, a)和 tf.minimum(x, b)可以实现同时对数据的上下边界限幅，即 𝑥 ∈ [𝑎, 𝑏]
    # x = tf.range(9)
    # [5 5 5 5 5 5 6 7 8]
    # print(tf.maximum(x, 5))
    # # [0 1 2 3 4 5 5 5 5]
    # print(tf.minimum(x, 5))
    # # 4. 使用 tf.clip_by_value 实现上下限幅
    # # [2 2 2 3 4 5 6 7 7]
    # print(tf.clip_by_value(x, 2, 7))
    # 5. 使用 tf.clip_by_norm 等比例放缩来减小L2范数,实现对梯度进行裁剪，等比例放缩，防止梯度爆炸
    # Clips tensor values to a maximum L2-norm.
    # tf.clip_by_norm
    # clip_by_norm(t, clip_norm, axes=None, name=None)
    # t: 输入tensor，也可以是list
    # clip_norm: 一个具体的数，如果l2norm(t) ≤ clip_norm， 则t不变化；否则t = t∗clip_norm / l2norm(t)
    # axes：指定计算l2norm的维度，如果不指定，利用t中所有元素计算l2norm，对于一维tensor没有影响，对于二维tensor会有影响
    # 给定一个张量t和一个最大剪辑值clip_norm，
    # 该操作进行归一化t，使其 L2 范数小于或等于clip_norm，沿 给出的维度axes。
    # 具体来说，在所有维度都用于计算的默认情况下，
    # 如果 的 L2-范数t已经小于或等于clip_norm，t则不进行修改。
    # 如果 L2 范数大于，则此操作返回与其值设置为clip_norm相同类型和形状的张量：t
    # x = tf.cast(x, dtype=tf.float32)
    # x = tf.clip_by_norm(x, clip_norm=3.0)
    # # [0.         0.21004201 0.42008403 0.63012606 0.84016806 1.05021
    # #  1.2602521  1.4702941  1.6803361 ]
    # print(x)
    # # tf.Tensor(3.0, shape=(), dtype=float32)
    # print(tf.norm(x, ord=2))
    # 6. 使用 tf.clip_by_global_norm 实现整体缩放，通过权重梯度的总和的比率来截取多个张量的值
    # x = tf.range(9, dtype=tf.float32)
    # Clips values of multiple tensors by the ratio of the sum of their norms.
    # clip_by_global_norm返回值有两个，分别为裁剪后的tensor和global norm
    print(tf.clip_by_global_norm([[3.0, 4.0], [1.0, 2.0]], clip_norm=2))

    pass
