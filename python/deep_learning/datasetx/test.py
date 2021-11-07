import h5py
import numpy as np
from matplotlib import pyplot as plt

# # 同序shuffle-按相同顺序打乱两个数组
# def same_shuffle(arr1: list, arr2: list):
#     rand_state = np.random.get_state()
#     np.random.shuffle(arr1)
#     np.random.set_state(rand_state)
#     np.random.shuffle(arr2)
#     return arr1, arr2


if __name__ == '__main__':
    # path = 'C://'
    # name = 'train.h5'
    # file = h5py.File(path+'/'+name, 'r')
    # print(file.keys())
    #
    # print('train_y')
    # print(np.array(file['train_y']))
    #
    #
    # key_name = 'train_x'
    # value = file[key_name]
    # train_set_x = value
    # arr = np.array(train_set_x)
    # plt.imshow(arr[2])
    # print(arr[2].shape)
    # plt.show()

    # import numpy as np
    #
    # a = np.arange(0, 10, 1)
    # b = np.arange(10, 20, 1)
    # print(a, b)
    #
    # a, b = same_shuffle(a, b)
    #
    # print(a, b)
    # result:[16 14 15 13 17 12 10 11 18 19]
    arr = [(1, 10), (2, 20), (3, 30)]
    arr1 = [elem[0] for elem in arr]
    arr2 = [elem[1] for elem in arr]
    print(arr1)
    print(arr2)
