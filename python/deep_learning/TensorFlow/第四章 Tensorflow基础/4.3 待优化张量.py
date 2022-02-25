import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
import tensorflow as tf
import math

if __name__ == '__main__':
    # ### 4.3 待优化张量，可训练张量
    # tf.Variable: 专门的数据类型来支持梯度信息的记录：tf.Variable。
    # tf.Variable
    # 类型在普通的张量类型基础上添加了name，trainable等属性来支持计算图的构建。

    # 普通张量转为待优化张量
    a = tf.constant(range(-1, 3))
    aa = tf.Variable(a)
    print(aa.name)
    print(aa.trainable)
