import os
import numpy as np
from PIL import Image
from test.reg_utils import predict
import matplotlib.pyplot as plt


def pic_to_np(path, label_dict, pic_size: 224):
    pic_list = os.listdir(path)
    for pic in pic_list:
        pic_path = path + '/' + pic
        detect_pic(pic_path=pic_path, pic_size=pic_size)
    pass


def detect_pic(pic_path, pic_size):
    # 缩放
    image = Image.open(pic_path)
    re_image = image.resize((pic_size, pic_size))
    # 转换成numpy数组(仅一行)
    image_arr = np.array(re_image)
    # reshape的参数为-1代表自动计算剩余
    train_x_flatten = image_arr.reshape(-1, 1)
    result = predict(train_x_flatten)
    print(result)


def auto_move(path, parameter):
    pass


if __name__ == '__main__':
    # 自动将图片分类的参数
    # 注意：label_dict里是数字是key,标签是value
    dtx_config = {
        'path': './origin/'
        # 标签字典
        , 'label_dict': {
            1: 'yes',
            0: 'no'
        }
        # 训练集占的比例
        , 'train_percent': 0.85
        # 图片缩放的尺寸
        , 'pic_size': 168
        , 'isLog': True
    }

    pic_to_np(path=dtx_config.get('path')
              , label_dict=dtx_config.get('label_dict')
              , pic_size=dtx_config.get('pic_size'))
    pass
