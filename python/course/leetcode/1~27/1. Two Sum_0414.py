# -*- coding:utf-8 -*-
# @Time:2020/6/13 22:21
# @Author:TimVan
# @File:1. Two Sum.py
# @Software:PyCharm

from typing import List


# 通过字典的方法，查找效率快很多，执行速度大幅缩短，共 88ms。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsLength = len(nums)
        # 定义一个哈希表，k是列表的值，v是列表下标
        hashMap = {}
        for i in range(numsLength):
            # 若在哈希表已含有即命中
            if target - nums[i] in hashMap:
                return [hashMap[target - nums[i]], i]
            # 若已有重复的key，仅保留第一个
            # 若无则新建
            elif nums[i] not in hashMap:
                hashMap[nums[i]] = i
        return []


myNums = [3, 2, 5, 1, 16,
          38, 20, 6, 14, 39]
myTarget = 20
# myNums = [3, 4, 5]
# myTarget = 6
# myNums = [3, 3, 5]
# myTarget = 6
solution = Solution()
print(solution.twoSum(myNums, myTarget))
