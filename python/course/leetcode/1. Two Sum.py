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

def twoSum(nums, target):
    global i
    lens = len(nums)
    j = -1
    for i in range(lens):
        if (target - nums[i]) in nums:
            # 如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
            if (nums.count(target - nums[i]) == 1) & (target - nums[i] == nums[i]):
                continue
            else:
                # index(x,i+1)是从num1后的序列后找num2
                j = nums.index(target - nums[i], i + 1)
                break
    if j > 0:
        return [i, j]
    else:
        return []
# 执行通过，不过耗时较长，共 1636ms。
