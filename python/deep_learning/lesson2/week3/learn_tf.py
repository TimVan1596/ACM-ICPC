import tensorflow as tf

if __name__ == '__main__':

    w = tf.Variable(tf.constant(4, dtype=tf.float32))  # 设定w初始值5
    times = 1000  # 循环迭代1000次

    for i in range(times):
        loss = 0
        with tf.GradientTape() as tape:
            loss = w ** 2 - 6 * w + 9  # 损失函数 Loss = w*w-20*w+100
        grads = tape.gradient(loss, w)  # 求loss函数在w处的导数
        w.assign_sub(loss / grads)  # 通过减法，让w向loss取得极小值的方向逼近
    print("经过 %s 次学习后,w = %f,loss = %f" % (times, w.numpy(), loss))
