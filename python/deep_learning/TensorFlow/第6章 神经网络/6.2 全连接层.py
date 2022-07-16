# #### 6.2 全连接层
import tensorflow as tf
from keras import layers


if __name__ == "__main__":

    # 6.2.1 张量方式实现

    # 在 TensorFlow 中，要实现全连接层，只需要定义好权值张量𝑾和偏置张量𝒃，
    # 并利用TensorFlow 提供的批量矩阵相乘函数 tf.matmul()即可完成网络层的计算。

    # 例如，创建输入𝑿 矩阵为𝑏 = 2个样本，每个样本的输入特征长度为𝑑in = 784，
    # x = tf.random.normal(shape=[2, 784])
    # print(x.shape)

    # 输出节点数为𝑑out = 256，故定义权值矩阵𝑾的 shape 为[784,256]，
    # 并采用正态分布初始化𝑾；偏置向量𝒃的 shape 定义为[256]，
    # w = tf.random.normal(shape=[784, 256])
    # b = tf.random.normal(shape=[256])

    # 在计算完𝑿@𝑾后相加即可，最终全连接层的输出𝑶的 shape 为[2,256]，
    # 即 2 个样本的特征，每个特征长度为 256
    # o = x@w+b
    # print(o.shape)

    # 6.2.2 层方式实现

    # TensorFlow 中有更高层、使用更方便的层实现方式：
    # layers.Dense(units, activation)。
    # 通过 layer.Dense 类，只需要指定输出节点数 Units 和激活函数类型 activation 即可。

    # 导入层模块 28*28=784
    x = tf.random.normal([4, 28 * 28])
    # 创建全连接层，指定输出节点数和激活函数
    fc = layers.Dense(512, activation=tf.nn.relu)
    # <keras.layers.core.dense.Dense object at 0x000002A368E14FA0>
    print(fc)
    # 通过 fc 类实例完成一次全连接层的计算，返回输出张量
    h1 = fc(x)
    # h1 = tf.Tensor shape=(4, 512)
    print(h1)

    # 输入的节点数在fc(x)计算时自动获取，并创建内部权值张量𝑾和偏置张量𝒃
    # - 可以通过类内部的成员名 kernel 和 bias 来获取权值张量 𝑾 和偏置张量 𝒃 对象
    # fc.kernel = tf.Variable shape=(784, 512)
    print(fc.kernel)
    # fc.bias = tf.Variable shape=(512,)
    print(fc.bias)
    # - 在优化参数时，需要获得网络的所有待优化的张量参数列表，
    # 可以通过类的 trainable_variables 来返回待优化参数列表
    # fc.trainable_variables = tf.Variable 'dense/kernel:0' 和 tf.Variable 'dense/bias:0'
    print("@fc.trainable_variables=", fc.trainable_variables)
    # - 还有部分层包含了不参与梯度优化的张量，如后续介绍的 Batch Normalization 层，
    # 可以通过non_trainable_variables 成员返回所有不需要优化的参数列表。
    # 如果希望获得所有参数列表，可以通过类的 variables 返回所有内部张量列表

    print("@fc.variables=", fc.variables)

    # - 对于全连接层，内部张量都参与梯度优化，故 variables 返回的列表与 trainable_variables 相同。
    # - 利用网络层类对象进行前向计算时，只需要调用类的**call**方法即可，
    #     即写成 fc(x)方式便可，它会自动调用类的**call**方法，在**call**方法中会自动调用 call 方法

    pass
