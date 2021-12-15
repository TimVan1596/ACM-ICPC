import numpy as np


# 将数据集切分成t份，便于实现mini-batch
def split_data(dataset: list, t=1):
    x = dataset[:][0]
    y = dataset[:][1]

    state = np.random.get_state()
    np.random.shuffle(x)
    np.random.set_state(state)
    np.random.shuffle(y)

    for i in range(len(dataset)):
        print(x)
        print(y)
    # np.shuffle(dataset)


if __name__ == '__main__':
    x = np.linspace(1, 10, 10, dtype='int').reshape(2, 5)
    y = [x[0, i] + x[1, i] for i in range(len(x[0,]))]
    print(x)
    print(y)
    dataset = [(x[:, i], y[i]) for i in range(len(y))]
    split_data(dataset)
