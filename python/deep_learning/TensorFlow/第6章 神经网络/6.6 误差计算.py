import tensorflow as tf

if __name__ == "__main__":
    # #### 6.6 误差计算
    ###### 6.6.1 均方差误差函数

    # - 均方差(Mean Squared Error，简称 MSE)误差函数把输出向量和真实向量映射到笛卡尔坐标系的两个点上，
    # 通过计算这两个点之间的欧式距离(准确地说是欧式距离的平方)来衡量两个向量之间的差距

    # - MSE 误差函数的值总是大于等于 0，当 MSE 函数达到最小值 0 时，输出等于真实标签，
    # 此时神经网络的参数达到最优状态

    # - 在 TensorFlow 中，可以通过函数方式或层方式实现 MSE 误差计算
    # 构造网络输出
    out = tf.random.uniform(shape=[2], minval=0, maxval=10, dtype=tf.int32)
    y_pred = tf.one_hot(out, depth=10)
    # 构造真实值
    y_true = tf.one_hot([2, 5], depth=10)
    # 计算均方差
    loss = tf.keras.losses.MSE(y_true, y_pred)
    print(y_pred)
    print(y_true)
    # 计算 batch 均方差
    # - 特别要注意的是，MSE 函数返回的是每个样本的均方差，需要在样本维度上再次平均来获
    loss = tf.reduce_mean(loss)
    print(loss)

    # 得平均样本的均方差
    # - 也可以通过层方式实现，对应的类为 keras.losses.MeanSquaredError()，和其他层的类一样

    criterion = tf.keras.losses.MeanSquaredError()
    loss = criterion(y_true, y_pred)
    print(loss)

    pass
