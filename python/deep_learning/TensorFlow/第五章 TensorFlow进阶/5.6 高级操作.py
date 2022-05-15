import os

import keras.datasets.imdb
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.6 高级操作
    #
    # #### 5.6.1 tf.gather
    #
    # - tf.gather 可以实现根据索引号收集数据的目的
    # - tf.gather 非常适合索引号没有规则的场合，其中索引号可以乱序排列，此时收 集的数据也是对应顺序
    # Gather slices from params axis axis according to indices. indices must be an integer tensor of any dimension (often 1-D).
    # Tensor.getitem works for scalars, tf.newaxis, and python slices
    # tf.gather extends indexing to handle tensors of indices.
    # In the simplest case it's identical to scalar indexing:
    # 考虑班级成绩册的例子，
    # 假设共有 4个班级，每个班级 35 个学生，8 门科目，
    # 保存成绩册的张量 shape 为[4,35,8]。
    # x = tf.random.uniform([4, 35, 8], maxval=100, dtype=tf.int32)
    # # (4, 35, 8)
    # print(x.shape)
    # # 现在需要收集第 1~2 个班级的成绩册，可以给定需要收集班级的索引号：[0,1]，并指定班
    # # 级的维度 axis=0，通过 tf.gather 函数收集数据，代码如下
    # # (2, 35, 8)
    # print(tf.gather(x, [0, 1], axis=0).shape)
    # # 需要抽查所有班级的第 1、4、9、12、13、27 号同学的成绩数据
    # # (4, 6, 8)
    # print(tf.gather(x, [0, 3, 8, 11, 12, 26], axis=1).shape)
    # # 如果需要收集所有同学的第 3 和第 5 门科目的成绩，则可以指定科目维度 axis=2
    # # (4, 35, 2)
    # print(tf.gather(x, [2, 4], axis=2).shape)
    # # 如果希望抽查第[2,3]班级的第[3,4,6,27]号同学的科目成绩，
    # # 则可以通过组合多个 tf.gather 实现。
    # # 首先抽出第[2,3]班级
    # xx = tf.gather(x, [1, 2], axis=0)
    # # (2, 4, 8)
    # print(tf.gather(xx, [2, 3, 5, 26], axis=1).shape)
    # # 这次我们希望抽查第 2 个班级的第 2 个同学的所有科目，
    # # 第 3 个班级的第 3 个同学的所有科目，第 4 个班级的第 4 个同学的所有科目
    # a = tf.gather(tf.gather(x, [1], axis=0), [1], axis=1)
    # b = tf.gather(tf.gather(x, [2], axis=0), [2], axis=1)
    # c = tf.gather(tf.gather(x, [3], axis=0), [3], axis=1)
    # # [1,1,8]
    # print(a.shape)
    # print(b.shape)
    # print(c.shape)
    # # tf.stack(tensors, axis)
    # d = tf.stack([x[1, 1], x[2, 2], x[3, 3]], axis=0)
    # # [[86 49 20 41 28 98 67 14]
    # #  [16 78 96  9  4 65 51 87]
    # #  [98 30 79 76 66 88 14 66]]
    # print(d.numpy())
    #

    # #### 5.6.2 tf.gather_nd
    # tf.gather_nd的函数原型是：
    # def gather_nd(params, indices, name=None)
    # 根据定义， 其主要功能是根据indices描述的索引，提取params上的元素， 重新构建一个tensor
    # `N` dimensions of `params`, where `N = indices.shape[-1]`.

    # 我们希望抽查第 2 个班级的第 2 个同学的所有科目，
    # 第 3 个班级的第 3 个同学的所有科目，
    # 第 4 个班级的第 4 个同学的所有科目
    # x = tf.random.uniform([4, 35, 8], maxval=100, dtype=tf.int32)
    # # (3, 8)
    # print(tf.gather_nd(x, [[1, 1], [2, 2], [3, 3]]).shape)
    #
    # # 一般地，在使用 tf.gather_nd 采样多个样本时，
    # # 例如希望采样𝑖号班级，𝑗个学生，𝑘门科目的成绩，
    # # 则可以表达为[. . . , [𝑖, 𝑗, 𝑘], . . . ]，
    # # 外层的括号长度为采样样本的个数，内层列表包含了每个采样点的索引坐标
    #
    # # 我们抽出了班级 1 的学生 1 的科目 2、班级 2 的学生 2 的科目 3、
    # # 班级 3 的学生 3 的科目 4 的成绩，
    # # 共有 3 个成绩数据，结果汇总为一个 shape 为[3]的张量
    # # (3,)
    # print(tf.gather_nd(x, [[0, 0, 1], [1, 1, 2], [2, 2, 3]]).shape)

    # #### 5.6.3 tf.boolean_mask
    # tf.boolean_mask 的作用是 通过布尔值 过滤元素
    #
    # ```python
    # def boolean_mask(tensor, mask, name="boolean_mask", axis=None):
    #     """Apply boolean mask to tensor."""
    # ```
    # 除了可以通过给定索引号的方式采样，还可以通过给定掩码(Mask)的方式进行采样
    #
    # 这里的 tf.boolean_mask 的用法其实与 tf.gather 非常类似，
    # 只不过一个通过掩码 方式采样，一个直接给出索引号采样
    #
    # 可见 tf.boolean_mask 既可以实现了 tf.gather 方式的一维 掩码采样，
    # 又可以实现 tf.gather_nd 方式的多维掩码采样。

    # # 以 shape 为[4,35,8]的成绩册张量为例,即采样第 1 和第 4 个班级的数据
    # x = tf.random.uniform([4, 35, 8], maxval=100, dtype=tf.int32)
    # # (2,35,8)
    # print(tf.boolean_mask(x, [True, False, False, True], axis=0).shape)

    # 为了方便演示，我们将班级数量减少到 2 个，
    # 学生的数量减少到 3 个，即一个班级只有 3 个学生，shape 为[2,3,8]。
    # 如果希望采样第 1 个班级的第 1~2 号学生，第 2 个班级的第 2~3 号学生，
    # 通过tf.gather_nd 可以实现为
    # x = tf.random.uniform([2, 3, 8], maxval=100, dtype=tf.int32)
    # # gather_nd(params, indices, name=name, batch_dims=batch_dims)
    # # (4,8)
    # print(tf.gather_nd(x, [[0, 0], [0, 1], [1, 1], [1, 2]]))
    # # 多维掩码采样
    # # 两个[]说明从班级数量2中均取得，[]中三个boolean说明从 3 个学生中取
    # # (4,8)
    # print(tf.boolean_mask(x, ([True, True, False], [False, True, True])))

    # #### 5.6.4 tf.where
    # - 通过 tf.where(cond, a, b)操作可以根据 cond 条件的真假从参数𝑨或𝑩中读取数据
    #
    # 条件判定规则如下：
    # 𝑜𝑖 =
    # 1. 𝑎𝑖 cond𝑖为 True
    # 2. 𝑏𝑖 cond𝑖为 False

    #
    # 其中𝑖为张量的元素索引，返回的张量大小与𝑨和𝑩一致，当对应位置的cond𝑖为 True，𝑜𝑖从 𝑎𝑖中复制数据；当对应位置的cond𝑖为 False，𝑜𝑖从𝑏𝑖中复制数据。
    #
    # - 通过一系列的比较、索引号收集和掩码收集的操作组合是有很大的实际应用的

    # 考虑从 2 个全 1 和全 0 的 3 × 3大小的张量𝑨和𝑩中提取数据，
    # 其中cond𝑖为 True 的位置从𝑨中对应位置提取元素 1，
    # cond𝑖为 False 的位置从𝑩对应位置提取元素 0
    # a = tf.ones([3, 3])
    # b = tf.zeros([3, 3])
    # cond = tf.constant([[True, False, False],
    #                     [False, True, False],
    #                     [False, False, True]])
    # # [[1. 0. 0.]
    # #  [0. 1. 0.]
    # #  [0. 0. 1.]]
    # print(tf.where(cond, a, b))
    #
    # # -当参数 a=b=None 时，即 a 和 b 参数不指定，tf.where 会返回 cond 张量中所有 True 的元素的索引坐标。
    # # If `x` and `y` are not provided (both are None):
    # #   `tf.where` will return the indices of `condition` that are non-zero
    # # [[0 0]
    # #  [1 1]
    # #  [2 2]]
    # print(tf.where(cond))

    # 我们需要提取张量中所有正数的数据和索引。
    # 首先构造张量 a，并通过比较运算得到所有正数的位置掩码
    # x = tf.random.normal([3, 3])
    # mask = x > 0
    # print(x)
    # print(mask)
    # indices = tf.where(mask)
    #
    # # tf.gather_nd(x, [[1, 1], [2, 2], [3, 3]]
    # # tf.boolean_mask(x, [True, False, False, True], axis=0)
    #
    # # 拿到索引后，通过 tf.gather_nd 即可恢复出所有正数的元素：
    # print(tf.gather_nd(x, indices))
    # print(tf.boolean_mask(x, mask))

    # #### 5.6.5 scatter_nd
    #
    # 张量白板刷新，有目的性刷新
    #
    # 通过 tf.scatter_nd(indices, updates, shape)函数可以高效地刷新张量的部分数据，

    # 构造需要刷新数据的位置参数，即为 4、3、1 和 7 号位置
    # indices = [[4], [3], [1], [7]]
    # # 构造需要写入的数据，4 号位写入 4.4,3 号位写入 3.3，以此类推
    # updates = [4.4, 3.3, 1.1, 7.7]
    # # 在长度为 8 的全 0 向量上根据 indices 写入 updates 数据
    # # [0,1.1,0,3.3,4.4,0,0,7.7]
    # print(tf.scatter_nd(indices=indices, updates=updates, shape=[8]))

    # 但是这个函数只能在全 0 的白板张量上面执行刷新操作，
    #
    # 因此可能需要结合其它操作来实现现有张量的数据刷新功能。
    #
    # 直接用scatter_nd是从全0白板更新，如何从已有的数据上更新？
    #
    # 1. 假设A是待更新，从A中将待更新的部分值取出，用scatter_nd生成A'
    # 2. 拿A=A-A'清除待更新的部分值（clear）
    # 3. 新的值通过scatter_nd生成A'',则A=A+A''可进行部分更新

    # A = tf.range(8) * 2
    # indices = tf.range(1, 8, 2)
    # indices = tf.reshape(indices, shape=[4, -1])
    # print(indices)
    #
    # print(tf.reshape(tf.gather(A, indices), shape=[-1]))
    # # indices = [[1] [3] [5] [7]]
    # # tf.reshape(tf.gather(A, indices), shape=[-1]) =  [ 2  6 10 14]
    # A1 = tf.scatter_nd(indices=indices,
    #                    updates=tf.reshape(tf.gather(A, indices), shape=[-1]),
    #                    shape=[8])
    # # A1 = [ 0  2  0  6  0 10  0 14]
    # print(A1)
    # A = A - A1
    # # A = [ 0  0  4  0  8  0 12  0]
    # print(A)
    # updates = [2.2, 6.6, 10.10, 14.14]
    # A2 = tf.scatter_nd(indices=indices,
    #                    updates=updates,
    #                    shape=[8])
    # # A2 = [ 0.    2.2   0.    6.6   0.   10.1   0.   14.14]
    # print(A2)
    # A = tf.cast(A, dtype=tf.float32) + A2
    # # A = [ 0.    2.2   4.    6.6   8.   10.1  12.   14.14]
    # print(A)

    # #### 5.6.6 meshgrid
    #
    # - 通过 tf.meshgrid 函数可以方便地生成二维网格的采样点坐标，方便可视化等应用场合。
    #

    # 通过在 x 轴上进行采样 100 个数据点，y 轴上采样 100 个数据点，
    # 然后利用tf.meshgrid(x, y)即可返回这 10000 个数据点的张量数据，
    # 保存在 shape 为[100,100,2]的张量中。
    # 为了方便计算，tf.meshgrid 会返回在 axis=2 维度切割后的 2 个张量𝑨和𝑩，
    # 其中张量𝑨包含了所有点的 x 坐标，𝑩包含了所有点的 y 坐标，shape 都为[100,100]，实现如下

    """
        x = [1, 2, 3]
        y = [4, 5, 6]
        X, Y = tf.meshgrid(x, y)
        # X = [[1, 2, 3],
        #      [1, 2, 3],
        #      [1, 2, 3]]
        # Y = [[4, 4, 4],
        #      [5, 5, 5],
        #      [6, 6, 6]]
    """
    x = tf.linspace(-8, 8, 100)
    y = tf.linspace(-8, 8, 100)
    X, Y = tf.meshgrid(x, y)
    # (100, 100)
    # (100, 100)
    print(X.shape)
    print(Y.shape)

    # 利用生成的网格点坐标张量𝑨和𝑩，Sinc 函数在 TensorFlow 中实现如下：
    # sinc 函数实现
    z = tf.sqrt(X ** 2 + Y ** 2)
    z = tf.sin(z) / z

    # 通过 matplotlib 库即可绘制出函数在𝑥 ∈ [−8,8],𝑦 ∈ [−8,8]区间的 3D 曲面
    # import matplotlib
    # from matplotlib import pyplot as plt
    # # 导入 3D 坐标轴支持
    # from mpl_toolkits.mplot3d import Axes3D
    #
    # fig = plt.figure()
    # ax = Axes3D(fig)  # 设置 3D 坐标轴
    # # 根据网格点绘制 sinc 函数 3D 曲面
    # ax.contour3D(x.numpy(), y.numpy(), z.numpy(), 50)
    # plt.show()

    # - 通过 tf.stack([x,y],axis=2) 可以将x，y还原成对应的坐标
    # stack的操作：当axis ≥ 0时，在axis 之前插入；当axis < 0时，在 axis 之后插入新维度。
    cord = tf.stack([X, Y], axis=2)
    # cord.shape=(100, 100, 2)
    print(cord.shape)
    pass
