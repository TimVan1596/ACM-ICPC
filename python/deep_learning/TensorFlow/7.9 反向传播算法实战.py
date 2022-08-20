from sklearn import datasets, model_selection
import numpy as np

# 导入数据
def load_data(N_SAMPLES=2000, TEST_SIZE=0.3):

    ###### 7.9.1 数据集
    # - 这里通过 scikit-learn 库提供的便捷工具生成 2000 个线性不可分的 2 分类数据集数据的特征长度为 2
    # - 所有的红色点为一类，所有的蓝色点为一类
    # - 可以看到每个类别数据的分布呈月牙状，并且是是线性不可分的，无法用线性网络获得较好效果。
    # - 我们按着7: 3比例切分训练集和测试集，其中2000 ∙ 0 3 = 600个样本点用于测试，不参与训练，剩下的 1400 个点用于网络的训练

    # 1. 数据集的采集直接使用 scikit-learn 提供的 make_moons 函数生成，设置采样点数和切割比率

    # 利用工具函数直接生成数据集
    # make_moons是函数用来生成数据集
    # 画两个相互交错的半圆。
    X, y = datasets.make_moons(n_samples=N_SAMPLES, noise=0.2, random_state=100)

    # 2. 可以通过如下可视化代码绘制数据集的分布
    # 调用 make_plot 函数绘制数据的分布，其中 X 为 2D 坐标，y 为标签
    make_plot(X, y, plot_name="分类数据集的可视化")
    # 将 2000 个点按着 7:3 分割为训练集和测试集
    # model_selection.train_test_split
    # 将数组或矩阵分割成随机序列和测试子集。
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        X, y, test_size=TEST_SIZE, random_state=42
    )
    return X_train, X_test, y_train, y_test


# 显示训练情况
def plot_history(history):
    import matplotlib.pyplot as plt

    hist = history
    plt.figure()
    plt.xlabel("Num of Epochs")
    plt.ylabel("value")
    plt.plot(hist["epoch"], hist["MSE"], label="MSE")
    # plt.plot(hist["epoch"], hist["val_loss"], label="val_loss")
    plt.plot(hist["epoch"], hist["accuracy"], label="accuracy")
    # plt.plot(hist["epoch"], hist["val_accuracy"], label="val_accuracy")
    plt.ylim([0, 1])
    plt.legend()
    plt.show()


# 绘制数据集的分布，X 为 2D 坐标，y 为数据点的标签
def make_plot(
    X, y, plot_name, file_name=None, XX=None, YY=None, preds=None, dark=False
):
    from matplotlib import pyplot as plt
    import seaborn as sns

    # matplotlib其实是不支持显示中文的 显示中文需要一行代码设置字体
    # 解决坐标轴负数的负号显示问题
    plt.rcParams["axes.unicode_minus"] = False

    if dark:
        plt.style.use("dark_background")
    else:
        # sns = seaborn
        # seaborn是python中的一个可视化库，是对matplotlib进行二次封装而成
        sns.set_style("whitegrid")
    plt.figure(figsize=(8, 6))
    axes = plt.gca()
    # Matplotlib.axes.Axes.set()
    # 设置xlabel，ylabel ，xlim ，ylim 和 title等
    axes.set(xlabel="$x_1$", ylabel="$x_2$")
    plt.title(plot_name, fontsize=15, fontproperties="SimHei")
    # 图像的边界位置调整
    plt.subplots_adjust(left=0.20)
    plt.subplots_adjust(right=0.80)
    if XX is not None and YY is not None and preds is not None:
        # contour和contourf都是画三维等高线图的，不同点在于contourf会对等高线间的区域进行填充
        # cm.Spectral = 光谱颜色图
        plt.contourf(XX, YY, preds.reshape(XX.shape), 25, alpha=1, cmap=cm.Spectral)
        plt.contour(
            XX,
            YY,
            preds.reshape(XX.shape),
            levels=[0.5],
            cmap="Greys",
            vmin=0,
            vmax=0.6,
        )
    # 绘制散点图，根据标签区分颜色
    plt.scatter(
        X[:, 0], X[:, 1], c=y.ravel(), s=40, cmap=plt.cm.Spectral, edgecolors="none"
    )
    # SVG是一种图形文件格式，它的英文全称为Scalable Vector Graphics，意思为可缩放的矢量图形
    plt.savefig("dataset.jpg")
    # plt.show()
    plt.close()


