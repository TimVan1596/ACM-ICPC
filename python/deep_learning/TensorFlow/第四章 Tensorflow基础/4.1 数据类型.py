# 4.1 数据类型
# 首先来介绍 TensorFlow 中的基本数据类型，包含数值类型、字符串类型和布尔类型。
# 4.1.1 数值类型根据维度数来区分，可分为：标量、向量、矩阵和张量
# 4.1.2 字符串类型
# 4.1.3 布尔类型
import tensorflow as tf

if __name__ == '__main__':
    # 数值类型
    # a = 1.2
    # aa = tf.constant(a)
    # print(type(a), type(aa), tf.is_tensor(aa))

    # x = tf.constant([23, 3.1])
    # print(x)
    # print(x.numpy())
    # print(x.shape)

    # 字符串类型
    # a = tf.constant('Hello DeepLearning')
    # print(a)
    # print(tf.strings.lower(a))

    # 布尔类型
    a = tf.constant(True)
    print(a is True)
    print(a == True)
