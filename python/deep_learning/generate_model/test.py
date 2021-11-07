import h5py
import numpy as np
from matplotlib import pyplot as plt


if __name__ == '__main__':
    path = 'C://'
    name = 'train.h5'
    file = h5py.File(path+'/'+name, 'r')
    print(file.keys())

    print('train_y')
    print(np.array(file['train_y']))


    key_name = 'train_x'
    value = file[key_name]
    train_set_x = value
    arr = np.array(train_set_x)
    plt.imshow(arr[2])
    print(arr[2].shape)
    plt.show()

