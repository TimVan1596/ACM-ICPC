# -*- coding:utf-8 -*-
# @Time:2021/4/27 13:39
# @Author:TimVan
# @File:35. 搜索插入位置.py.py
# @Software:PyCharm

# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 你可以假设数组中无重复元素。
#
# 示例 1:
# 输入: [1,3,5,6], 5
# 输出: 2
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)


solution = Solution()
nums = [1, 3, 5, 6]
target = 5
print(solution.searchInsert(nums, target))
