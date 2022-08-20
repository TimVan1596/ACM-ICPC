## 7.8 Himmelblau 函数优化实战
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import pyplot as plt, cm


# 1. 首先我们通过如下代码实现 Himmelblau 函数的表达式
def Himmelblau(input):
    # himmelblau 函数实现，传入参数 x 为 2 个元素的 List
    x = input[0]
    y = input[1]
    return (x**2 + y - 11) ** 2 + (x + y**2 - 7) ** 2


# Himmelblau 函数的可视化操作
def visual_functions():
    # 2. 然后完成 Himmelblau 函数的可视化操作。通过 np.meshgrid 函数生成二维平面网格点坐标
    # (TensorFlow 中也有meshgrid 函数)
    x = np.arange(-10, 10, 0.1)
    y = np.arange(-10, 10, 0.1)
    print("x,y range:", x.shape, y.shape)

    # 生成 x-y 平面采样网格点，方便可视化
    x_mesh, y_mesh = np.meshgrid(x, y)
    # print(f"X,Y maps:{x_mesh,y_mesh}")
    z_mesh = Himmelblau([x_mesh, y_mesh])

    # 3. 并利用 Matplotlib 库可视化 Himmelblau 函数
    # 绘制 himmelblau 函数曲面
    fig = plt.figure("himmelblau")
    # 设置 3D 坐标轴
    # gca = get current axes
    ax = fig.gca(projection="3d")
    # 3D 曲面图
    ax.plot_surface(
        x_mesh, y_mesh, z_mesh, cmap=cm.coolwarm, linewidth=0, antialiased=True
    )
    # 转换视角进行观察，通过设置VIEW_INIT(ELEV,AZIM)两个参数变化
    ax.view_init(45, 45)
    ax.set_xlabel("x")
    ax.set_ylabel("y")

    plt.show()


if __name__ == "__main__":
    #### 7.8 Himmelblau 函数优化实战

    """
    - Himmelblau 函数是用来测试优化算法的常用样例函数之一，它包含了两个自变量𝑥和𝑦
    1. 首先我们通过如下代码实现 Himmelblau 函数的表达式
    2. 然后完成 Himmelblau 函数的可视化操作。通过 np.meshgrid 函数(TensorFlow 中也有meshgrid 函数)生成二维平面网格点坐标
    3. 并利用 Matplotlib 库可视化 Himmelblau 函数
    4. Himmelblau 函数的等高线图，大致可以看出，它共有 4 个局部极小值点，并且局部极小值都是 0，所以这 4 个局部极小值也是全局最小值
    5. 利用 TensorFlow 自动求导来求出函数在𝑥和𝑦的偏导数，并循环迭代更新𝑥和𝑦值

    实际上，通过改变网络参数的初始化状态，程序可以得到多种极小值数值解。

    参数的初始化状态是可能影响梯度下降算法的搜索轨迹的，甚至有可能搜索出完全不同的数值解
    """
    # - Himmelblau 函数是用来测试优化算法的常用样例函数之一，它包含了两个自变量𝑥和𝑦
    # 1. 首先我们通过如下代码实现 Himmelblau 函数的表达式

    # 2. 然后完成 Himmelblau 函数的可视化操作。
    # visual_functions()

    # 4. Himmelblau 函数的等高线图，大致可以看出，它共有 4 个局部极小值点，并且局部极小值都是 0，所以这 4 个局部极小值也是全局最小值
    # 它们分别是：
    # (3,2), (−2.805, 3.131), (−3.779, −3.283), (3.584, −1.848)

    # 5. 利用 TensorFlow 自动求导来求出函数在𝑥和𝑦的偏导数，并循环迭代更新𝑥和𝑦值
    # 参数的初始化值对优化的影响不容忽视，可以通过尝试不同的初始化值，
    # 检验函数优化的极小值情况
    # [1., 0.], [-4, 0.], [4, 0.]
    # 初始化参数
    x = tf.constant([-4.0, 0.0])

    for step in range(200):
        # 梯度跟踪
        with tf.GradientTape() as tape:
            # 加入梯度跟踪列表
            tape.watch([x])
            # 前向传播
            y = Himmelblau(x)
        # 反向传播
        grads = tape.gradient(y, [x])[0]
        # 更新参数
        x -= 0.01*grads
        # 打印优化的极小值
        if step % 20 == 19:
            print ('step {}: x = {}, f(x) = {}'.format(step, x.numpy(), y.numpy()))
        
    pass
