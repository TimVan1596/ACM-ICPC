#### 6.4 激活函数
import tensorflow as tf
from keras import layers, Sequential


if __name__ == "__main__":

    # #### 6.4 激活函数
    x = tf.linspace(-6, 6, 13)

    # - 可以通过 tf.nn.sigmoid 实现 Sigmoid 函数
    print(tf.nn.sigmoid(x))
    # - 可以通过 tf.nn.relu 实现 ReLU 函数
    # [0. 0. 0. 0. 0. 0. 0. 1. 2. 3. 4. 5. 6.], shape=(13,)
    print(tf.nn.relu(x))
    # - LeakyReLU 函数=𝑝𝑥,𝑥 < 0,可以通过 tf.nn.leaky_relu 实现 LeakyReLU 函数,其中 alpha 参数代表𝑝
    # x=[-1.20000002 -1.00000001 -0.80000001 -0.60000001 -0.40000001 -0.2
    #   0.          1.          2.          3.          4.          5.
    #   6.        ]
    print(tf.nn.leaky_relu(x))    
    # - 可以通过 tf.nn.tanh 实现 tanh 函数
    # 可以看到向量元素值的范围被映射到(−1,1)之间
    print(tf.nn.tanh(x))    
    pass
