import tensorflow as tf
import matplotlib.pyplot as plt

if __name__ == '__main__':
    print("当前Tensorflow版本为：{}".format(tf.__version__))
    x = []
    y = []
    w = tf.Variable(tf.constant(5, dtype=tf.float32))  # 设定w初始值5
    a = 0.01  # 学习率
    times = 1000  # 循环迭代40次

    for i in range(times):
        loss = 0
        with tf.GradientTape() as tape:
            loss = (w - 10) ** 2  # 损失函数 Loss = w*w-20*w+100
        grads = tape.gradient(loss, w)  # 求loss函数在w处的导数
        w.assign_sub(a * grads)  # 通过减法，让w向loss取得极小值的方向逼近
        if i % 10 == 0:
            x.append(i)
            y.append(loss)
    print("经过 %s 次学习后,w = %f,loss = %f" % (times, w.numpy(), loss))

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 这两行需要手动设置
    plt.xlabel("x/times")
    plt.ylabel("损失函数")
    plt.title('Tensorflow 梯度下降')
    plt.plot(x, y, color='orange')
    plt.show()
