import tensorflow as tf
import tensorflow.keras.datasets as datasets


# 1、获取数据集
# 2、数据集分成mini-batch
# 3、按照epoch进行更新
# 4、三层神经网络

# 获取数据集
def load_data():
    # 1、获取 MNIST 数据集
    (x, y), (_, _) = datasets.mnist.load_data()
    # 2、数据预处理：x转为浮点数，并缩放到-1~1，最后改变视图
    #               y转为整数 ，并转为独热编码
    # x = (60000, 28, 28) y=(60000,)
    x = tf.convert_to_tensor(x, dtype=tf.float32) / 255
    x = tf.reshape(x, (-1, 28 * 28))
    y = tf.convert_to_tensor(y, dtype=tf.int32)
    y = tf.one_hot(y, depth=10)
    # 3、构建数据集对象，进行mini-batch分组
    train_dataset = tf.data.Dataset.from_tensor_slices((x, y))
    # 批量训练
    train_dataset = train_dataset.batch(200)
    return train_dataset


def train():
    # 获取数据集
    train_dataset = load_data()


if __name__ == '__main__':
    train()
