import urllib.request as re
import numpy as np

if __name__ == "__main__":
    a = np.array(
        [
            [1, 2],
            [3, 4],
            [4, 6],
        ]
    )
    print(a.shape)

    b = np.sum(
        a,
        axis=0
    )
    print(b)

    c = np.sum(
        a,
        axis=1
    )

    print(c)
    print(a)