# ###### 7.9.2 网络层
# 1. 通过新建类 Layer 实现一个网络层
# - 通过新建类 Layer 实现一个网络层，需要传入网络层的输入节点数、输出节点数、激活函数类型等参数，
# - 权值 weights 和偏置张量 bias 在初始化时根据输入、输出节点数自动生成并初始化。
class Layer:
    # 1.全连接网络层
    def __init__(self, n_input, n_neurons, activation=None, weights=None, bias=None):
        """
        :param int n_input: 输入节点数
        :param int n_neurons: 输出节点数
        :param str activation: 激活函数类型
        :param weights: 权值张量，默认类内部生成
        :param bias: 偏置，默认类内部生成
        """
        # 通过正态分布初始化网络权值，初始化非常重要，不合适的初始化将导致网络不收敛
        self.weights = (
            weights
            if weights is not None
            else np.random.randn(n_input, n_neurons) * np.sqrt(1 / n_neurons)
        )
        self.bias = bias if bias is not None else np.random.rand(n_neurons) * 0.1
        # 激活函数类型，如’sigmoid’
        self.activation = activation
        # 激活函数的输出值 o
        self.last_activation = None
        # 用于计算当前层的 delta 变量的中间变量
        self.error = None
        # 记录当前层的 delta 变量，用于计算梯度
        self.delta = None
        pass

    # 2.网络层的前向传播函数实现如下，其中 last_activation 变量用于保存当前层的输出值
    def activate(self, x):
        # 前向传播函数
        r = np.dot(x, self.weights) + self.bias  # X@W+b
        # 通过激活函数，得到全连接层的输出 o
        self.last_activation = self._apply_activation(r)
        return self.last_activation

    # 3. 上述代码中的 self._apply_activation 函数实现了不同类型的激活函数的前向计算过程，
    # 尽管此处我们只使用 Sigmoid 激活函数一种
    def _apply_activation(self, r):
        # 计算激活函数的输出
        if self.activation is None:
            return r  # 无激活函数，直接返回
        # ReLU 激活函数
        elif self.activation == "relu":
            return np.maximum(r, 0)
        # tanh 激活函数
        elif self.activation == "tanh":
            return np.tanh(r)
        # sigmoid 激活函数
        elif self.activation == "sigmoid":
            return 1 / (1 + np.exp(-r))
        return r

    # 4. 针对于不同类型的激活函数，它们的导数计算实现如下
    def apply_activation_derivative(self, r):
        # 计算激活函数的导数
        # 无激活函数，导数为 1
        if self.activation is None:
            return np.ones_like(r)
        # ReLU 函数的导数实现
        elif self.activation == "relu":
            grad = np.array(r, copy=True)
            grad[r > 0] = 1.0
            grad[r <= 0] = 0.0
            return grad
        # tanh 函数的导数实现
        elif self.activation == "tanh":
            return 1 - r**2
        # Sigmoid 函数的导数实现
        # 5. 可以看到，Sigmoid 函数的导数实现为𝑟 (1 − 𝑟)，其中𝑟即为𝜎(𝑧)
        elif self.activation == "sigmoid":
            return r * (1 - r)
        return r


