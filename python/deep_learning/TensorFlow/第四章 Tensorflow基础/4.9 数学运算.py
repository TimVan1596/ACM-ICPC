import os

os.environ['TF_CPP_MIN_LEVEL_LOG'] = '1'
import tensorflow as tf

if __name__ == '__main__':
    ### 4.9 数学运算
    ##### 4.9.1 加、减、乘、除运算
    # 分别通过tf.add, tf.subtract, tf.multiply,tf.divide函数实现，
    # TensorFlow已经重载了 +、 − 、 ∗ 、 / 运算符(推荐)
    # a = tf.range(5)
    # b = tf.constant(2)
    # print(a % b)
    ##### 4.9.2 乘方运算
    # 通过tf.pow(x, a)可以方便地完成𝑦 = 𝑎的乘方运算，也可以通过运算符 ** 实现 ∗∗ 𝑎运算
    # 特别地，对于常见的平方和平方根运算，可以使用tf.square(x)和tf.sqrt(x)实现。
    # a = tf.range(5)
    # print(a ** 2)
    a = tf.constant([0, 1, 2, 4], dtype=float)
    # print(tf.square(a))
    # print(tf.sqrt(a))
    ##### 4.9.3 指数和对数运算
    # 1.通过tf.pow(a, x)或者 ** 运算符也可以方便地实现指数运算𝑎的𝑥
    # 2.特别地，对于自然指数e𝑥，可以通过tf.exp(x)实现
    # print(tf.exp(0.0))
    # 3.在TensorFlow中，自然对数loge可以通过tf.math.log(x)实现
    # 4.如果希望计算其它底数的对数，可以根据对数的换底公式, 间接地通过tf.math.log(x)实现
    # print(tf.math.log(2.71))
    # print(tf.math.log(100.0)/tf.math.log(10.0))
    ##### 4.9.4 矩阵相乘运算
    # 通过 @ 运算符可以方便的实现矩阵相乘，还可以通过tf.matmul(a, b)函数实现。
    # 当张量𝑨和𝑩维度数大于2时，TensorFlow会选择𝑨和𝑩的最后两个维度进行矩阵相乘，前面所有的维度都视作Batch维度。
    a = tf.random.normal([4, 9, 2])
    b = tf.random.normal([2, 3])
    print((a @ b).shape)
    ##### 4.9.5 运算的分类
    # 1.element - wise
    # +- * /，即两向量按元素两两对应，逐个相运算
    # 2.matrix - wise
    # @和matual，即以矩阵相乘的方式进行
    # 3.dim - wise
    # reduce_mean / max / min / sum，按维度进行运算
    pass
