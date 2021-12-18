import numpy as np
import math


# 将数据集切分成t份，便于实现mini-batch(先打乱，再拆分)
# x = 数据集，y=对应的结果
def split_data(x, y, t=1):
    # 首先判断x和y的长度是否匹配
    assert x.shape[1] == y.shape[1]
    m = x.shape[1]

    state = np.random.get_state()
    np.random.shuffle(x.T)
    np.random.set_state(state)
    np.random.shuffle(y.T)

    x_list = []
    y_list = []
    max_k = math.ceil(x.shape[1] / t)
    for i in range(max_k):
        start = i * t
        end = start + t if (start + t) <= m else None
        x_list.append(x[:, start:end])
        y_list.append(y[:, start:end])
    return x_list, y_list


if __name__ == '__main__':
    x = np.linspace(1, 10, 10, dtype='int').reshape(2, 5)
    y = np.array([x[0, i] + x[1, i] for i in range(len(x[0,]))]).reshape(1, -1)
    print(x)
    print(y)
    dataset = (x, y)

    # 切分成每单位2个
    x_list, y_list = split_data(x, y, t=2)
    print(x_list)
    print(y_list)
