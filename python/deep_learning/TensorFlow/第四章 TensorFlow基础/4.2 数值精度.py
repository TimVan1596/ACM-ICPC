import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
import tensorflow as tf

if __name__ == '__main__':
    ### 4.2 数值精度

    # 常用的精度类型有
    # tf.int16、tf.int32、tf.int64、tf.float16、tf.float32、 tf.float64等。
    # 其中tf.float64即为tf.double。
    # 4.1.1 读取精度使用a.dtype
    # 4.1.2 类型转换使用tf.cast(a, dtype=tf.float32)

    a = 2 ** 16 + 1
    print("2**16={}".format(a))
    aa = tf.constant(a, dtype=tf.int16)
    ab = tf.constant(a, dtype=tf.int32)
    print(aa)
    print(ab)

    # 读取精度
    print("Before:{}".format(ab.dtype))
    if ab.dtype != tf.float32:
        ab = tf.cast(ab, tf.float32)
    print("After:{}".format(ab.dtype))

    # bool型转换
    a = tf.range(0, 3)
    a = tf.cast(a, dtype=tf.bool)
    print(a)
