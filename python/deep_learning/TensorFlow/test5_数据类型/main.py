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

    with tf.device("/cpu:0"):
        a = tf.constant([3])
    with tf.device("/gpu:0"):
        b = tf.range(4)

    print(a.device)
    print(b.device)
    aa = a.gpu()
    bb = b.cpu()
    print(aa.device)
    print(bb.device)

    # tensor 转 numpy
    print(b.numpy())
