## TensorFlow深度学习

## 第4章 TensorFlow 基础

### 4.1 数据类型

首先来介绍 TensorFlow 中的基本数据类型，包含数值类型、字符串类型和布尔类型。  
4.1.1 数值类型根据维度数来区分，可分为：标量、向量、矩阵和张量  
4.1.2 字符串类型  
4.1.3 布尔类型

### 4.2 数值精度

常用的精度类型有 tf.int16、tf.int32、tf.int64、tf.float16、tf.float32、 tf.float64 等。  
其中 tf.float64 即为 tf.double。  
4.1.1 读取精度使用a.dtype  
4.1.2 类型转换使用tf.cast(a,dtype=tf.float32)

### 4.3 待优化张量

tf.Variable:专门的数据类型来支持梯度信息的记录：tf.Variable。  
tf.Variable 类型在普通的张量类型基础上添加了name，trainable 等属性来支持计算图的构建。

### 4.4 创建张量

可以通过多种方式创建张量，如从 Python 列表对象创建，从Numpy 数组创建，或者创建采样自某种已知分布的张量等。

##### 4.4.1 通过从数组、numpy列表使用tf.constant()对象创建

##### 4.4.2 创建全 0 或全 1 张量

通过tf.zeros()和 tf.ones()即可创建任意形状，且内容全 0 或全 1 的张量。  
tf.\*_like 是一系列的便捷函数，可以通过 tf.zeros(a.shape)等方式实现。

##### 4.4.3 创建自定义数值张量

通过tf.fill(shape, value)可以创建全为自定义数值 value 的张量，形状由 shape 参数指 定。

##### 4.4.4 创建已知分布的张量

通过 tf.random.normal(shape, mean=0.0, stddev=1.0)可以创建形状为 shape，均值为 mean，标准差为 stddev 的正态分布𝒩(mean,stddev2)。  
通过 tf.random.uniform(shape, minval=0, maxval=None, dtype=tf.float32)可以创建采样自[minval, maxval)区间的均匀分布的张量。
如果需要均匀采样整形类型的数据，必须指定采样区间的最大值 maxval 参数，同时指 定数据类型为 tf.int*型。

##### 4.4.5 创建序列

tf.range(limit, delta=1)可以创建[0, limit)之间，步长为 delta 的整型序列，不包含 limit 本身。  
通过 tf.range(start, limit, delta=1)可以创建[start,limit)，步长为 delta 的序列，不包含 limit 本身

### 4.5 张量的典型应用

##### 4.5.1 标量

是一个简单的数字，维度数为 0，shape 为[]

##### 4.5.2 向量

##### 4.5.3 矩阵

##### 4.5.4 三维张量

三维的张量一个典型应用是表示序列信号，它的格式是 𝑿 = [𝑏, sequence len, feature len]  
其中𝑏表示序列信号的数量，sequence len 表示序列信号在时间维度上的采样点数或步数， feature len 表示每个点的特征长度。

##### 4.5.5 四维张量

[𝑏, ℎ, w, 𝑐]其中𝑏表示输入样本的数量，ℎ/w 分别表示特征图的高/宽，𝑐表示特征图的通道数

### 4.6 索引与切片

##### 4.6.1 索引

##### 4.6.2 切片

通过start: end: step切片方式,end 为结束读取位置的索引(不包含 end 位)

##### 4.6.3 选择索引

- tf.gather(params,indices,axis=0)
  从params的axis维根据indices的参数值获取切片
- tf.gather_nd( params, indices, name=None)
  按照indices的格式从params中抽取切片（合并为一个Tensor） indices是一个K维整数Tensor，
- tf.boolean_mask(tensor, mask, name="boolean_mask", axis=None)
  tf.boolean_mask 的作用是通过布尔值过滤元素

### 4.7 维度变换

##### 4.7.1 改变视图

改变 x 的视图，存储并未改变

##### 4.7.2 增、删维度

- tf.expand_dims(x, axis)  
  通过 tf.expand_dims(x, axis)可在指定的 axis 轴前可以插入一个新的维度  
  需要注意的是，tf.expand_dims 的 axis 为正时，表示在当前维度之前插入一个新维度；为 负时，表示当前维度之后插入一个新的维度。
