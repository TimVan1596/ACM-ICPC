### 5.2 数据统计
import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    # ##### 5.2.1 向量范数
    #
    # 向量范数(Vector Norm)是表征向量“长度”的一种度量方法，它可以推广到张量上在
    #  TensorFlow 中，可以通过 tf.norm(x, ord)求解张量的 L1、L2、∞等范数，
    #  其中参数ord 指定为 1、2 时计算 L1、L2 范数，指定为 np.inf 时计算∞ −范数
    x = tf.ones([2, 2])
    # 计算L1范数, 即绝对值之和, L1=4.0
    print(tf.norm(x, ord=1))
    # 计算L2范数, 即所有元素的平方和再开根号, L2=2.0
    print(tf.norm(x, ord=2))
    # 计算无穷范数, 即绝对值的最大值, 无穷范数=1
    print(tf.norm(x, ord=np.inf))
