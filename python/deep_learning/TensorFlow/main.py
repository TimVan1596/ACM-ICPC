# -*- coding:utf-8 -*-
# @Time:2020/8/18 2:11
# @Author:TimVan
# @File:gen_dataset.py
# @Software:PyCharm

import os

import numpy as np

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "99"

if __name__ == "__main__":
    arr = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    arr = np.array(arr)
    print(arr[:, 1::])