- tf.squeeze(x, axis)  
  删除维度 是增加维度的逆操作，与增加维度一样，删除维度只能删除长度为 1 的维 度，也不会改变张量的存储。如果希望将 图片数量维度删除，可以通过 tf.squeeze(x, axis)函数，axis 参数为待删除的维度的索引号

##### 4.7.3 交换维度

使用 tf.transpose(x, perm)函数完成维度交换操作，其中参数 perm 表示新维度的顺序 List

##### 4.7.4 复制数据

当通过增加维度操作插入新维度后，可能希望在新的维度上面复制若干份数据。  
可以通过 tf.tile(x, multiples)函数完成数据在指定维度上的复制操作，multiples 分别指 定了每个维度上面的复制倍数，对应位置为 1 表明不复制，为 2 表明新长度为原来长度的 2 倍，即数据复制一份，以此类推。

### 4.8 Broadcasting

Broadcasting 称为广播机制(或自动扩展机制)，它是一种轻量级的张量复制手段，  
在逻辑上扩展张量数据的形状，但是只会在需要时才会执行实际存储复制操作。

- 靠右对齐，先考虑小维度再拓展至大维度

1. 如果当前维度为1，拓展至相同
2. 如果没有维度，插入新维度再拓展至相同
3. 否则不支持广播

通过 tf.broadcast_to(x, new_shape)函数可以显式地执行自动扩展功能

### 4.9 数学运算

##### 4.9.1 加、减、乘、除运算

分别通过 tf.add, tf.subtract, tf.multiply,tf.divide函数实现， TensorFlow 已经重载了+、 − 、 ∗ 、/运算符(推荐)

##### 4.9.2 乘方运算

通过 tf.pow(x, a)可以方便地完成𝑦 = 𝑎的乘方运算，也可以通过运算符**实现 ∗∗ 𝑎运 算  
特别地，对于常见的平方和平方根运算，可以使用 tf.square(x)和 tf.sqrt(x)实现。

##### 4.9.3 指数和对数运算

1. 通过 tf.pow(a, x)或者**运算符也可以方便地实现指数运算𝑎的𝑥
2. 特别地，对于自然指数e𝑥，可以通过 tf.exp(x)实现
3. 在 TensorFlow 中，自然对数loge 可以通过 tf.math.log(x)实现
4. 如果希望计算其它底数的对数，可以根据对数的换底公式,间接地通过 tf.math.log(x)实现

##### 4.9.4 矩阵相乘运算

通过@运算符可以方 便的实现矩阵相乘，还可以通过 tf.matmul(a, b)函数实现。 当张量𝑨和𝑩维度数大 于 2 时，TensorFlow 会选择𝑨和𝑩的最后两个维度进行矩阵相乘， 前面所有的维度都视作 Batch 维度。

##### 4.9.5 运算的分类

1. element-wise  
   +-*/，即两向量按元素两两对应，逐个相运算
2. matrix-wise  
   @和matual，即以矩阵相乘的方式进行
3. dim-wise  
   reduce_mean/max/min/sum，按维度进行运算

### 4.10 前向传播实战

完成三层神经网络的实现：  
out = 𝑅𝑒𝐿𝑈{𝑅𝑒𝐿𝑈{𝑅𝑒𝐿𝑈[𝑿@𝑾1 + 𝒃1]@𝑾2 + 𝒃2}@𝑾 + 𝒃 }

1. 获取数据集 1、获取 MNIST 数据集  
   2、数据预处理：x转为浮点数，并缩放到-1~1，最后改变视图  
   y转为整数 ，并转为独热编码  
   3、构建数据集对象，进行mini-batch分组

2. 初始化参数
3. 按照epoch进行更新
4. 三层神经网络

## 第5章 TensorFlow 进阶

### 5.1 合并与分割

##### 5.1.1 合并

张量的合并可以使用拼接(Concatenate)和堆叠(Stack)操作实现

- 拼接

  在 TensorFlow 中，可以通过 tf.concat(tensors, axis)函数拼接张量
- 堆叠

  如果在合并数据 时，希望创建一个新的维度，则需要使用 tf.stack 操作。  
  使用 tf.stack(tensors, axis)可以堆叠方式合并多个张量，通过 tensors 列表表示，参数 axis 指定新维度插入的位置，axis 的用法与 tf.expand_dims 的一致，当axis ≥ 0时，在
  axis 之前插入；当axis < 0时，在 axis 之后插入新维度。

