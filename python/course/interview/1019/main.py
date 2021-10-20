import numpy as np


class MyList:
    arr = []
    index = -1

    def __init__(self, arr):
        self.arr = arr
        print(self.arr)

    def __iter__(self):
        self.index = self.index + 1
        return self

    def __next__(self):
        max = len(arr)
        if self.index + 1 >= max:
            raise StopIteration
        else:
            self.index = self.index + 1

        return self.arr[self.index]


if __name__ == '__main__':
    # myList = [15, 54, 2021, 10, 19]
    # it = iter(myList)
    # for elem in myList:
    #     print(type(elem))
    #     print(elem)
    #     print(next(it))
    arr = [15, 54, 2021, 10, 19]
    myList = MyList(arr)
    myiter = iter(myList)
    while True:
        print(next(myiter))
