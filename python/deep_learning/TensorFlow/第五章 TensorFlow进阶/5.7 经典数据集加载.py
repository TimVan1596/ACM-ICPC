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

    # #### 5.7.1 随机打散
    #
    # 通过 Dataset.shuffle(buffer_size)工具可以设置 Dataset 对象随机打散数据之间的顺序，

    # 防止每次训练时数据按固定顺序产生，从而使得模型尝试“记忆”住标签信息
    #
    # 其中，buffer_size 参数指定缓冲池的大小，一般设置为一个较大的常数即可。
    # 调用 Dataset提供的这些工具函数会返回新的 Dataset 对象

    # 随机打散样本，不会打乱样本与标签映射关系
    train_db = train_db.shuffle(10000)
    # <ShuffleDataset element_spec=(TensorSpec(shape=(28, 28), dtype=tf.uint8, name=None), TensorSpec(shape=(), dtype=tf.uint8, name=None))>
    print(train_db)

    # #### 5.7.2 批训练 .batch

    # 一般在网络的计算过程中会同时计算多个样本，我们把这种训练方式叫做批训练，
    # 其中一个批中样本的数量叫做 Batch Size。
    # 为了一次能够从 Dataset 中产生 Batch Size 数量的样本，需要设置 Dataset 为批训练方式
    # 其中 128 为 Batch Size 参数，即一次并行计算 128 个样本的数据
    train_db = train_db.batch(128)
    # <BatchDataset element_spec=(TensorSpec(shape=(None, 28, 28), dtype=tf.uint8, name=None), TensorSpec(shape=(None,), dtype=tf.uint8, name=None))>
    print(train_db)


    # #### 5.7.3 预处理
    #
    # Dataset 对象通过提供 map(func)工具函数，
    #
    # 可以非常方便地调用用户自定义的预处理逻辑，它实现在 func 函数里
    #
    # 例如，下方代码调用名为 preprocess 的函数完成每个样本的预处理：
    # # 自定义的预处理函数
    def preprocess(x, y):
        # 调用此函数时会自动传入 x,y 对象，shape 为[b, 28, 28], [b]

        x = tf.cast(x, dtype=tf.float32) / 255.0  # 标准化到 0~1
        x = tf.reshape(x, shape=[-1, 28 * 28])  # 打平
        y = tf.cast(y, dtype=tf.int32)  # 转成整型张量
        # one-hot 编码
        '''
            indices = [0, 1, 2]
            depth = 3
            tf.one_hot(indices, depth)  # output: [3 x 3]
            # [[1., 0., 0.],
            #  [0., 1., 0.],
            #  [0., 0., 1.]]
        '''
        y = tf.one_hot(y, depth=10)
        return x, y


    # ```python
    # # 预处理函数实现在 preprocess 函数中，传入函数名即可
    train_db = train_db.map(preprocess)
    # shape=(None, 784),shape=(None, 10)
    # <MapDataset element_spec=(TensorSpec(shape=(None, 784), dtype=tf.float32, name=None), TensorSpec(shape=(None, 10), dtype=tf.float32, name=None))>
    print(train_db)

    pass
