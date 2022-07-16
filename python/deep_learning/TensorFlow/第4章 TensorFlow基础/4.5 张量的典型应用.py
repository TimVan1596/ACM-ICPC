import os

import tensorflow as tf
from tensorflow import keras
from keras import layers

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    ### 4.5 张量的典型应用
    ##### 4.5.1 标量
    ##### 4.5.2 向量
    ##### 4.5.3 矩阵
    ##### 4.5.4 三维张量
    ##### 4.5.5 四维张量

    ##### 4.5.1 标量
    # 是一个简单的数字，维度数为; 0，shape; 为[]
    # 模拟MSE误差计算
    out = tf.random.uniform([4, 10])
    y = tf.constant([2, 3, 2, 0])
    y = tf.one_hot(y, depth=10)
    loss = tf.keras.losses.mse(y, out)
    loss = tf.reduce_mean(loss)
    # print(loss)

    ##### 4.5.2 向量
    ##### 4.5.3 矩阵
    ##### 4.5.4 三维张量
    # 三维的张量一个典型应用是表示序列信号，它的格式是; 𝑿 = [𝑏, sequence len, feature len];
    # 其中𝑏表示序列信号的数量，sequence; len; 表示序列信号在时间维度上的采样点数或步数， feature;
    # len; 表示每个点的特征长度。

    # num_words=单词按照它们出现的频率（在训练集中）进行排序，并且只保留最常见的单词。
    # (x_train, y_train), (x_test, y_test) \
    #     = keras.datasets.imdb.load_data(num_words=10000)
    # print(x_train.shape)
    # print(y_train.shape)
    # x_train = keras.preprocessing.sequence.pad_sequences(x_train, maxlen=80)
    # print(x_train.shape)
    # embedding = layers.Embedding(10000, 100)
    # out = embedding(x_train)
    # shape; 变为[25000, 80, 100]
    # 其中25000表示句子个数，80表示每个句子共80个单词,其中 100 表示每个单词编码为长度是 100 的向量
    # print(out.shape)
    ##### 4.5.5 四维张量
    # [𝑏, ℎ,, 𝑐]其中𝑏表示输入样本的数量，ℎ / 分别表示特征图的高 / 宽，𝑐表示特征图的通道数
    # 模拟创建32*32的彩色图片输入，个数为4
    x = tf.random.normal([4, 32, 32, 3])
    # 创建卷积神经网络
    layer = layers.Conv2D(16, kernel_size=3)
    out = layer(x)
    print(out.shape)
    print(layer.kernel.shape)
