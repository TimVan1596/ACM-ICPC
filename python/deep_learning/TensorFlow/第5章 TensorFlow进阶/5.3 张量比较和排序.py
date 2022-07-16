import os

import tensorflow as tf
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.3 张量比较和排序
    #
    # #### 5.3.1 张量比较
    # 通过 tf.equal(a, b)(或 tf.math.equal(a, b)，两者等价)函数可以比较这 2 个张量是否相等
    # tf.equal()函数返回布尔类型的张量比较结果
    # 模拟10个样本的预测结果,pred = shape=(10,)
    # out = tf.random.normal([10, 5])
    # out = tf.nn.softmax(out, axis=1)
    # # pred = [2 0 3 0 2 1 3 3 4 3]
    # pred = tf.argmax(out, axis=1)
    # print(pred)
    # # y = [0 4 3 0 3 4 1 2 1 4]
    # y = tf.random.uniform([10], dtype=tf.int64, maxval=5)
    # print(y)
    # out = tf.equal(pred, y)
    # out = tf.reduce_sum(tf.cast(out, dtype=tf.float32))
    # acc = out / y.shape[0]
    # print(acc)

    # 除了比较相等的 tf.equal(a, b)函数，其它的比较函数用法类似，如:
    #
    # 1. tf.math.greater
    # 2. tf.math.less
    # 3. tf.math.greater_equal...等
    #
    # - tf.unique 返回去除重复的与索引号

    # #### 5.3.2 张量排序
    # 1. 排序sort,argsort:求排序和索引
    # 一、排序sort
    # tf.sort(tensor, direction= ’ ’ )
    # a = tf.random.shuffle(tf.range(7))
    # # [0 2 6 3 5 4 1]
    # print(a)
    # # [0 1 2 3 4 5 6]
    # print(tf.sort(a))
    # # [0 2 6 3 5 4 1]
    # print(a)
    #
    # a = tf.random.shuffle(tf.reshape(tf.range(10), shape=[2, -1]))
    # # [[0 1 2 3 4]
    # #  [5 6 7 8 9]]
    # print(a)
    # # [[5 6 7 8 9]
    # #  [0 1 2 3 4]]
    # print(tf.sort(a, axis=0, direction='DESCENDING'))

    # tf.argsort( tensor )获取索引,默认axis=-1，纵0横1
    # **特别的，argsort是原来元素在排序后所在的下标**
    # a_np = np.arange(9)
    # np.random.shuffle(a_np)
    # a = tf.constant(a_np.reshape((3, -1)))
    # # [[0 4 3]
    # #  [2 6 1]
    # #  [7 5 8]]
    # print(a)
    # # [[0 2 1]
    # #  [1 2 0]
    # #  [1 0 2]]
    # print(tf.argsort(a))

    # 2. 前k大值 Top_k,res=tf.math.top_k(a,2)
    # a = [18, 56, 20.22, 42.7, 71, 30]
    # # [71.  56.  42.7]
    # print(tf.math.top_k(a, 3).values.numpy())

    # 3. Top Acc:前N个中有没有命中的准确率
    # prob = tf.constant([[0.3, 0.2, 0.7], [0.2, 0.1, 0.8]])
    # target = tf.constant([2, 0])
    # k_b = tf.math.top_k(prob, k=2).indices
    # # k_b =[[2,1],[1,0]]
    # print(k_b)
    # target = tf.broadcast_to(target, [2, 2])
    #
    # correct = tf.equal(target, k_b)
    # bool2int = tf.cast(correct, dtype=tf.int32)
    # # bool2int =[[1,0],[0,1]]
    # print(bool2int)
    # num_of_pre_correct = tf.reduce_sum(bool2int)
    # top_k_accuracy = num_of_pre_correct / target.shape[0]
    # # top_k_accuracy = 1
    # print(top_k_accuracy)

    # 4. tf.unique() 返回去除重复的与给出索引，并且可以用tf.gather()进行还原
    a = tf.constant([3, 6, 2, 0, 2, 6])
    unique = tf.unique(a)
    # Unique(y=<tf.Tensor: shape=(4,), dtype=int32, numpy=array([3, 6, 2, 0])>,
    # idx=<tf.Tensor: shape=(6,), dtype=int32, numpy=array([0, 1, 2, 3, 2, 1])>)
    print(unique)
    # tf.Tensor([3 6 2 0 2 6], shape=(6,), dtype=int32)
    print(tf.gather(unique.y, unique.idx))
    pass