##### 5.1.2 分割

合并操作的逆过程就是分割

- tf.split

  通过 tf.split(x, num_or_size_splits, axis)可以完成张量的分割操作 x 参数：待分割张量。 num_or_size_splits 参数：切割方案。当 num_or_size_splits

  为单个数值时，如 10，表示等长切割为 10 份；当 num_or_size_splits 为 List 时，List 的每个元素表示每份的长 度，如[2,4,2,2]表示切割为 4 份，每份的长度依次是 2、4、2、2。

  axis 参数：指定分割的维度索引号。
- tf.unstack

  特别地，如果希望在某个维度上全部按长度为 1 的方式分割，还可以使用 tf.unstack(x, axis)函数。

  这种方式是 tf.split 的一种特殊情况，切割长度固定为 1，只需要指定切割维度 的索引号即可。

### 5.2 数据统计

##### 5.2.1 向量范数

向量范数(Vector Norm)是表征向量“长度”的一种度量方法，它可以推广到张量上在

TensorFlow 中，可以通过 tf.norm(x, ord)求解张量的 L1、L2、∞等范数，

其中参数ord 指定为 1、2 时计算 L1、L2 范数，指定为 np.inf 时计算∞ −范数

##### 5.2.2 最值、均值、和

通过 tf.reduce_max、tf.reduce_min、tf.reduce_mean、tf.reduce_sum 函数

可以求解张量 在某个维度上的最大、最小、均值、和，也可以求全局最大、最小、均值、和信息。

这样的操作相当于减维，因此用reduce前缀

- 通过 tf.reduce_max 函数实现最大值
- 当不指定 axis 参数时，tf.reduce_*函数会求解出全局元素的最大、最小、均值、和等 数据
- 通过 tf.reduce_mean 在样本数维度上计算均值
- 求和函数 tf.reduce_sum(x, axis)，它可以求解张量在 axis 轴上所有 特征的和
- 通过 tf.argmax(x, axis)和 tf.argmin(x, axis)可以求解在 axis 轴上，x 的最大值、最小值所 在的索引号

### 5.3 张量比较和排序

#### 5.3.1 张量比较

通过 tf.equal(a, b)(或 tf.math.equal(a, b)，两者等价)函数可以比较这 2 个张量是否相等

tf.equal()函数返回布尔类型的张量比较结果

除了比较相等的 tf.equal(a, b)函数，其它的比较函数用法类似，如:

1. tf.math.greater
2. tf.math.less
3. tf.math.greater_equal...等

- tf.unique 返回去除重复的与索引号

#### 5.3.2 张量排序

1. 排序sort,argsort:求排序和索引：
   **特别的，argsort是原来元素在排序后所在的下标**
2. 前k大值 Top_k,res=tf.math.top_k(a,2)
3. Top Acc:前N个中有没有命中的准确率，即使用top_k和target进行比较
4. tf.unique() 返回去除重复的与给出索引，并且可以用tf.gather()进行还原

### 5.4 填充与复制

#### 5.4.1 填充

填充操作可以通过 tf.pad(x, paddings)函数实现。

参数 paddings 是包含了多个[Left Padding,Right Padding]的嵌套方案 List

如[[0,0],[2,1],[1,2]]表示第一个维度不填 充，第二个维度左边(起始处)填充两个单元，右边(结束处)填充一个单元，第三个维度左边 填充一个单元，右边填充两个单元

#### 5.4.2 复制

1. 通过 tf.tile 函数可以在任意维度将数据重复复制多份

   如 shape 为[4,32,32,3]的数据， 复制方案为 multiples=[2,3,3,1]，

   即通道数据不复制，高和宽方向分别复制 2 份，图片数再 复制 1 份

2. 复制推荐使用tf.broadcast_to， **仅适用[3, 4]->[2, 3, 4]**
   tf.broadcast_to(input, shape, name=None)既不占用空间，也能达到复制效果

### 5.5 数据限幅

