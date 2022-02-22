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