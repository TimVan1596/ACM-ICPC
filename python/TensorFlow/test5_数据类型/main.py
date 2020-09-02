# -*- coding:utf-8 -*-
# @Time:2020/9/1 23:18
# @Author:TimVan
# @File:main.py
# @Software:PyCharm
import tensorflow as tf

if __name__ == "__main__":
    # a = tf.constant(1)
    # print(a)
    # a = tf.constant(1.)
    # print(a)
    #
    # # TypeError
    # # a = tf.constant(1., dtype=tf.int32)
    # # print(a)
    #
    # a = tf.constant([True, False])
    # print(a)

    with tf.device("cpu"):
        a = tf.constant([3])
    with tf.device("gpu"):
        b = tf.constant(True)

    print(a)
    print(b)