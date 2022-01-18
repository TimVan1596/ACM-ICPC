import logging

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras

# 设置日志级别
logging.basicConfig(level=logging.CRITICAL)
# 设置绘图参数
plt_x = []
plt_loss = []


# 获取数据集并进行处理
def init_data():
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
    data_list = [[x_train, y_train], [x_test, y_test]]
    for data in data_list[:]:
        # 预处理步骤：x先归一化到[0,1]，再缩放至[-1,1]
        data[0] = ((tf.convert_to_tensor(data[0], dtype=tf.float32) / 255.0) - 0.5) * 2
    return data_list[0], data_list[1]


# 神经网络模型
def train_model(dataset, epoch_num=10, learning_rate=0.01):
    model = keras.Sequential([
        keras.layers.Dense(8, activation='relu'),
        keras.layers.Dense(5, activation='relu'),
        keras.layers.Dense(10, activation='relu')
    ])
    opt = keras.optimizers.SGD(learning_rate=learning_rate)
    index = 0
    for epoch in range(epoch_num):
        # 一个epoch
        for step, (x, y) in enumerate(dataset):
            index += 1
            with tf.GradientTape() as tape:
                x = tf.reshape(x, (-1, 28 * 28))
                out = model(x)
                y_one_hot = tf.one_hot(y, depth=10)
                loss = tf.square(out - y_one_hot)
                loss = tf.reduce_sum(loss) / x.shape[0]
            grads = tape.gradient(loss, model.trainable_variables)
            opt.apply_gradients(zip(grads, model.trainable_variables))
            if index % 100 == 0:
                plt_x.append(index)
                plt_loss.append(loss.numpy())
                print("{}-{}-{}:loss={}".format(index, epoch, step, loss.numpy()))


# matplotlib.pyplot的设置
def plt_init():
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.plot(plt_x, plt_loss, color='blue', label='loss')
    plt.xlabel("x/Train_Times")
    plt.legend()

    plt.title("Chapter3 MNIST")
    plt.show()


# 对手写数字进行训练（仅完成训练集的部分）
# 思路
# 1、获取训练集
# 2、前向传播：训练集使用三层网络进行训练
# 3、反向传播：获取LOSS并自动求导
# 4、集成：多次迭代
if __name__ == '__main__':
    # 暂时仅需训练集
    (x_train, y_train), _ = init_data()
    dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
    dataset = dataset.batch(128)

    train_model(dataset, epoch_num=3, learning_rate=0.005)
    plt_init()
