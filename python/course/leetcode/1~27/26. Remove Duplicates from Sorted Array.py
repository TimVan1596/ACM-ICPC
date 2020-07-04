# -*- coding:utf-8 -*-
# @Time:2020/6/22 10:10
# @Author:TimVan
# @File:26. Remove Duplicates from Sorted Array.py
# @Software:PyCharm

# 26. Remove Duplicates from Sorted Array.py
# Given a sorted array nums, remove the duplicates in-place such that
# each element appear only once and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#   Given nums = [1,1,2],
#   Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
#   It doesn't matter what you leave beyond the returned length.
# Example 2:
#   Given nums = [0,0,1,1,1,2,2,3,3,4],
#   Your function should return length = 5,
#   with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#   It doesn't matter what values are set beyond the returned length.

# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference,
# which means modification to the input array will be known to the caller as well.
# Internally you can think of this:
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeDuplicates(nums);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }

from typing import List


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         numsLen = len(nums)
#         if numsLen == 0:
#             return 0
#         j = 1
#         # 由于仅有一个数列，所以
#         while j < len(nums):
#             element = nums[j]
#             if element in nums[0:j]:
#                 nums.pop(j)
#                 # 弹出后需要后移下标
#                 j -= 1
#             j += 1
#         return len(nums)

# 读题发现是 Sorted Array，因此不需要从 [0~j)下标内进行查找
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        # 由于仅有一个数列，所以nums的长度在不断变化
        while j < len(nums):
            element = nums[j]
            if element == nums[j-1]:
                nums.pop(j)
                # 弹出后需要后移修正下标
                j -= 1
            j += 1
        return len(nums)


solution = Solution()
inputArr = [
    [1, 1, 2],
    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
    [],
    [1, 2, 3],
    [100, 100, 100]
]
for one in inputArr:
    # print(one)

    lens = solution.removeDuplicates(one)
    print("lens=%d" % lens)
    i = 0
    while i < lens:
        print(one[i], end=",")
        i += 1
    print("\n")