1. 通过 tf.maximum(x, a)实现数据的下限幅，即𝑥 ∈ [𝑎, +∞)；
2. 可以通过 tf.minimum(x, a)实现数据的上限幅，即𝑥 ∈ (−∞,𝑎]
3. 通过组合 tf.maximum(x, a)和 tf.minimum(x, b)可以实现同时对数据的上下边界限幅，即 𝑥 ∈ [𝑎, 𝑏]
4. 使用 tf.clip_by_value 实现上下限幅
5. 使用 tf.clip_by_norm 等比例放缩来减小L2范数,实现对梯度进行裁剪，等比例放缩，防止梯度爆炸
6. 使用 tf.clip_by_global_norm 实现整体缩放，通过权重梯度的总和的比率来截取多个张量的值

### 5.6 高级操作

#### 5.6.1 tf.gather

- tf.gather 可以实现根据索引号收集数据的目的
- tf.gather 非常适合索引号没有规则的场合，其中索引号可以乱序排列，此时收 集的数据也是对应顺序

#### 5.6.2 tf.gather_nd

tf.gather_nd的函数原型是：

def gather_nd(params, indices, name=None)

根据定义， 其主要功能是根据indices描述的索引，提取params上的元素， 重新构建一个tensor

\`N\` dimensions of \`params\`, where \`N = indices.shape[-1]\`.

一般地，在使用 tf.gather_nd 采样多个样本时，例如希望采样𝑖号班级，𝑗个学生，𝑘门 科目的成绩，则可以表达为[. . . , [𝑖, 𝑗, 𝑘], . . . ]，外层的括号长度为采样样本的个数，内层列表
包含了每个采样点的索引坐标

#### 5.6.3 tf.boolean_mask

tf.boolean_mask 的作用是 通过布尔值 过滤元素

```python
def boolean_mask(tensor, mask, name="boolean_mask", axis=None):
    """Apply boolean mask to tensor."""
```

除了可以通过给定索引号的方式采样，还可以通过给定掩码(Mask)的方式进行采样

这里的 tf.boolean_mask 的用法其实与 tf.gather 非常类似，只不过一个通过掩码 方式采样，一个直接给出索引号采样

可见 tf.boolean_mask 既可以实现了 tf.gather 方式的一维 掩码采样，又可以实现 tf.gather_nd 方式的多维掩码采样。

**上面的 3 个操作比较常用，尤其是 tf.gather 和 tf.gather_nd 出现的频率较高，必须掌握**

#### 5.6.4 tf.where

- 通过 tf.where(cond, a, b)操作可以根据 cond 条件的真假从参数𝑨或𝑩中读取数据

条件判定规则如下：

𝑜𝑖 =

1. 𝑎𝑖 cond𝑖为 True

2. 𝑏𝑖 cond𝑖为 False

其中𝑖为张量的元素索引，返回的张量大小与𝑨和𝑩一致，当对应位置的cond𝑖为 True，𝑜𝑖从 𝑎𝑖中复制数据；当对应位置的cond𝑖为 False，𝑜𝑖从𝑏𝑖中复制数据。

- 当参数 a=b=None 时，即 a 和 b 参数不指定，tf.where 会返回 cond 张量中所有 True 的元素的索引坐标
- 通过一系列的比较、索引号收集和掩码收集的操作组合是有很大的实际应用的

#### 5.6.5 scatter_nd

张量白板刷新，有目的性刷新

通过 tf.scatter_nd(indices, updates, shape)函数可以高效地刷新张量的部分数据，

但是这个函数只能在全 0 的白板张量上面执行刷新操作，

因此可能需要结合其它操作来实现现有张量的数据刷新功能。

直接用scatter_nd是从全0白板更新，如何从已有的数据上更新？

1. 假设A是待更新，从A中将待更新的部分值取出，用scatter_nd生成A'
2. 拿A=A-A'清除待更新的部分值（clear）
3. 新的值通过scatter_nd生成A'',则A=A+A''可进行部分更新

#### 5.6.6 meshgrid

- 通过 tf.meshgrid 函数可以方便地生成二维网格的采样点坐标，方便可视化等应用场合。

  ```python
  x = [1, 2, 3]
  y = [4, 5, 6]
  X, Y = tf.meshgrid(x, y)
  # X = [[1, 2, 3],
  #      [1, 2, 3],
  #      [1, 2, 3]]
  # Y = [[4, 4, 4],
  #      [5, 5, 5],
  #      [6, 6, 6]]
  ```

- 通过 tf.stack([x,y],axis=2) 可以将x，y还原成对应的坐标

stack的操作：当axis ≥ 0时，在axis 之前插入；当axis < 0时，在 axis 之后插入新维度。

### 5.7 经典数据集加载

keras.datasets 模块提供了常用经典数据集的自动下载、管理、加载与转换功能， 并且提供了 tf.data.Dataset 数据集对象

- 通过 datasets.xxx.load_data()函数即可实现经典数据集的自动加载，

其中 xxx 代表具体 的数据集名称，如“CIFAR10”、“MNIST”。

TensorFlow 会默认将数据缓存在用户目录下 的.keras/datasets 文件夹

- 通过 load_data()函数会返回相应格式的数据

- 通过 Dataset.from_tensor_slices 可以将训练部分的数据图片 x 和标签 y 都转换成 Dataset 对象(将numpy数据转换为dataset)

#### 5.7.1 随机打散

通过 Dataset.shuffle(buffer_size)工具可以设置 Dataset 对象随机打散数据之间的顺序，

防止每次训练时数据按固定顺序产生，从而使得模型尝试“记忆”住标签信息

其中，buffer_size 参数指定缓冲池的大小，一般设置为一个较大的常数即可。调用 Dataset

提供的这些工具函数会返回新的 Dataset 对象

#### 5.7.2 批训练

.batch,一般在网络的计算过程中会同时计算多个样本，我们 把这种训练方式叫做批训练，

其中一个批中样本的数量叫做 Batch Size。

为了一次能够从 Dataset 中产生 Batch Size 数量的样本，需要设置 Dataset 为批训练方式

```python
# 设置批训练,batch size 为 128
train_db = train_db.batch(128) 
```

其中 128 为 Batch Size 参数，即一次并行计算 128 个样本的数据

#### 5.7.3 预处理

Dataset 对象通过提供 map(func)工具函数，

可以非常方便地调用用户自定义的预处理逻辑，它实现在 func 函数里

例如，下方代码调用名为 preprocess 的函数完成每个样本的预处理：

```python
# 预处理函数实现在 preprocess 函数中，传入函数名即可
train_db = train_db.map(preprocess)


