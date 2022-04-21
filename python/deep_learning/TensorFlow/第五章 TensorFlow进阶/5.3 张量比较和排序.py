import os

import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = "1"

if __name__ == '__main__':
    # ### 5.3 张量比较和排序
    #
    # #### 5.3.1 张量比较
    # 通过 tf.equal(a, b)(或 tf.math.equal(a, b)，两者等价)函数可以比较这 2 个张量是否相等
    # tf.equal()函数返回布尔类型的张量比较结果
    # 模拟10个样本的预测结果,pred = shape=(10,)
    out = tf.random.normal([10, 5])
    out = tf.nn.softmax(out, axis=1)
    # pred = [2 0 3 0 2 1 3 3 4 3]
    pred = tf.argmax(out, axis=1)
    print(pred)
    # y = [0 4 3 0 3 4 1 2 1 4]
    y = tf.random.uniform([10], dtype=tf.int64, maxval=5)
    print(y)
    out = tf.equal(pred, y)
    out = tf.reduce_sum(tf.cast(out, dtype=tf.float32))
    acc = out / y.shape[0]
    print(acc)

    # 除了比较相等的 tf.equal(a, b)函数，其它的比较函数用法类似，如:
    #
    # 1. tf.math.greater
    # 2. tf.math.less
    # 3. tf.math.greater_equal...等
    #
    # - tf.unique 返回去除重复的与索引号
    pass
