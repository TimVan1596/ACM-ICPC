import os

import keras.datasets.imdb
import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.4 填充与复制
    #
    # #### 5.4.1 填充
    # 填充操作可以通过 tf.pad(x, paddings)函数实现
    # 参数 paddings 是包含了多个[Left Padding,Right Padding]的嵌套方案 List
    # 如[[0,0],[2,1],[1,2]]表示第一个维度不填充，
    # 第二个维度左边(起始处)填充两个单元，右边(结束处)填充一个单元，
    # 第三个维度左边 填充一个单元，右边填充两个单元
    # 考虑上述 2 个句子的例子，需要在第二个句子的第一个维度的右边填充 2 个单元，则 paddings 方案为[[0,2]]：
    # a = tf.constant([1, 2, 3, 4, 5, 6])  # 第一个句子
    # b = tf.constant([7, 8, 1, 6])  # 第二个句子
    # b = tf.pad(b, [[0, 2]])
    # # [7, 8, 1, 6, 0, 0]
    # print(b)
    # # 填充后句子张量形状一致，再将这 2 句子 Stack 在一起，代码如下
    # c = tf.stack([a, b], axis=0)
    # # [[1 2 3 4 5 6]
    # #  [7 8 1 6 0 0]]
    # print(c)
    # 以 IMDB 数据集的加载为例，
    # 我们来演示如何将不等长的句子变换为等长结构
    # 对于小于 80 个单词的句子，在末尾填充相应数量的 0；
    # 对大于 80 个单词的句子，截断超过规定长度的部分单词
    # total_words = 10000  # 设定词汇量大小
    # max_review_len = 80  # 最大句子长度
    # embedding_len = 100  # 词向量长度
    # # 加载IMDB数据集
    # # only the `num_words` most frequent words are kept
    # (x, y), (x_test, y_test) = keras.datasets.imdb.load_data(num_words=total_words)
    # (x, y), (x_test, y_test).shape均为(25000,)
    # 218
    # 1
    # 189
    # print(len(x[0]), y[0], len(x[1]))
    # # # 将句子填充或截断到相同长度，设置为末尾填充和末尾截断方式
    # x_train = keras.preprocessing.sequence.pad_sequences(x, maxlen=max_review_len
    #                                                      , truncating='post', padding='post')
    # x_test = keras.preprocessing.sequence.pad_sequences(x_test,
    #                                                     maxlen=max_review_len, truncating='post', padding='post')
    # # (25000, 80) (25000, 80)
    # # 上述代码中，我们将句子的最大长度 max_review_len 设置为 80 个单词，通过
    # # keras.preprocessing.sequence.pad_sequences 函数可以快速完成句子的填充和截断工作
    # # 可以看到在句子末尾填充了若干数量的 0，使得句子的长度刚好 80
    # print(x_train.shape, x_test.shape)  # 打印等长的句子张量形状

    # 如果网络层所接受的数据高宽为32 × 32，则必须将28 × 28大小填充到32 × 32，
    # 可以选择在图片矩阵的上、下、左、右方向各填充 2 个单元
    x = tf.random.normal([4, 28, 28, 1])
    # 图片上下、左右各填充 2 个单元
    x = tf.pad(x, [[0, 0], [2, 2], [2, 2], [0, 0]])
    print(x.shape)
    pass