# 自定义的预处理函数
def preprocess(x, y):
    # 预处理函数里面进行
    pass
```

#### 5.7.4 循环训练

对于 Dataset 对象，在使用时可以通过

```python
# 迭代数据集对象，带 step 参数
for step, (x, y) in enumerate(train_db):
# 或迭代数据集对象
for x, y in train_db: 
```

方式进行迭代，每次返回的 x 和 y 对象即为批量样本和标签。 当对 train_db 的所有样本完成一次迭代后，for 循环终止退出。

- 完成一个 Batch 的数据训练，叫做一个 Step；
- 通过多个 step 来完成整个训练集的一次迭代，叫做一个 Epoch。
- 1 epoch = 1代 = 遍历整个数据集一次
- 1 Step 是每次的梯度下降即完成1个Batch

此外，也可以通过设置 Dataset 对象，使得数据集对象内部遍历多次才会退出，实现如下:

```python
# 数据集迭代 20 遍才终止
train_db = train_db.repeat(20) 
```

### 5.8 MNIST 测试实战

前面已经介绍并实现了前向传播和数据集的加载部分。现在我们来完成剩下的分类任 务逻辑。

1. 在训练的过程中，通过间隔数个 Step 后打印误差数据，可以有效监督模型的训练进度
2. 在若干个 Step 或者若干个 Epoch 训练后，可以进行一次测试(验证)，以获得模型的当前性能

现在我们来利用学习到的 TensorFlow 张量操作函数，完成准确度的计算实战

1. 先考虑一个 Batch 的样本 x，通过前向计算可以获得网络的预测值。预测值 out 的 shape 为[𝑏, 10]，分别代表了样本属于每个类别的概率
2. 我们根据 tf.argmax 函数选出概率最大值出现的索引号，也即样本最有可能的类别号
3. 由于我们的标注 y 已经在预处理中完成了 one-hot 编码，这在测试时其实是不需要的，因此通过 tf.argmax 可以得到数字编码的标注 y
4. 通过 tf.equal 可以比较这两者的结果是否相等
5. 并求和比较结果中所有 True(转换为 1)的数量，即为预测正确的数量
6. 预测正确的数量除以总测试数量即可得到准确度，并打印出来

## 第6章 神经网络

#### 6.2 全连接层

6.2.1 张量方式实现

在 TensorFlow 中，要实现全连接层，只需要定义好权值张量 𝑾 和偏置张量 𝒃，

并利用 TensorFlow 提供的批量矩阵相乘函数 tf.matmul()即可完成网络层的计算。

> @ 是矩阵乘法，\*是对应元素相乘

6.2.2 层方式实现

TensorFlow 中有更高层、使用更方便的层实现方式：

`layers.Dense(units, activation)。`

通过 layer.Dense 类，只需要指定输出节点数 Units 和激活函数类型 activation 即可。

- 可以通过类内部的成员名 kernel 和 bias 来获取权值张量 𝑾 和偏置张量 𝒃 对象
- 在优化参数时，需要获得网络的所有待优化的张量参数列表，可以通过类的 trainable_variables 来返回待优化参数列表
- 还有部分层包含了不参与梯度优化的张量，如后续介绍的 Batch Normalization 层，可以通过
  non_trainable_variables 成员返回所有不需要优化的参数列表。
  如果希望获得所有参数列表，可以通过类的 variables 返回所有内部张量列表
- 对于全连接层，内部张量都参与梯度优化，故 variables 返回的列表与 trainable_variables 相同。
- 利用网络层类对象进行前向计算时，只需要调用类的**call**方法即可，
  即写成 fc(x)方式便可，它会自动调用类的**call**方法，在**call**方法中会自动调用 call 方法

#### 6.3 神经网络

###### 6.3.1 张量方式实现

对于多层神经网络，以图 6.5 网络结构为例，需要分别定义各层的权值矩阵 𝑾 和偏置向量 𝒃。

有多少个全连接层，则需要相应地定义数量相当的 𝑾 和 𝒃，

并且每层的参数只能用于对应的层，不能混淆使用。

- 在计算时，只需要按照网络层的顺序，将上一层的输出作为当前层的输入即可，重复直至最后一层，并将输出层的输出作为网络的输出
- 最后一层是否需要添加激活函数通常视具体的任务而定，这里加不加都可以

在使用 TensorFlow 自动求导功能计算梯度时，

需要将前向计算过程放置在 tf.GradientTape()环境中，

从而利用 GradientTape 对象的 gradient()方法自动求解参数的梯度，

并利用 optimizers 对象更新参数。

###### 6.3.2 层方式实现

对于常规的网络层，通过层方式实现起来更加简洁高效。

1. 首先新建各个网络层类，并指定各层的激活函数类型
2. 在前向计算时，依序通过各个网络层即可
3. 对于这种数据依次向前传播的网络，也可以通过 Sequential 容器封装成一个网络大类对象，调用大类的前向计算函数一次即可完成所有层的前向计算，使用起来更加方便
4. 前向计算时只需要调用一次网络大类对象，即可完成所有层的按序计算

#### 6.4 激活函数

- 可以通过 tf.nn.sigmoid 实现 Sigmoid 函数
- 可以通过 tf.nn.relu 实现 ReLU 函数
- LeakyReLU 函数=𝑝𝑥,𝑥 < 0,可以通过 tf.nn.leaky_relu 实现 LeakyReLU 函数,其中 alpha 参数代表 𝑝
- 可以通过 tf.nn.tanh 实现 tanh 函数

#### 6.5 输出层设计

###### 6.5.3 [0,1]区间，和为 1

- 在 TensorFlow 中，可以通过 tf.nn.softmax 实现 Softmax 函数
- TensorFlow 中提供了一个统一的接口，将 Softmax 与交叉熵损失函数同时实现，同时也处理了数值不稳定的异常
- 函数式接口为 tf.keras.losses.categorical_crossentropy(y_true, y_pred, from_logits=False)
- 为了数值计算稳定性，一般设置 from_logits 为 True，此时 tf.keras.losses.categorical_crossentropy 将在内部进行 Softmax 函数计算，所以不需要在模型中显式调用 Softmax 函数
- 除了函数式接口，也可以利用 losses.CategoricalCrossentropy(from_logits)类方式同时实现 Softmax 与交叉熵损失函数的计算，from_logits 参数的设置方式相同。

###### 6.5.4 [-1, 1]

如果希望输出值的范围分布在(−1,1)区间，可以简单地使用 tanh 激活函数

#### 6.6 误差计算

###### 6.6.1 均方差误差函数

- 均方差(Mean Squared Error，简称 MSE)误差函数把输出向量和真实向量映射到笛卡尔坐标系的两个点上，通过计算这两个点之间的欧式距离(准确地说是欧式距离的平方)来衡量两个向量之间的差距
- MSE 误差函数的值总是大于等于 0，当 MSE 函数达到最小值 0 时，输出等于真实标签，此时神经网络的参数达到最优状态
- 在 TensorFlow 中，可以通过函数方式或层方式实现 MSE 误差计算
- 特别要注意的是，MSE 函数返回的是每个样本的均方差，需要在样本维度上再次平均来获
  得平均样本的均方差
- 也可以通过层方式实现，对应的类为 keras.losses.MeanSquaredError()，和其他层的类一
  样

#### 6.8 汽车油耗预测实战

本节我们将利用全连接网络模型来完成汽车的效能指标 MPG(Mile Per Gallon，每加仑燃油英里数)的预测问题实战

###### 6.8.1 数据集

- 采用 Auto MPG 数据集，它记录了各种汽车效能指标与气缸数、重量、马力等其它因子的真实数据
- Auto MPG 数据集一共记录了 398 项数据，我们从 UCI 服务器下载并读取数据集到
  DataFrame 对象中
- 原始表格中的数据可能含有空字段(缺失值)的数据项，需要清除这些记录项
- 由于 Origin 字段为类别类型数据，我们将其移除，并转换为新的 3 个字段：USA、Europe 和 Japan，分别代表是否来自此产地
- 按着 8:2 的比例切分数据集为训练集和测试集
- 将 MPG 字段移出为标签数据
- 统计训练集的各个字段数值的均值和标准差，并完成数据的标准化，通过 norm()函数实现
- 打印出训练集和测试集的大小
- 利用切分的训练集数据构建数据集对象
- 我们可以通过简单地统计数据集中各字段之间的两两分布来观察各个字段对 MPG 的影响

###### 6.8.2 创建网络

1. 考虑到 Auto MPG 数据集规模较小
1. 我们只创建一个 3 层的全连接网络来完成 MPG值的预测任务。
1. 输入𝑿的特征共有 9 种，因此第一层的输入节点数为 9。
1. 第一层、第二层的输出节点数设计为64和64，
1. 由于只有一种预测值，输出层输出节点设计为 1。

**步骤**

1. 我们将网络实现为一个自定义网络类
1. 只需要在初始化函数中创建各个子网络层，
1. 并在前向计算函数 call 中实现自定义网络类的计算逻辑即可。
1. 自定义网络类继承自keras.Model 基类，这也是自定义网络类的标准写法，以方便地利用 keras.Model 基类提供
的 trainable_variables、save_weights 等各种便捷功能。

###### 6.8.3 训练与测试

1. 在完成主网络模型类的创建后，我们来实例化网络对象和创建优化器
1. 接下来实现网络训练部分。通过 Epoch 和 Step 组成的双层循环训练网络，共训练200个Epoch
1. 程序运算时记录每个 Epoch 结束时的训练和测试 MAE 数据，并绘制变化曲线

## 第7章 反向传播算法

#### 7.3 激活函数导数

实现部分全部使用 Numpy 演示

- Sigmoid 函数导数
- ReLU 函数导数:既不会放大梯度，造成梯度爆炸(Gradient exploding)现象；也不会缩小梯度，造成梯度弥散(Gradient vanishing)现象
- LeakyReLU 函数导数:p 一般设置为某较小的数值，如 0.01 或 0.02
- Tanh 函数梯度

#### 7.6 链式法则

简单使用 TensorFlow 自动求导功能，来体验链式法则的魅力

#### 7.8 Himmelblau 函数优化实战

- Himmelblau 函数是用来测试优化算法的常用样例函数之一，它包含了两个自变量𝑥和𝑦

1. 首先我们通过如下代码实现 Himmelblau 函数的表达式
1. 然后完成 Himmelblau 函数的可视化操作。通过 np.meshgrid 函数(TensorFlow 中也有
meshgrid 函数)生成二维平面网格点坐标
1. 并利用 Matplotlib 库可视化 Himmelblau 函数
1. Himmelblau 函数的等高线图，大致可以看出，它共有 4 个局部极小值点，并且局部极小值都是 0，所以这 4 个局部极小值也是全局最小值
1. 利用 TensorFlow 自动求导来求出函数在𝑥和𝑦的偏导数，并循环迭代更新𝑥和𝑦值

实际上，通过改变网络参数的初始化状态，程序可以得到多种极小值数值解。

参数的初始化状态是可能影响梯度下降算法的搜索轨迹的，甚至有可能搜索出完全不同的数值解

#### 7.9 反向传播算法实战

- 我们将实现一个 4 层的全连接网络，来完成二分类任务。
- 网络输入节点数为 2，隐藏层的节点数设计为：25、50和25
- 输出层两个节点，分别表示属于类别 1 的概率和类别 2的概率
- 直接利用均方误差函数计算与 One-hot 编码的真实标签之间的误差
- 所有的网络激活函数全部采用 Sigmoid 函数

###### 7.9.1 数据集

- 这里通过 scikit-learn 库提供的便捷工具生成 2000 个线性不可分的 2 分类数据集数据的特征长度为 2
- 所有的红色点为一类，所有的蓝色点为一类
- 可以看到每个类别数据的分布呈月牙状，并且是是线性不可分的，无法用线性网络获得较好效果。
- 我们按着7: 3比例切分训练集和测试集，其中2000 ∙ 0 3 = 600个样本点用于测试，不参与训练，剩下的 1400 个点用于网络的训练

1. 数据集的采集直接使用 scikit-learn 提供的 make_moons 函数生成，设置采样点数和切割比率
2. 可以通过如下可视化代码绘制数据集的分布

###### 7.9.2 网络层

1. 通过新建类 Layer 实现一个网络层

- 通过新建类 Layer 实现一个网络层，需要传入网络层的输入节点数、输出节点数、激活函数类型等参数，
- 权值 weights 和偏置张量 bias 在初始化时根据输入、输出节点数自动生成并初始化。

2. 网络层的前向传播函数实现如下，其中 last_activation 变量用于保存当前层的输出值
3. 上述代码中的 self._apply_activation 函数实现了不同类型的激活函数的前向计算过程，尽管此处我们只使用 Sigmoid 激活函数一种
4. 针对于不同类型的激活函数，它们的导数计算实现如下
5. 可以看到，Sigmoid 函数的导数实现为𝑟 (1 − 𝑟)，其中𝑟即为𝜎(𝑧)

###### 7.9.3 网络模型

1. 创建单层网络类后，我们实现网络模型的 NeuralNetwork 类

- 它内部维护各层的网络层 Layer 类对象
- 可以通过 add_layer 函数追加网络层，实现创建不同结构的网络模型目的

2. 网络的前向传播只需要循环调各个网络层对象的前向计算函数即可
3. 根据网络结构配置，利用 NeuralNetwork 类创建网络对象，并添加 4 层全连接层
4. 网络模型的反向传播实现稍复杂，需要从最末层开始，计算每层的𝛿变量，然后根据推导出的梯度公式，将计算出的𝛿变量存储在 Layer 类的 delta 变量中
5. 在反向计算完每层的𝛿变量后，只需要按着𝜕ℒ/𝜕𝑤𝑖 = 𝑜𝑖𝛿j公式计算每层参数的梯度并更新网络参数即可

- 由于代码中的 delta 计算的其实是−𝛿，因此更新时使用了加号

6. 因此，在 backpropagation 函数中，反向计算每层的𝛿变量，并根据梯度公式计算每层参数的梯度值，按着梯度下降算法完成一次参数的更新。

###### 7.9.4 网络训练

1. 这里的二分类任务网络设计为两个输出节点，因此需要将真实标签𝑦进行 One-hot 编码
2. 将 One-hot 编码后的真实标签与网络的输出计算均方误差并调用反向传播函数更新网络参数

- 循环迭代训练集 1000 遍即可
