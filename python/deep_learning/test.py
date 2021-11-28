import numpy as np


# 激活函数
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s


if __name__ == '__main__':
    keys = []
    key = 'W1'
    parameter = {
        'W1': np.array([
            [0, 1, 2], [3, 4, 5]
        ])
    }
    new_vector = np.reshape(parameter[key], (-1, 1))
    keys = keys + [key] * new_vector.shape[0]
    print(keys)
