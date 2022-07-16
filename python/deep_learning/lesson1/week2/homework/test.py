import h5py
import numpy as np
from matplotlib import pyplot as plt

file = h5py.File('datasets/train_catvnoncat.h5', 'r')
print(file.keys())

# keys = file.keys()
# for key_name in keys:
#     value = file[key_name]
#     print('key_name = ')
#     print(key_name)
#     print('value = ')
#     print(value)
#     print('-' * 10)


key_name = 'list_classes'
value = file[key_name]

print('key_name = ')
print(key_name)
print('value = ')
print(value[0])
print(value[1])
print('-' * 10)

key_name = 'train_set_x'
value = file[key_name]
print(value)
train_set_x = value
print(train_set_x.shape)

arr = np.array(train_set_x)
plt.imshow(arr[2])
plt.show()