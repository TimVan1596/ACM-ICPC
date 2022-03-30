import tensorflow as tf
import tensorflow.keras.datasets as datasets


# 1、获取数据集
# 2、数据集分成mini-batch
# 3、按照epoch进行更新
# 4、三层神经网络

# 获取数据集
def load_data(batch_size=200):
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
    train_dataset = train_dataset.batch(batch_size=200)
    return train_dataset


# 初始化参数
def init_parameters():
    # 每层的张量都需要被优化，故使用Variable类型
    # 并使用截断的正太分布初始化权值张量
    # 偏置向量初始化为 0 即可
    w1 = tf.Variable(tf.random.truncated_normal([784, 256], stddev=0.1))
    b1 = tf.Variable(tf.zeros(256))
    w2 = tf.Variable(tf.random.truncated_normal([256, 128], stddev=0.1))
    b2 = tf.Variable(tf.zeros(128))
    w3 = tf.Variable(tf.random.truncated_normal([128, 10], stddev=0.1))
    b3 = tf.Variable(tf.zeros(10))
    return w1, b1, w2, b2, w3, b3


# epoch进行训练
# 1 epoch=一代=只是一次遍历了训练集
def train_epoch(epoch, train_dataset, param, lr=0.001):
    w1, b1, w2, b2, w3, b3 = param[0], param[1], param[2], param[3], param[4], param[5]
    print(tensor_equal(w1, param[0]))
    print(tensor_equal(w1, param[1]))
    print(tensor_equal(b1, param[1]))

    # 总共300个step，每个step有200个数据
    # 300*200 = 600000 =  MNIST数据集数量
    for step, (x, y) in enumerate(train_dataset):
        # x.shape=(200, 784)  y.shape=(200, 10)
        with tf.GradientTape() as tape:
            # 三层结构为 784*256,256*128,128*10
            h1 = x @ w1 + tf.broadcast_to(b1, (x.shape[0], 256))
            pass


def train(epochs):
    # 1、获取数据集
    train_dataset = load_data(batch_size=200)
    # 2、初始化参数
    (w1, b1, w2, b2, w3, b3) = init_parameters()
    param = (w1, b1, w2, b2, w3, b3)
    # 3、epoch进行训练
    for epoch in range(epochs):
        train_epoch(epoch, train_dataset, param, lr=0.001)
        break
    pass


# 判断两个tensor的值是否相等
def tensor_equal(a, b):
    # 判断类型是否均为tensor
    if type(a) != type(b):
        return False
    if isinstance(a, type(tf.constant([]))) is not True:
        if isinstance(a, type(tf.Variable([]))) is not True:
            return False
    # 判断形状相等
    if a.shape != b.shape:
        return False
    # 逐值对比后若有False则不相等
    if not tf.reduce_min(tf.cast(a == b, dtype=tf.int32)):
        return False
    return True


if __name__ == '__main__':
    epochs = 5
    train(epochs)
