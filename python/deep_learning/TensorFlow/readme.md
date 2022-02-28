## TensorFlow深度学习

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