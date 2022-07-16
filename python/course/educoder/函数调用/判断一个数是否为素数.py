# 引入numpy库
import numpy as np


# 定义cnmda函数
def cnmda(m, n):
    '''
    创建numpy数组
    参数：
   		m:第一维的长度
   		n: 第二维的长度
    返回值:
    	ret: 一个numpy数组
    '''

    ret = 0

    # 请在此添加创建多维数组的代码并赋值给ret
    # ********** Begin *********#
    ret = np.random.randn(m, n)
    # ********** End **********#

    return ret


fd = 5
sd = 8
array = cnmda(int(fd), int(sd))
print(array.shape)
