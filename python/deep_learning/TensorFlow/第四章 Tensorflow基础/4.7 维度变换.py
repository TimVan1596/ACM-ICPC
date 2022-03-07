import os

os.environ['TF_CPP_MIN_LEVEL_LOG'] = '1'
import tensorflow as tf

if __name__ == '__main__':
    ### 4.7 维度变换
    ##### 4.7.1 改变视图
    # 其中的参数−1; 表示当前轴上长度需要根据张量总元素不变的法则自动推导
    # x = tf.reshape(tf.linspace(0, 14, 15), [3, -1])
    # print(x)

    ##### 4.7.2 增、删维度
    # - tf.expand_dims(x, axis)
    # 通过tf.expand_dims(x, axis)可在指定的axis轴前可以插入一个新的维度需要注意的是，
    # tf.expand_dims的axis为正时，表示在当前维度之前插入一个新维度；
    # 为负时，表示当前维度之后插入一个新的维度。
    # x = tf.reshape(tf.linspace(0, 19, 20), [2, 2, 5])
    # x = tf.expand_dims(x, axis=0)
    # print(x.shape)
    # x = tf.expand_dims(x, axis=-2)
    # print(x.shape)
    # - tf.squeeze(x, axis)
    # 删除维度是增加维度的逆操作，与增加维度一样，删除维度只能删除长度为1的维度，也不会改变张量的存储。
    # 如果希望将图片数量维度删除，可以通过tf.squeeze(x, axis)函数，axis参数为待删除的维度的索引号
    # x = tf.squeeze(x, axis=-2)
    # print(x.shape)
    ##### 4.7.3 交换维度
    # 使用; tf.transpose(x, perm)函数完成维度交换操作，其中参数perm表示新维度的顺序List
    # x = tf.random.normal([2, 32, 32, 3])
    # tf.transpose(x, perm=[0, 3, 1, 2])
    # print(x)
    ##### 4.7.4 复制数据
    # 当通过增加维度操作插入新维度后，可能希望在新的维度上面复制若干份数据。
    # 可以通过tf.tile(x, multiples)函数完成数据在指定维度上的复制操作，
    # multiples分别指定了每个维度上面的复制倍数，对应位置为1表明不复制，
    # 为2表明新长度为原来长度的2倍，即数据复制一份，以此类推。
    x = tf.reshape(tf.range(0, 10, 1), [2, -1])
    print(x.shape)
    print(x)
    x = tf.tile(x, multiples=[2, 2])
    print(x.shape)
    print(x)
