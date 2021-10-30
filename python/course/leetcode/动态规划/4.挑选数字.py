# -*- coding:utf-8 -*-
# @Time:2020/7/5 18:37
# @Author:TimVan
# @File:4.挑选数字.py
# @Software:PyCharm

# 挑选数字
# 给定一组数字，若可挑选某些数字使得它们相加符合目标，则返回true，否则返回false
def isConformTargetDriver(arr: list, target: int) -> bool:
    num = arr[0]
    # 判断是否为target
    if target == num:
        return True

    # 结束条件
    if len(arr) > 1:
        # 选择当前数字，target = target-num
        ret = isConformTargetDriver(arr[1:], target - num)
        if ret:
            return ret
        # 不选择当前数字，target = target
        ret = isConformTargetDriver(arr[1:], target)
        if ret:
            return ret

    return False


inputArr = [
    ([1, 2, 4, 1, 7, 8, 3], 5),
    ([99, 1, 99, 1, 99, 1000], 3),
    ([4, 1, 1, 9, 1], 10),
    ([100], 100),
    ([100, 200, 300], 99),
    ([100, 200, 300, 12, 4, 2020, 77, -3], 13),
]
for one in inputArr:
    print("-> %s" % isConformTargetDriver(one[0], one[1]))
