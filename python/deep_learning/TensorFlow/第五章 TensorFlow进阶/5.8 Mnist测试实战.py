import os

import tensorflow as tf
import keras.datasets as datasets
import matplotlib.pyplot as plt

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "2"
print(tf.__version__)

# pyplot显示中文标签
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


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

    # 总共300个step，每个step有200个数据
    # 300*200 = 600000 =  MNIST数据集数量
    for step, (x, y) in enumerate(train_dataset):
        # x.shape=(200, 784)  y.shape=(200, 10)
        with tf.GradientTape() as tape:
            # 三层结构为 784*256,256*128,128*10
            # 第一层 (200, 784)*(784, 256)+(200,256) = (200,256)
            h1 = x @ w1 + b1
            h1 = tf.nn.relu(h1)
            # 第二层 (200,256)*(256, 128)+(200,128) = (200,128)
            h2 = h1 @ w2 + b2
            h2 = tf.nn.relu(h2)
            # 输出层 (200,128)*(128, 10)+(200,10) = (200,10)
            h3 = h2 @ w3 + b3
            out = tf.nn.relu(h3)
            # 计算均方差 mse = mean(sum(y-out)^2)
            loss = tf.square(y - out)
            loss = tf.reduce_mean(loss)
            grads = tape.gradient(loss, [w1, b1, w2, b2, w3, b3])
        # 梯度更新，原地更新
        w1.assign_sub(grads[0] * lr)
        b1.assign_sub(grads[1] * lr)
        w2.assign_sub(grads[2] * lr)
        b2.assign_sub(grads[3] * lr)
        w3.assign_sub(grads[4] * lr)
        b3.assign_sub(grads[5] * lr)
        if step % 200 == 0:
            tips = "[debug]:epoch={0},step={1} => loss:{2}" \
                .format(epoch, step, loss.numpy())
            print(tips)
    return loss.numpy()


def train(epochs):
    losses = []
    # 1、获取数据集
    train_dataset = load_data(batch_size=200)
    # 2、初始化参数
    (w1, b1, w2, b2, w3, b3) = init_parameters()
    param = (w1, b1, w2, b2, w3, b3)
    # 3、epoch进行训练
    for epoch in range(epochs):
        loss = train_epoch(epoch, train_dataset, param, lr=0.001)
        losses.append(loss)
    x = range(0, epochs)
    # 绘制曲线
    plt.plot(x, losses, color='orange',
             marker='s', label='训练')
    plt.xlabel('Epoch')
    plt.ylabel('MSE')
    plt.legend()
    plt.savefig('MNIST数据集的前向传播训练误差曲线.jpg')
    plt.show()
    plt.close()


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
    # ### 5.8 MNIST 测试实战
    # 　上一节前向传播和数据集的加载步骤：
    # 1、获取数据集
    # 2、数据集分成mini-batch
    # 3、按照epoch进行更新
    # 4、三层神经网络
    train(5)

    # 分类任务测试部分逻辑：
    # 1、传入参数（w1，b1，w2，b2，w3，b3）
    # 2、进行训练，获取最大下标
    # 3、结果转为0和1，统计为1的个数
    # 4、计算准确率ACC，并通过plt打印

    # 前面已经介绍并实现了前向传播和数据集的加载部分。现在我们来完成剩下的分类任务逻辑。
    #
    # 1. 在训练的过程中，通过间隔数个 Step 后打印误差数据，可以有效监督模型的训练进度
    # 2. 在若干个 Step 或者若干个 Epoch 训练后，可以进行一次测试(验证)，以获得模型的当前性能

    # 现在我们来利用学习到的 TensorFlow 张量操作函数，完成准确度的计算实战
    #
    # 1. 先考虑一个 Batch 的样本 x，通过前向计算可以获得网络的预测值。预测值 out 的 shape 为[𝑏, 10]，分别代表了样本属于每个类别的概率
    # 2. 我们根据 tf.argmax 函数选出概率最大值出现的索引号，也即样本最有可能的类别号
    # 3. 由于我们的标注 y 已经在预处理中完成了 one-hot 编码，这在测试时其实是不需要的，因此通过 tf.argmax 可以得到数字编码的标注 y
    # 4. 通过 tf.equal 可以比较这两者的结果是否相等
    # 5. 并求和比较结果中所有 True(转换为 1)的数量，即为预测正确的数量
    # 6. 预测正确的数量除以总测试数量即可得到准确度，并打印出来
    pass
