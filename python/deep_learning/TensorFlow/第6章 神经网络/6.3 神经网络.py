#### 6.3 神经网络
import tensorflow as tf
from keras import layers, Sequential


if __name__ == "__main__":
    ###### 6.3.1 张量方式实现
    # 对于多层神经网络，以图 6.5 网络结构为例，需要分别定义各层的权值矩阵𝑾和偏置向量𝒃。

    # 有多少个全连接层，则需要相应地定义数量相当的𝑾和𝒃，

    # 并且每层的参数只能用于对应的层，不能混淆使用。

    # b = 10
    # x = tf.random.normal([b, 28 * 28])

    # w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1))
    # b1 = tf.Variable(tf.zeros([256]))

    # w2 = tf.Variable(tf.random.truncated_normal([256, 128], stddev=0.1))
    # b2 = tf.Variable(tf.zeros([128]))

    # w3 = tf.Variable(tf.random.truncated_normal([128, 64], stddev=0.1))
    # b3 = tf.Variable(tf.zeros([64]))

    # w4 = tf.Variable(tf.random.truncated_normal([64, 10], stddev=0.1))
    # b4 = tf.Variable(tf.zeros([10]))

    # # - 在计算时，只需要按照网络层的顺序，将上一层的输出作为当前层的输入即可，重复直至最后一层，并将输出层的输出作为网络的输出
    # # 梯度记录器
    # with tf.GradientTape() as tape:
    #     h1 = x @ w1 + tf.broadcast_to(b1, [x.shape[0], 256])
    #     h1 = tf.nn.relu(h1)

    #     h2 = h1 @ w2 + tf.broadcast_to(b2, [x.shape[0], 256])
    #     h2 = tf.nn.relu(h2)

    #     h3 = h2 @ w3 + tf.broadcast_to(b3, [x.shape[0], 256])
    #     h3 = tf.nn.relu(h3)

    #     h4 = h3 @ w4 + b4

    # - 最后一层是否需要添加激活函数通常视具体的任务而定，这里加不加都可以
    # 在使用 TensorFlow 自动求导功能计算梯度时，
    # 需要将前向计算过程放置在tf.GradientTape()环境中，
    # 从而利用 GradientTape 对象的 gradient()方法自动求解参数的梯度，
    # 并利用 optimizers 对象更新参数。

    # ###### 6.3.2 层方式实现
    # 对于常规的网络层，通过层方式实现起来更加简洁高效。
    # 1. 首先新建各个网络层类，并指定各层的激活函数类型
    # 256-> 128-> 64-> 10
    fc1 = layers.Dense(256, activation=tf.nn.relu)
    fc2 = layers.Dense(128, activation=tf.nn.relu)
    fc3 = layers.Dense(64, activation=tf.nn.relu)
    fc4 = layers.Dense(10)

    # 2. 在前向计算时，依序通过各个网络层即可

    # 模拟一个输入样本
    b = 10
    x = tf.random.normal([b, 28 * 28])
    h1 = fc1(x)
    h2 = fc2(h1)
    h3 = fc3(h2)
    h4 = fc4(h3)
    # h4 =  shape=(10, 10)
    print(h4)

    # 3. 对于这种数据依次向前传播的网络，也可以通过 Sequential 容器封装成一个网络大类对象，调用大类的前向计算函数一次即可完成所有层的前向计算，使用起来更加方便

    model = Sequential(
        [
            layers.Dense(256, activation=tf.nn.relu),
            layers.Dense(128, activation=tf.nn.relu),
            layers.Dense(64, activation=tf.nn.relu),
            layers.Dense(10),
        ]
    )
    # 4. 前向计算时只需要调用一次网络大类对象，即可完成所有层的按序计算
    out = model(x)
    # h4 = shape=(10, 10)
    print(out)
    print(float(out[0][0]) == float(h4[0][0]))
    print(float(out[5][0]) == float(h4[5][0]))

    pass
