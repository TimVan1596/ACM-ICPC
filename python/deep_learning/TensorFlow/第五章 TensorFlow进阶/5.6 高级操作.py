import os

import keras.datasets.imdb
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.6 高级操作
    #
    # #### 5.6.1 tf.gather
    #
    # - tf.gather 可以实现根据索引号收集数据的目的
    # - tf.gather 非常适合索引号没有规则的场合，其中索引号可以乱序排列，此时收 集的数据也是对应顺序
    # Gather slices from params axis axis according to indices. indices must be an integer tensor of any dimension (often 1-D).
    # Tensor.getitem works for scalars, tf.newaxis, and python slices
    # tf.gather extends indexing to handle tensors of indices.
    # In the simplest case it's identical to scalar indexing:
    # 考虑班级成绩册的例子，
    # 假设共有 4个班级，每个班级 35 个学生，8 门科目，
    # 保存成绩册的张量 shape 为[4,35,8]。
    x = tf.random.uniform([4, 35, 8], maxval=100, dtype=tf.int32)
    # (4, 35, 8)
    print(x.shape)
    # 现在需要收集第 1~2 个班级的成绩册，可以给定需要收集班级的索引号：[0,1]，并指定班
    # 级的维度 axis=0，通过 tf.gather 函数收集数据，代码如下
    # (2, 35, 8)
    print(tf.gather(x, [0, 1], axis=0).shape)
    # 需要抽查所有班级的第 1、4、9、12、13、27 号同学的成绩数据
    # (4, 6, 8)
    print(tf.gather(x, [0, 3, 8, 11, 12, 26], axis=1).shape)
    # 如果需要收集所有同学的第 3 和第 5 门科目的成绩，则可以指定科目维度 axis=2
    # (4, 35, 2)
    print(tf.gather(x, [2, 4], axis=2).shape)
    # 如果希望抽查第[2,3]班级的第[3,4,6,27]号同学的科目成绩，
    # 则可以通过组合多个 tf.gather 实现。
    # 首先抽出第[2,3]班级
    xx = tf.gather(x, [1, 2], axis=0)
    # (2, 4, 8)
    print(tf.gather(xx, [2, 3, 5, 26], axis=1).shape)
    # 这次我们希望抽查第 2 个班级的第 2 个同学的所有科目，
    # 第 3 个班级的第 3 个同学的所有科目，第 4 个班级的第 4 个同学的所有科目
    a = tf.gather(tf.gather(x, [1], axis=0), [1], axis=1)
    b = tf.gather(tf.gather(x, [2], axis=0), [2], axis=1)
    c = tf.gather(tf.gather(x, [3], axis=0), [3], axis=1)
    # [1,1,8]
    print(a.shape)
    print(b.shape)
    print(c.shape)
    # tf.stack(tensors, axis)
    d = tf.stack([x[1, 1], x[2, 2], x[3, 3]], axis=0)
    # [[86 49 20 41 28 98 67 14]
    #  [16 78 96  9  4 65 51 87]
    #  [98 30 79 76 66 88 14 66]]
    print(d.numpy())

    pass
