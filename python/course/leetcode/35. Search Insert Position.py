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


# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         j = 0
#         lens = len(nums)
#         while j < lens and target > nums[j]:
#             j += 1
#         return j


# 题解
# 由于是排序不重复数组，本题实质上为二分查找
#
# 二分法
# 初始化左指针l = 0，右指针r = n - 1
# r = n−1，其中n为数组长度。res = -1
# res =−1，用来保存target不在数组中的情况。
# 当l <= r时，执行循环：（注意！，因为初始化r = n - 1
# r = n−1，所以搜索区间为闭合区间[l, r]，因此结束条件为l > r，所以是l <= r）
#
# 定义mid = (l + r) // 2
# mid = (l + r) // 2，当nums[mid] == target时，返回mid,。
# 当nums[mid] > target时，说明target在搜索区间[l, mid - 1][l, mid−1]中，令r = mid - 1。
# 当nums[mid] < target时，说明target在搜索区间[mid + 1, r][mid + 1, r]中，令l = mid + 1。
# 此时，返回ll，即为插入位置，三种情况：
#
# [2, 3, 5, 6, 7], target = 4，此时l = 2，满足。
# [2, 3, 4, 5, 6], target = 0，此时l = 0，满足。
# [2, 3, 4, 5, 6], target = 7，此时l = 5，满足。
# 复杂度分析
# 时间复杂度：O(log n)
# 空间复杂度：O(1)
# Python
#二分查找
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums为空
        if not nums:
            return 0
        n = len(nums)
        left = 0
        right = n - 1
        res = -1
        while left <= right:
            # 向下取整
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        res = left
        return res


solution = Solution()
inputArr = [
    ([1, 3, 5, 6], 5)
    , ([1, 3, 5, 6], 2)
    , ([1, 3, 5, 6], 7)
    , ([1, 3, 5, 6], 0)]

for one in inputArr:
    print(solution.searchInsert(one[0], one[1]))
