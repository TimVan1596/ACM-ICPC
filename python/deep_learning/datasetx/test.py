import h5py
import numpy as np
from matplotlib import pyplot as plt

# # 同序shuffle-按相同顺序打乱两个数组
# def same_shuffle(arr1: list, arr2: list):
#     rand_state = np.random.get_state()
#     np.random.shuffle(arr1)
#     np.random.set_state(rand_state)
#     np.random.shuffle(arr2)
#     return arr1, arr2

import os
from urllib.parse import urlparse


# 根据url获取文件名和后缀
# 返回 （文件名,后缀）
def get_url_file_info(url):
    file_name = os.path.basename(urlparse(url).path)
    return os.path.splitext(file_name)


if __name__ == '__main__':
    url = 'https://img95.699pic.com/photo/50071/9458.jpeg_wh300.jpg'
    get_url_file_info(url)
