import os

os.environ["TF_CPP_MIN_LEVEL_LOG"] = '2'

import numpy as np
import tensorflow as tf

if __name__ == '__main__':
    x = tf.linspace(0, 1, 2)
    y = tf.linspace(2, 3, 2)
    print(x, y)
    x, y = tf.meshgrid(x, y)
    print(x, y)
