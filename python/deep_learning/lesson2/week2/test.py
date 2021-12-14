import numpy as np


# 将数据集切分成t份，便于实现mini-batch
def split_data(dataset: list, t=1):
    for i in range(len(dataset)):
        x = dataset[i][0]
        y = dataset[i][1]
        print(x)
        print(y)
    # np.shuffle(dataset)


if __name__ == '__main__':
    x = np.linspace(1, 10, 10, dtype='int').reshape(2, 5)
    y = [0, 0, 1, 1, 1]
    print(x)
    print(y)
    dataset = [(x[:, i], y[i]) for i in range(len(y))]
    split_data(dataset)
