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




### 4.6 索引与切片
##### 4.6.1 索引
##### 4.6.2 切片  
通过start: end: step切片方式,end 为结束读取位置的索引(不包含 end 位)
##### 4.6.3 选择索引
- tf.gather(params,indices,axis=0)
从params的axis维根据indices的参数值获取切片
- tf.gather_nd( params, indices, name=None)
按照indices的格式从params中抽取切片（合并为一个Tensor）
indices是一个K维整数Tensor，
- tf.boolean_mask(tensor, mask, name="boolean_mask", axis=None)
tf.boolean_mask 的作用是通过布尔值过滤元素

### 4.7 维度变换
##### 4.7.1 改变视图  
改变 x 的视图，存储并未改变
##### 4.7.2 增、删维度
- tf.expand_dims(x, axis)  
通过 tf.expand_dims(x, axis)可在指定的 axis 轴前可以插入一个新的维度  
需要注意的是，tf.expand_dims 的 axis 为正时，表示在当前维度之前插入一个新维度；为
负时，表示当前维度之后插入一个新的维度。 
- tf.squeeze(x, axis)  
删除维度 是增加维度的逆操作，与增加维度一样，删除维度只能删除长度为 1 的维
度，也不会改变张量的存储。如果希望将
图片数量维度删除，可以通过 tf.squeeze(x, axis)函数，axis 参数为待删除的维度的索引号
##### 4.7.3 交换维度  
使用 tf.transpose(x, perm)函数完成维度交换操作，其中参数 perm 表示新维度的顺序 List
##### 4.7.4 复制数据
当通过增加维度操作插入新维度后，可能希望在新的维度上面复制若干份数据。  
可以通过 tf.tile(x, multiples)函数完成数据在指定维度上的复制操作，multiples 分别指
定了每个维度上面的复制倍数，对应位置为 1 表明不复制，为 2 表明新长度为原来长度的
2 倍，即数据复制一份，以此类推。

### 4.8 Broadcasting
Broadcasting 称为广播机制(或自动扩展机制)，它是一种轻量级的张量复制手段，  
在逻辑上扩展张量数据的形状，但是只会在需要时才会执行实际存储复制操作。  
- 靠右对齐，先考虑小维度再拓展至大维度
1. 如果当前维度为1，拓展至相同
2. 如果没有维度，插入新维度再拓展至相同
3. 否则不支持广播  
  
通过 tf.broadcast_to(x, new_shape)函数可以显式地执行自动扩展功能