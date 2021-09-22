import numpy as np

if __name__ == '__main__':
    W1 = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 6, 2],
    ])
    X = np.array([
        [20, 11],
        [21, 6],
        [9, 8],
    ])
    ret = np.dot(W1, X)
    print(ret)