###### 7.9.3 网络模型
# 1. 创建单层网络类后，我们实现网络模型的 NeuralNetwork 类
# - 它内部维护各层的网络层 Layer 类对象
# - 可以通过 add_layer 函数追加网络层，实现创建不同结构的网络模型目的
class NeuralNetwork:
    # 神经网络模型大类
    def __init__(self):
        # 网络层对象列表
        # __foo__：一种约定，Python内部的名字，用来区别其他用户自定义的命名，以防冲突。
        # _foo：一种约定，用来指定变量私有。程序员用来指定私有变量的一种方式。
        # __foo：这个有真正的意义：解析器用_classname__foo来代替这个名字，以区别和其他类相同的命名。
        # _layers用来指定变量私有
        self._layers = []

    # 追加网络层
    def add_layer(self, layer):
        self._layers.append(layer)

    # 2. 网络的前向传播只需要循环调各个网络层对象的前向计算函数即可
    # 前向传播
    def feed_forward(self, X):
        for layer in self._layers:
            # 依次通过各个网络层
            X = layer.activate(X)
        return X

    # 4. 网络模型的反向传播实现稍复杂，需要从最末层开始，计算每层的𝛿变量，
    # 然后根据推导出的梯度公式，将计算出的𝛿变量存储在 Layer 类的 delta 变量中
    def backpropagation(self, X, y, learning_rate):
        # 反向传播算法实现
        # 前向计算，得到输出值
        output = self.feed_forward(X)
        # 反向循环
        # TODO 可以简化 i = 3 2 1 0
        for i in reversed(range(len(self._layers))):
            # 得到当前层对象
            layer = self._layers[i]
            # 如果是输出层
            if layer == self._layers[-1]:
                # 计算二分类任务的均方差的导数
                layer.error = y - output
                # 关键步骤：计算最后一层的 delta，参考输出层的梯度公式
                # 参见7.9 梯度示意图
                layer.delta = layer.error * layer.apply_activation_derivative(output)
            # 如果是隐藏层
            else:
                # 得到下一层对象
                next_layer = self._layers[i + 1]
                layer.error = np.dot(next_layer.weights, next_layer.delta)
                # 关键步骤：计算隐藏层的 delta，参考隐藏层的梯度公式
                # 参见7.9 梯度示意图
                layer.delta = layer.error * layer.apply_activation_derivative(
                    layer.last_activation
                )
        # 5. 在反向计算完每层的𝛿变量后，只需要按着𝜕ℒ/𝜕𝑤𝑖 = 𝑜𝑖𝛿j公式计算每层参数的梯度并更新网络参数即可
        # 循环更新权值
        for i in range(len(self._layers)):
            layer = self._layers[i]
            # o_i 为上一网络层的输出
            o_i = np.atleast_2d(X if i == 0 else self._layers[i - 1].last_activation)
            # 梯度下降算法，delta 是公式中的负数，故这里用加号
            layer.weights += layer.delta * o_i.T * learning_rate
        # 6. 因此，在 backpropagation 函数中，反向计算每层的𝛿变量，并根据梯度公式计算每层参数的梯度值，按着梯度下降算法完成一次参数的更新。

    # ###### 7.9.4 网络训练
    # 1. 这里的二分类任务网络设计为两个输出节点，因此需要将真实标签𝑦进行 One-hot 编码
    # 网络训练函数
    def train(self, X_train, X_test, y_train, y_test, learning_rate, max_epochs):
        # one-hot 编码
        # numpy索引多维数组
        # 即np.arange(y_train.shape[0])为行坐标，y_train为列坐标
        # 参考：https://www.numpy.org.cn/user/basics/indexing.html#%E7%B4%A2%E5%BC%95%E5%A4%9A%E7%BB%B4%E6%95%B0%E7%BB%84
        y_onehot = np.zeros((y_train.shape[0], 2))
        y_onehot[np.arange(y_train.shape[0]), y_train] = 1
        # 2. 将 One-hot 编码后的真实标签与网络的输出计算均方误差并调用反向传播函数更新网络参数
        # - 循环迭代训练集 1000 遍即可
        mses = []
        # 记录训练历史
        history = {
            "epoch": [],
            "accuracy": [],
            "MSE": [],
        }
        # 训练 max_epochs 个 epoch
        for i in range(max_epochs):
            # 一次训练一个样本
            for j in range(len(X_train)):
                self.backpropagation(X_train[j], y_onehot[j], learning_rate)
            if i % 10 == 0:
                # 打印出 MSE Loss
                mse = np.mean(np.square(y_onehot - self.feed_forward(X_train)))
                mses.append(mse)
                print("Epoch: #%s, MSE: %f" % (i, float(mse)))

                acc = self.accuracy(self.predict(X_test), y_test.flatten())
                history["epoch"].append(i)
                history["accuracy"].append(acc)
                history["MSE"].append(float(mse))

                # 统计并打印准确率
                print("Accuracy: %.2f%%" % (acc * 100))
        plot_history(history)
        return mses

    # 准确率
    def accuracy(self, pred, y):
        out = np.equal(pred, y, dtype=np.float32)
        correct = np.sum(out)
        return correct / len(out)

    # 进行预测（即前向传播）
    def predict(self, X_test):
        output = self.feed_forward(X_test)
        # return [int(np.where(elem == np.max(elem))[0]) for elem in output]
        return np.argmax(output, axis=1)


if __name__ == "__main__":
    # #### 7.9 反向传播算法实战
    # - 我们将实现一个 4 层的全连接网络，来完成二分类任务。
    # - 网络输入节点数为 2，隐藏层的节点数设计为：25、50和25
    # - 输出层两个节点，分别表示属于类别 1 的概率和类别 2的概率
    # - 直接利用均方误差函数计算与 One-hot 编码的真实标签之间的误差
    # - 所有的网络激活函数全部采用 Sigmoid 函数

    # 1. 导入数据
    # 采样点数
    N_SAMPLES = 2000
    # 测试数量比率
    TEST_SIZE = 0.3
    X_train, X_test, y_train, y_test = load_data(
        N_SAMPLES=N_SAMPLES, TEST_SIZE=TEST_SIZE
    )

    # 3. 根据网络结构配置，利用 NeuralNetwork 类创建网络对象，并添加 4 层全连接层
    # 实例化网络类
    network = NeuralNetwork()
    # 隐藏层 1, 2=>25
    network.add_layer(Layer(2, 25, "sigmoid"))
    # 隐藏层 2, 25=>50
    network.add_layer(Layer(25, 50, "sigmoid"))
    # 隐藏层 3, 50=>25
    network.add_layer(Layer(50, 25, "sigmoid"))
    # 输出层, 25=>2
    network.add_layer(Layer(25, 2, "sigmoid"))

    network.train(X_train, X_test, y_train, y_test, learning_rate=0.001, max_epochs=360)

    # ###### 7.9.5 网络性能
    # - self.accuracy
    # - 完整运行
    # 1. 我们将每个 Epoch 的训练损失ℒ值记录下，并绘制为曲线

    # 2. 在训练完 1000 个 Epoch 后，在测试集 600 个样本上得到的准确率为
    # 3. 在每个 Epoch 中，我们在测试集上完成一次准确度测试，并绘制成曲线
    # - 可以看到，随着 Epoch 的进行，模型的准确率稳步提升，开始阶段提升较快，后续提升较为平缓。

    pass
