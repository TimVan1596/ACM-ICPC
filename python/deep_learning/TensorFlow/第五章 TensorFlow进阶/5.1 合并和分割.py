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
    a = tf.random.normal([35, 8])
    b = tf.random.normal([35, 8])
    #     参数 axis 指定新维度插入的位置，axis 的用法与 tf.expand_dims 的一致，
    #     当axis ≥ 0时，在 axis 之前插入；
    #     当axis < 0时，在 axis 之后插入新维度。
    c = tf.stack([a, b], axis=0)
    #  axis=0,c.shape=(2, 35, 8)
    print(c.shape)
    c = tf.stack([a, b], axis=2)
    #  axis=2,c.shape=(35, 8, 2)
    print(c.shape)
    c = tf.stack([a, b], axis=-1)
    #  axis=-1,c.shape=(35, 2, 8)
    print(c.shape)
