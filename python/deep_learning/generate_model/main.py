# -*- coding:utf-8 -*-
# @Time:2021-11-5 20:52:32
# @Author:TimVan
# @File:main.py
# @Software:PyCharm

# 图片缩放为 64*64
import numpy as np

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

    # 未来：自动分配train/test的比重，指定的path，path自动转换，放到线上，每一步的文字提示
'''


# 主驱动
def gen_from_pictures(path, label_dict):
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
    train_label_list = []
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
            train_label_list.append(label_dict.get(train_folder))
            train_list.append(np.array(re_im))

            # plt.imshow(re_im)
            # plt.show()
    train_file.create_dataset('train_x', data=train_list)
    train_file.create_dataset('train_y', data=train_label_list)
    train_file.close()

    # 处理训练集
    test_folder_list = os.listdir(test_path)
    test_file = h5py.File('test.h5', 'w')
    # test_file.create_array('list_classes')
    test_list = []
    test_label_list = []
    # 进入标签
    for test_folder in test_folder_list:
        # test_file['list_classes'].append(str(test_folder))
        test_folder_path = test_path + '/' + test_folder
        test_folder_pict_list = os.listdir(test_folder_path)
        # 进入具体的图片
        for test_folder_pic in test_folder_pict_list:
            # 缩放为相同大小
            im = Image.open(test_folder_path + '/' + test_folder_pic)
            re_im = im.resize((PIC_SIZE, PIC_SIZE))  # 宽*高
            test_label_list.append(label_dict.get(test_folder))
            test_list.append(np.array(re_im))

            # plt.imshow(re_im)
            # plt.show()
    test_file.create_dataset('test_x', data=test_list)
    test_file.create_dataset('test_y', data=test_label_list)
    test_file.close()


if __name__ == '__main__':
    # 标签字典
    label_dict = {
        'yes': 1,
        'no': 0
    }

    path = 'C:/auto_file.py'
    gen_from_pictures(path, label_dict)
