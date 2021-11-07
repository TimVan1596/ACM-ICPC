# -*- coding:utf-8 -*-
# @Time:2021-11-5 20:52:32
# @Author:TimVan
# @File:gen_dataset.py
# @Software:PyCharm

# 图片缩放为 64*64
import numpy as np
import random
import os
from PIL import Image
import h5py
import logging

'''
    # 1.读取当前目录下的train/test文件夹
    # 2.分别读取对应文件夹下的文件夹(标签)
    # 3.对应标签生成对应的数据
    # 4.对应的数据应该是格式化的，如(224,224,3)，打乱的
    # 5.博客总结，可视化预期,readme介绍
    # 指出输入的格式和输出的格式，告诉hdpy是什么

    # 未来：自动分配train/test的比重，指定的path，path自动转换，放到线上，每一步的文字提示
    # 运行环境为windows
    # 假如样本小于10,0.9的问题
    # 应该包含classes信息
'''


# 主驱动
# 通过jpg图片，生成train.h5dy和test.h5dy格式的数据集
# path = 数据集的目录
# label_dict = 标签和值对应的字典，如{'yes':1,'no;:0}
# train_percent = 训练集占总样本的比例，默认为0.9
# pic_size = 生成数据集中缩放图片的尺寸，默认为224*224
# isLog = 是否需要日志
def gen_from_pictures(path, label_dict, train_percent=0.9, pic_size=224, isLog=False):
    if isLog:
        init_logging()

    logging.info('datasetX 开始转换')
    logging.debug('--path=' + path)
    logging.debug('--label_dict=' + str(label_dict))
    logging.debug('--train_percent=' + str(train_percent))
    logging.debug('--pic_size=' + str(pic_size))

    # pic_cnt = 图片的个数
    pic_cnt = 0
    data_path = path + '/data'

    label_list = os.listdir(data_path)
    # data_list = 元素是(图片元素,标签数字)元组的数组
    data_list = []
    for label in label_list:
        label_path = data_path + '/' + label
        pic_list = os.listdir(label_path)
        # 累加图片的个数
        pic_cnt = pic_cnt + len(pic_list)
        # 进入具体的图片
        for pic in pic_list:
            # 缩放
            image = Image.open(label_path + '/' + pic)
            re_image = image.resize((pic_size, pic_size))
            # 新增一个(图片元素,标签数字)元组
            data_list.append((np.array(re_image), label_dict.get(label)))
            logging.debug('--正在处理第' + str(len(data_list)) + '个文件')

    # 检验两者是否相等
    assert len(data_list) == pic_cnt

    random.shuffle(data_list)
    train_cnt = int(train_percent * pic_cnt)
    train_list = data_list[0:train_cnt]
    test_list = data_list[train_cnt:]

    assert len(train_list) + len(test_list) == pic_cnt
    logging.info('共有文件' + str(pic_cnt) + '个文件'
                 + ',其中训练集有' + str(len(train_list)) + '个'
                 + ',测试集集有' + str(len(test_list)) + '个')

    train_file_path = gen_h5(train_list, path, file_name='train')
    test_file_path = gen_h5(test_list, path, file_name='test')
    logging.info('训练集保存在' + train_file_path)
    logging.info('测试集保存在' + test_file_path)


# 同序shuffle-按相同顺序打乱两个数组
def same_shuffle(arr1: list, arr2: list):
    rand_state = np.random.get_state()
    np.random.shuffle(arr1)
    np.random.set_state(rand_state)
    np.random.shuffle(arr2)
    return arr1, arr2


# 通过x,y生成h5文件
# data_list = 元素是(图片元素,标签数字)元组的数组
def gen_h5(data_list, file_path, file_name='file'):
    x = []
    y = []
    # 从(图片元素,标签数字)取出两列成数组
    for elem in data_list:
        x.append(elem[0])
        y.append(elem[1])
    path = file_path + '/output/'
    # 判断文件夹是否存在，不存在则创建
    if not os.path.exists(path):
        os.mkdir(path)
    file = h5py.File(path + file_name + '.h5', 'w')
    file.create_dataset('x', data=x)
    file.create_dataset('y', data=y)
    file.close()
    return path


# 初始化日志logging
def init_logging():
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"  # 日志格式化输出
    DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"  # 日期格式
    fp = logging.FileHandler('log.txt', encoding='utf-8')
    fs = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])  # 调用


if __name__ == '__main__':
    # 标签字典
    label_dict = {
        'yes': 1,
        'no': 0
    }

    # 训练集占的比例
    train_percent = 0.85
    # 图片缩放的尺寸
    pic_size = 168

    path = './'
    gen_from_pictures(path, label_dict, train_percent, pic_size=pic_size, isLog=True)
