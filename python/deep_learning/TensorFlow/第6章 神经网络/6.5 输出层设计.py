import tensorflow as tf


if __name__ == "__main__":
    # #### 6.5 输出层设计

    # ###### 6.5.3 [0,1]区间，和为 1
    # - 在 TensorFlow 中，可以通过 tf.nn.softmax 实现 Softmax 函数
    z = tf.constant([2.0, 1.0, 0.1])
    # tf.Tensor([0.6590012  0.24243298 0.09856589], shape=(3,), dtype=float32)
    print(tf.nn.softmax(z))

    # - TensorFlow 中提供了一个统一的接口，将 Softmax 与交叉熵损失函数同时实现，同时也处理了数值不稳定的异常
    # 构造输出层的输出
    z = tf.random.normal([2, 10])
    # 构造真实值
    y_onehot = tf.constant([1, 3])
    # one-hot 编码
    y_onehot = tf.one_hot(y_onehot, depth=10)
    # y_onehot = shape=(2, 10)
    print(y_onehot)
    # - 函数式接口为tf.keras.losses.categorical_crossentropy(y_true, y_pred, from_logits=False)
    # - 为了数值计算稳定性，一般设置 from_logits 为 True，此时tf.keras.losses.categorical_crossentropy将在内部进行 Softmax 函数计算，所以不需要在模型中显式调用 Softmax 函数

    # 输出层未使用 Softmax 函数，故 from_logits 设置为 True
    # 这样 categorical_crossentropy 函数在计算损失函数前，会先内部调用 Softmax 函数
    loss = tf.keras.losses.categorical_crossentropy(y_onehot, z, from_logits=True)
    # loss = shape=(2, )
    print(loss)
    loss = tf.reduce_mean(loss)
    print(loss)

    # - 除了函数式接口，也可以利用 losses.CategoricalCrossentropy(from_logits)类方式同时实现 Softmax 与交叉熵损失函数的计算，from_logits 参数的设置方式相同。
    # 创建 Softmax 与交叉熵计算类，输出层的输出 z 未使用 softmax
    criterion = tf.keras.losses.CategoricalCrossentropy(from_logits=True)
    loss = criterion(y_onehot, z)
    print(loss)

    # ###### 6.5.4 [-1, 1]
    # 如果希望输出值的范围分布在(−1,1)区间，可以简单地使用 tanh 激活函数
    x = tf.linspace(-6, 6, 13)
    print(tf.tanh(x))
    pass
