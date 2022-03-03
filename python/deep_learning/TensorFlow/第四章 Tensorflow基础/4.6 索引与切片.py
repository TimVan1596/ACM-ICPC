import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = '1'
import tensorflow as tf

if __name__ == '__main__':
    ### 4.6 索引与切片
    ##### 4.6.1 索引
    # 通过start: end: step切片方式, end为结束读取位置的索引(不包含end位)
    x = tf.random.normal([4, 32, 32, 3])
    print(x[0].shape)
    ##### 4.6.2 切片
    print(x[1:3].shape)
    print(x[0, ::].shape)
    x = tf.range(9)
    # 考虑最特殊的一种例子，当step = −1时，start:end: −1
    # 表示从start开始，逆序读取至end结束(不包含end)，索引号𝑒𝑛𝑑 ≤ 𝑠𝑡𝑎𝑟𝑡。
    print(x[::-1])
    # [8 6 4 2]
    print(x[8:0:-2])
    x = tf.random.normal([4, 32, 32, 3])
    print(x[0:2, ..., 1:].shape)
    # ##### 4.6.3 选择索引
    # - tf.gather(params, indices, axis=0)
    # 从params的axis维根据indices的参数值获取切片
    x = tf.reshape(tf.range(0, 10), [2, 5])
    print(x)
    print(tf.gather(x, [0, 2, 4], axis=1))
    # - tf.gather_nd(params, indices, name=None)
    # 按照indices的格式从params中抽取切片（合并为一个Tensor）
    # indices是一个K维整数Tensor，
    print(tf.gather_nd(x, [[0, 1], [0, 3], [1, 0]]))
