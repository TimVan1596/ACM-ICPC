import tensorflow as tf
import pandas as pd
from keras import utils, Model, layers, optimizers, losses


# 导入数据
def load_data(fname, path_url, column_names):
    """导入数据

    返回pandas.DataFrame类型的数据
    """

    # - 采用 Auto MPG 数据集，它记录了各种汽车效能指标与气缸数、重量、马力等其它因子的真实数据
    # - Auto MPG 数据集一共记录了 398 项数据，我们从 UCI 服务器下载并读取数据集到
    dataset_path = utils.get_file(fname, path_url)

    raw_dataset = pd.read_csv(
        dataset_path,
        names=column_names,
        na_values="?",
        comment="\t",
        sep=" ",
        skipinitialspace=True,
    )
    return raw_dataset


# 数据预处理
def preprocess(dataset, batch_size=32):
    """数据预处理

    input: dataset = pandas.DataFrame对象
    """
    dataset = dataset.dropna()

    # - 由于 Origin 字段为类别类型数据，我们将其移除，并转换为新的 3 个字段：USA、Europe 和 Japan，分别代表是否来自此产地
    # 处理类别型数据，其中 origin 列代表了类别 1,2,3,分布代表产地：美国、欧洲、日本
    # 先弹出(删除并返回)origin 这一列
    origin = dataset.pop("Origin")
    # 根据 origin 列来写入新的 3 个列
    dataset["USA"] = (origin == 1) * 1.0
    dataset["Europe"] = (origin == 2) * 1.0
    dataset["Japan"] = (origin == 3) * 1.0

    # - 按着 8:2 的比例切分数据集为训练集和测试集
    train_dataset = dataset.sample(frac=0.8, random_state=0)
    test_dataset = dataset.drop(train_dataset.index)

    # 移动 MPG 油耗效能这一列为真实标签 Y
    train_labels = train_dataset.pop("MPG")
    test_labels = test_dataset.pop("MPG")

    # - 统计训练集的各个字段数值的均值和标准差，并完成数据的标准化，通过 norm()函数实现
    train_stats = train_dataset.describe().transpose()

    # 标准化数据, 减去每个字段的均值，并除以标准差
    def norm(x, stats):
        return (x - stats["mean"]) / stats["std"]

    # 标准化训练集
    # normed_train_data.shape= (314, 9)
    normed_train_data = norm(train_dataset, train_stats)
    # 标准化测试集
    normed_test_data = norm(test_dataset, train_stats)

    # - 利用切分的训练集数据构建数据集对象
    train_db = tf.data.Dataset.from_tensor_slices(
        (normed_train_data.values, train_labels.values)
    )
    # 随机打散，批量化
    train_db = train_db.shuffle(100).batch(batch_size)
    return train_db, (normed_test_data, test_labels)


# 训练
def train(train_db, epoch=20):
    # 3. 训练
    # 创建网络类实例
    model = Network()
    # 通过 build 函数完成内部张量的创建，其中 4 为任意设置的 batch 数量，9 为输入特征长度
    model.build(input_shape=(None, 9))
    model.summary()
    # 加速梯度下降
    optimizer = optimizers.RMSprop(learning_rate=0.001)

    for epoch in range(epoch):
        loss = 0.0
        # 遍历一次训练集
        for step, (x, y) in enumerate(train_db):
            # 梯度记录器，训练时需要使用它
            with tf.GradientTape() as tape:
                # 通过网络获得输出
                out = model(x)
                # 计算 MSE
                loss = tf.reduce_mean(losses.MSE(y, out))
                mae_loss = tf.reduce_mean(losses.MAE(y, out))
        # 间隔性地打印训练误差
        if epoch % 10 == 0:
            print(epoch, float(loss))
            print(
                f"-epoch={epoch}, MSE_LSS={float(loss)}, MAE_LSS={float(mae_loss)}")
        # 计算梯度，并更新
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))


# 网络模型类
class Network(Model):
    # region
    # 6.8.2 创建网络
    # 考虑到 Auto MPG 数据集规模较小
    # 1. 我们只创建一个 3 层的全连接网络来完成 MPG值的预测任务。
    # 1. 输入𝑿的特征共有 9 种，因此第一层的输入节点数为 9。
    # 1. 第一层、第二层的输出节点数设计为64和64，
    # 1. 由于只有一种预测值，输出层输出节点设计为 1。

    # **步骤**

    # 1. 我们将网络实现为一个自定义网络类
    # 1. 只需要在初始化函数中创建各个子网络层，
    # 1. 并在前向计算函数 call 中实现自定义网络类的计算逻辑即可。
    # 1. 自定义网络类继承自keras.Model 基类，这也是自定义网络类的标准写法，以方便地利用 keras.Model 基类提供的 trainable_variables、save_weights 等各种便捷功能。
    # endregion

    # 回归网络模型
    def __init__(self):
        super(Network, self).__init__()
        # 创建 3 个全连接层
        # self.fc1 = layers.Dense(1)
        self.fc1 = layers.Dense(32, activation="relu")
        self.fc2 = layers.Dense(64, activation="relu")
        self.fc3 = layers.Dense(128, activation="relu")
        self.fc4 = layers.Dense(64, activation="relu")
        self.fc5 = layers.Dense(32, activation="relu")
        self.fc6 = layers.Dense(1)

    def call(self, inputs, training=None, mask=None):
        # 依次通过三个全连接层
        x = self.fc1(inputs)
        x = self.fc2(x)
        x = self.fc3(x)
        x = self.fc4(x)
        x = self.fc5(x)
        x = self.fc6(x)
        return x


# #### 6.8 汽车油耗预测实战
if __name__ == "__main__":
    # #### 6.8 汽车油耗预测实战
    # 本节我们将利用全连接网络模型来完成汽车的效能指标 MPG(Mile Per Gallon，每加仑燃油英里数)的预测问题实战

    # ###### 6.8.1 数据集
    # region
    fname = "auto-mpg.data"
    path_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"
    # 每一列的意义
    # MPG - 每加仑燃油英里
    # Cylinders - 气缸数
    # Displacement - 排量
    # Horsepower - 马力
    # Weight - 重量
    # Acceleration - 加速度
    # Model - 型号
    # Year - 年份
    # Origin - 产地
    # endregion
    column_names = [
        "MPG",
        "Cylinders",
        "Displacement",
        "Horsepower",
        "Weight",
        "Acceleration",
        "Model Year",
        "Origin",
    ]
    # 1. 导入数据
    dataset = load_data(fname, path_url, column_names)
    # 2. 数据预处理
    train_db, (test_data, test_labels) = preprocess(dataset, batch_size=128)

    # 3. 训练
    train(train_db, epoch=400)

    pass
