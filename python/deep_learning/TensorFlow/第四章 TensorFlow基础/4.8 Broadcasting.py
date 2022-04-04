import os

os.environ['TF_CPP_MIN_LEVEL_LOG'] = '1'
import tensorflow as tf

if __name__ == '__main__':
    ### 4.8 Broadcasting
    # Broadcasting称为广播机制(或自动扩展机制)，它是一种轻量级的张量复制手段，
    # 在逻辑上扩展张量数据的形状，但是只会在需要时才会执行实际存储复制操作。
    # - 靠右对齐，先考虑小维度再拓展至大维度
    # 1.如果当前维度为1，拓展至相同
    # 2.如果没有维度，插入新维度再拓展至相同
    # 3.否则不支持广播
    A = tf.random.normal([32, 32, 1])
    A = tf.broadcast_to(A, [4, 32, 32, 3])
    print(A.shape)
    # 通过tf.broadcast_to(x, new_shape)函数可以显式地执行自动扩展功能
    # A的最低为度长度为2，不具备普适性
    A = tf.random.normal([32, 32, 2])
    A = tf.broadcast_to(A, [4, 32, 32, 3])
    print(A.shape)
