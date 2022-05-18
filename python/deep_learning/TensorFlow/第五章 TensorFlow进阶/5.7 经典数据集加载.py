import os

import tensorflow as tf
import keras.datasets as datasets

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.7 经典数据集加载
    #
    # 在 TensorFlow 中，keras.datasets 模块提供了常用经典数据集的自动下载、管理、加载与转换功能， 并且提供了 tf.data.Dataset 数据集对象

    # - 通过 datasets.xxx.load_data()函数即可实现经典数据集的自动加载，
    # 其中 xxx 代表具体 的数据集名称，如“CIFAR10”、“MNIST”。
    (x, y), (x_test, y_test) = datasets.mnist.load_data()
    #  x.shape=(60000, 28, 28)  y.shape=(60000,)
    #  x_test.shape=(10000, 28, 28)  y_test.shape=(10000,)
    # TensorFlow 会默认将数据缓存在用户目录下 的.keras/datasets 文件夹
    # C:\Users\用户\.keras\datasets
    print('x:', x.shape, 'y:', y.shape, 'x test:', x_test.shape, 'y test:',
          y_test.shape)

    # - 通过 load_data()函数会返回相应格式的数据
    #
    # 对于图片数据集 MNIST、CIFAR10 等，会返 回 2 个 tuple，第一个 tuple 保存了用于训练的数据 x 和 y 训练集对象；
    #
    # 第 2 个 tuple 则保存 了用于测试的数据 x_test 和 y_test 测试集对象，所有的数据都用 Numpy 数组容器保存。
    #
    # - 通过 Dataset.from_tensor_slices 可以将训练部分的数据图片 x 和标签 y 都转换成 Dataset 对象
    #
    # 数据加载进入内存后，需要转换成 Dataset 对象，才能利用 TensorFlow 提供的各种便捷功能。
    # (将numpy数据转换为dataset)
    train_db = tf.data.Dataset.from_tensor_slices((x, y))
    # <TensorSliceDataset element_spec=(TensorSpec(shape=(28, 28), dtype=tf.uint8, name=None), TensorSpec(shape=(), dtype=tf.uint8, name=None))>
    print(train_db)
    pass
