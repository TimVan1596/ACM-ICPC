# -*- coding:utf-8 -*-
# @Time:2020/8/18 2:11
# @Author:TimVan
# @File:gen_dataset.py
# @Software:PyCharm

import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "1"
import numpy as np
import tensorflow as tf

if __name__ == "__main__":
    a = tf.random.uniform(shape=[3, 3], maxval=10, dtype=tf.int32)
    print(a)

    print(tf.sort(a))
    print(tf.sort(a, direction="DESCENDING"))

    idx = tf.argsort(a)
    print(idx)
