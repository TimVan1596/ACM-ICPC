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


# 最初解法
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         i = 0
#         j = 0
#         # 内、外层循环
#         for i in range(len(nums) - 1):
#             j = i + 1
#             while j < len(nums):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#                 j += 1
#         return [i, j]
#
#
# myNums = [3, 2, 4]
# myTarget = 6
# solution = Solution()
# print(solution.twoSum(myNums, myTarget))


# 方法一：
# 解题关键主要是想找到
# num2 = target - num1，是否也在 list 中，那么就需要运用以下两个方法：
# num2 in nums，返回 True 说明有戏
# nums.index(num2)，查找 num2 的索引
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        global i
        lens = len(nums)
        j = -1
        for i in range(lens):
            num1 = nums[i]
            num2 = target - num1
            try:
                j = nums.index(num2, i + 1)
                break
            except:
                continue
        if j > 0:
            return [i, j]
        else:
            return []


# 执行通过，不过耗时较长，共 1636ms。

myNums = [3, 2, 5, 1, 16,
          38, 20, 6, 14, 39]
myTarget = 20
# myNums = [3, 2, 4]
# myTarget = 6
solution = Solution()
print(solution.twoSum(myNums, myTarget))
