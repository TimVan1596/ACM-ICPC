import tensorflow as tf
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
    X, y = datasets.make_moons(n_samples=N_SAMPLES, noise=0.2, random_state=50)

    print(f"-- X.shape={X.shape}, y.shape={y.shape}")

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
    plt.show()
    plt.close()


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

    # ###### 7.9.2 网络层
    # 1. 通过新建类 Layer 实现一个网络层
    # - 通过新建类 Layer 实现一个网络层，需要传入网络层的输入节点数、输出节点数、激活函数类型等参数，
    # - 权值 weights 和偏置张量 bias 在初始化时根据输入、输出节点数自动生成并初始化。
    class Layer:
        # 1.全连接网络层
        def __init__(
            self, n_input, n_neurons, activation=None, weights=None, bias=None
        ):
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

    pass
