from bs4 import BeautifulSoup
import numpy as np


def test_fun(fun, a, b):
    fun(a)


def has_tag(var):
    print("执行了参数,var={}".format(var))
    return True


if __name__ == '__main__':
    # soup = BeautifulSoup("<div class='black'>data</div><div class='black'>number</div><div class='red'>text</div>",
    #                      "html.parser")
    # list = soup.find_all(has_tag)
    # print(list)
    # test_fun(has_tag, 3, 4)
    w1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 6, 2]])
    X = np.array([[20, 11], [21, 6], [9, 8]])
    print(w1)
    print()
    print(X)
