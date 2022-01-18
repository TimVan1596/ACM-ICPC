# -*- coding:utf-8 -*-
# @Time:2020/8/18 2:11
# @Author:TimVan
# @File:gen_dataset.py
# @Software:PyCharm

import os

import tensorflow as tf

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"

if __name__ == "__main__":
    y = tf.constant([0, 1, 2, 3])
    y = tf.one_hot(y, depth=10)
    print(y)
