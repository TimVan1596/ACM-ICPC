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

[𝑏, ℎ, , 𝑐]其中𝑏表示输入样本的数量，ℎ/ 分别表示特征图的高/宽，𝑐表示特征图的通道数

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
1. 排序sort,argsort:求排序和索引
2. 前k大值 Top_k,res=tf.math.top_k(a,2)
3. Top Acc:前N个中有没有命中的准确率
4. tf.unique() 返回去除重复的与索硬化
