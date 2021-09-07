def fun():
    print("123")


if __name__ == '__main__':
    print("Hello World")
    # arr = np.array([1, 2, 3])
    arr = [2021, 9, 7, 16, 11]

    a = 168
    if a < 168:
        print("a小于168")
    elif a >= 168:
        print("a大于168")
    else:
        print('a大于300')

    # 循环
    arrLen = len(arr)
    i = 0
    while i < len(arr):
        print(arr[i])
        i = i + 2

        print()
        for element in arr:
            print(element)

        print(arr)
