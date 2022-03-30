import os

os.environ["TF_CPP_MIN_LEVEL_LOG"] = '2'

import tensorflow as tf


# 判断两个tensor的值是否相等
def tensor_equal(a, b):
    # 判断类型是否均为tensor
    if type(a) != type(b):
        return False
    if isinstance(a, type(tf.constant([]))) is not True:
        if isinstance(a, type(tf.Variable([]))) is not True:
            return False
    # 判断形状相等
    if a.shape != b.shape:
        return False
    # 逐值对比后若有False则不相等
    if not tf.reduce_min(tf.cast(a == b, dtype=tf.int32)):
        return False
    return True


if __name__ == '__main__':
    x = tf.constant([0, 1])
    ans = tensor_equal(x, tf.constant([0, 1]))
    print(ans)
    ans = tensor_equal(x, tf.constant([0, 1, 3]))
    print(ans)
    ans = tensor_equal(x, [0, 1])
    print(ans)
    ans = tensor_equal(x, tf.Variable([0, 1]))
    print(ans)
