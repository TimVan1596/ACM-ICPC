# -*- coding:utf-8 -*-
# @Time:2020/6/13 22:21
# @Author:TimVan
# @File:1. Two Sum.py
# @Software:PyCharm

# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = 0
        # 内、外层循环
        for i in range(len(nums) - 1):
            j = i + 1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
        return [i, j]


myNums = [3, 2, 4]
myTarget = 6
solution = Solution()
print(solution.twoSum(myNums, myTarget))
