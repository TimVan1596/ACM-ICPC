import os
import numpy as np
import matplotlib.pyplot as plt
import h5py


# 导入必要的包

def get_files(file_dir):
    yes_list = []
    label_yes_list = []

    not_list = []
    label_not_list = []

    for file in os.listdir(file_dir + '/not_tumble'):
        not_list.append(file_dir + '/not_tumble' + '/' + file)
        label_not_list.append(0)  # 添加标签，该类标签为0，此为2分类例子，多类别识别问题自行添加
    for file in os.listdir(file_dir + '/yes_tumble'):
        yes_list.append(file_dir + '/yes_tumble' + '/' + file)
        label_yes_list.append(1)

    # 把cat和dog合起来组成一个list（img和lab）
    image_list = np.hstack((not_list, yes_list))
    label_list = np.hstack((label_not_list, label_yes_list))

    # 利用shuffle打乱顺序
    temp = np.array([image_list, label_list])
    temp = temp.transpose()
    np.random.shuffle(temp)

    # 从打乱的temp中再取出list（img和lab）
    image_list = list(temp[:, 0])
    label_list = list(temp[:, 1])
    label_list = [int(i) for i in label_list]

    return image_list, label_list
    # 返回两个list 分别为图片文件名及其标签  顺序已被打乱


if __name__ == '__main__':
    train_dir = 'd:/deep'
    image_list, label_list = get_files(train_dir)

    print(len(image_list))
    print(len(label_list))

    # 450为数据长度的20%
    Train_image = np.random.rand(len(image_list) - 6, 64, 64, 3).astype('float32')
    Train_label = np.random.rand(len(image_list) - 6, 1).astype('float32')

    Test_image = np.random.rand(6, 64, 64, 3).astype('float32')
    Test_label = np.random.rand(6, 1).astype('float32')

    for i in range(len(image_list) - 6):
        Train_image[i] = np.array(plt.imread(image_list[i]))
        Train_label[i] = np.array(label_list[i])

    for i in range(len(image_list) - 6, len(image_list)):
        Test_image[i + 6 - len(image_list)] = np.array(plt.imread(image_list[i]))
        Test_label[i + 6 - len(image_list)] = np.array(label_list[i])

    # Create a new file
    f = h5py.File('data.h5', 'w')
    f.create_dataset('X_train', data=Train_image)
    f.create_dataset('y_train', data=Train_label)
    f.create_dataset('X_test', data=Test_image)
    f.create_dataset('y_test', data=Test_label)
    f.close()

    # Load hdf5 dataset
    train_dataset = h5py.File('data.h5', 'r')
    train_set_x_orig = np.array(train_dataset['X_train'][:])  # your train set features
    train_set_y_orig = np.array(train_dataset['y_train'][:])  # your train set labels
    test_set_x_orig = np.array(train_dataset['X_test'][:])  # your train set features
    test_set_y_orig = np.array(train_dataset['y_test'][:])  # your train set labels
    f.close()

    # 测试
    plt.imshow(train_set_x_orig[5])
    print(train_set_y_orig[5])
