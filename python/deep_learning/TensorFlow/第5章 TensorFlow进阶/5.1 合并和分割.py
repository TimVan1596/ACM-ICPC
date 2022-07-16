# ## 第5章 TensorFlow 进阶
# ### 5.1 合并与分割
# ##### 5.1.1 合并
# 张量的合并可以使用拼接(Concatenate)和堆叠(Stack)操作实现
# - 拼接
#     在 TensorFlow 中，可以通过 tf.concat(tensors, axis)函数拼接张量
# - 堆叠
#     如果在合并数据 时，希望创建一个新的维度，则需要使用 tf.stack 操作。
#     使用 tf.stack(tensors, axis)可以堆叠方式合并多个张量，通过 tensors 列表表示，
#     参数 axis 指定新维度插入的位置，axis 的用法与 tf.expand_dims 的一致，当axis ≥ 0时
#     ，在 axis 之前插入；当axis < 0时，在 axis 之后插入新维度。
import tensorflow as tf

if __name__ == '__main__':
    # ### 5.1 合并与分割
    # ##### 5.1.1 合并
    # - 拼接
    #     在 TensorFlow 中，可以通过 tf.concat(tensors, axis)函数拼接张量
    # # 模拟成绩册 A [class,students,scores]
    # a = tf.random.normal([4, 35, 8])
    # # 模拟成绩册 B
    # b = tf.random.normal([6, 35, 8])
    # # 拼接合并成绩册
    # c = tf.concat([a, b], axis=0)
    # # c.shape = (10, 35, 8)
    # print(c.shape)

    # - 堆叠
    #     如果在合并数据 时，希望创建一个新的维度，则需要使用 tf.stack 操作
    #     使用 tf.stack(tensors, axis)可以堆叠方式合并多个张量
    # a = tf.random.normal([35, 8])
    # b = tf.random.normal([35, 8])
    # #     参数 axis 指定新维度插入的位置，axis 的用法与 tf.expand_dims 的一致，
    # #     当axis ≥ 0时，在 axis 之前插入；
    # #     当axis < 0时，在 axis 之后插入新维度。
    # c = tf.stack([a, b], axis=0)
    # #  axis=0,c.shape=(2, 35, 8)
    # print(c.shape)
    # c = tf.stack([a, b], axis=2)
    # #  axis=2,c.shape=(35, 8, 2)
    # print(c.shape)
    # c = tf.stack([a, b], axis=-1)
    # #  axis=-1,c.shape=(35, 2, 8)
    # print(c.shape)

    ##### 5.1.2 分割

    # 合并操作的逆过程就是分割
    #
    # - tf.split
    #   通过 tf.split(x, num_or_size_splits, axis)可以完成张量的分割操作 x 参数：待分割张量。
    #   num_or_size_splits 参数：切割方案。
    #   当 num_or_size_splits为单个数值时，如 10，表示等长切割为 10 份；
    # 模拟成绩册[class ,students, scores]
    #   当 num_or_size_splits 为 List 时，List 的每个元素表示每份的长 度，如[2,4,2,2]表示切割为 4 份，每份的长度依次是 2、4、2、2。
    x = tf.random.normal([10, 35, 8])
    result = tf.split(x, [1, 2, 3, -1], axis=1)
    # 4
    print(len(result))
    # (10, 29, 8)
    print(result[3].shape)
    #   axis 参数：指定分割的维度索引号。
    # - tf.unstack
    #   特别地，如果希望在某个维度上全部按长度为 1 的方式分割，还可以使用 tf.unstack(x, axis)函数。
    #   这种方式是 tf.split 的一种特殊情况，切割长度固定为 1，只需要指定切割维度 的索引号即可。
    x = tf.random.normal([10, 35, 8])
    result = tf.unstack(x, axis=0)
    # 10
    print(len(result))
