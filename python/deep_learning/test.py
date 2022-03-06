import numpy as np


# 激活函数
def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s
 

if __name__ == '__main__':
    x = np.arange(0, 9).reshape([3, 3])
    y = np.array([[0], [1], [2]])
    print(x.shape)
    print(y.shape)

    # [[[0 1] [0 2] [0 3]]
    # [[1 4] [1 5] [1 6]]
    # [[2 7] [2 8] [2 9]]]
    z = [[[y[i][0],x[i,j]] for j in range(x.shape[1])] for i in range(x.shape[0])]
    print(z.shape)
    print(z)
