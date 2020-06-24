# -*- coding:utf-8 -*-
# @Time:2020/6/24 11:11
# @Author:TimVan
# @File:35. Search Insert Position.py
# @Software:PyCharm
# 35. Search Insert Position.py
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume no duplicates in the array.
# Example 1:
# Input: [1,3,5,6], 5
# Output: 2
#
# Example 2:
# Input: [1,3,5,6], 2
# Output: 1
#
# Example 3:
# Input: [1,3,5,6], 7
# Output: 4
#
# Example 4:
# Input: [1,3,5,6], 0
# Output: 0
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        j = 0
        lens = len(nums)
        while j < lens and nums[j] < target:

            j += 1


solution = Solution()
inputArr = [
    ([1, 3, 5, 6], 5)
    , ([1, 3, 5, 6], 2)
    , ([1, 3, 5, 6], 7)
    , ([1, 3, 5, 6], 0)]

for one in inputArr:
    print(solution.searchInsert(one[0], one[1]))
