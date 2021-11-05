#### 笔记
index = 1
##### 1.tf.constant()
    即tensor类型，并非常量，可用tf.constant(2.)来定义float32类型
##### 2.tf.is_tensor()和isinstance()
    判断是否是tensor类型，推荐使用tf.is_tensor()
##### 3.tf.cast(tensor,dtype=)
    将tensor类型转换为其他类型，如dtype=float32或tf.bool等
##### 4.tf.variable(tensor).trainable
    将tensor转为variable类型，即可训练，可求导，可自动记录梯度信息