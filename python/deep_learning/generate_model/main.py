# -*- coding:utf-8 -*-
# @Time:2021-11-5 20:52:32
# @Author:TimVan
# @File:main.py
# @Software:PyCharm

# 图片缩放为 64*64
PIC_SIZE = 64

import os
from PIL import Image
import matplotlib.pyplot as plt
import h5py

'''
    # 1.读取当前目录下的train/test文件夹
    # 2.分别读取对应文件夹下的文件夹(标签)
    # 3.对应标签生成对应的数据
    # 4.对应的数据应该是格式化的，如(224,224,3)，打乱的
    # 5.博客总结，可视化预期,readme介绍
    # 指出输入的格式和输出的格式，告诉hdpy是什么

    # 未来：自动分配train/test的比重，指定的path，path自动转换，放到线上
'''


# 主驱动
def gen_from_pictures(path):
    # 读取data文件夹下的内容
    folders = os.listdir(path)
    path = path + '/data'
    train_path = path + '/train'
    test_path = path + '/test'

    # 处理训练集
    train_folder_list = os.listdir(train_path)
    train_file = h5py.File('train.h5', 'w')
    # train_file.create_array('list_classes')
    train_list = []
    # 进入标签
    for train_folder in train_folder_list:
        # train_file['list_classes'].append(str(train_folder))
        train_folder_path = train_path + '/' + train_folder
        train_folder_pict_list = os.listdir(train_folder_path)
        # 进入具体的图片
        for train_folder_pic in train_folder_pict_list:
            # 缩放为相同大小
            im = Image.open(train_folder_path + '/' + train_folder_pic)
            re_im = im.resize((PIC_SIZE, PIC_SIZE))  # 宽*高

            train_list.append((re_im, train_folder))

            # plt.imshow(re_im)
            # plt.show()
    print(train_list, sep='-- \n')

    pass


if __name__ == '__main__':
    path = 'C:/Users/TimVan/Desktop/XM/ACM/python/deep_learning/generate_model'
    gen_from_pictures(path)
