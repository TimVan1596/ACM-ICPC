# -*- coding:utf-8 -*-
# @Time:2020/6/22 15:53
# @Author:TimVan
# @File:27. Remove Element.py
# @Software:PyCharm

# 27. Remove Element
# Given an array nums and a value val,
# remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array,
#     you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#
# Example 1:
#     Given nums = [3,2,2,3], val = 3,
#     Your function should return length = 2, with the first two elements of nums being 2.
#     It doesn't matter what you leave beyond the returned length.
#
# Example 2:
#     Given nums = [0,1,2,2,3,0,4,2], val = 2,
#     Your function should return length = 5,
#     with the first five elements of nums containing 0, 1, 3, 0, and 4.
#     Note that the order of those five elements can be arbitrary.
#     It doesn't matter what values are set beyond the returned length.
#
# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference,
# which means modification to the input array will be known to the caller as well.
# Internally you can think of this:
#     // nums is passed in by reference. (i.e., without making a copy)
#     int len = removeElement(nums, val);
#
#     // any modification to nums in your function would be known by the caller.
#     // using the length returned by your function, it prints the first len elements.
#     for (int i = 0; i < len; i++) {
#         print(nums[i]);
#     }
from typing import List


# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         j = 0
#         # 由于仅有一个数列，所以nums的长度在不断变化
#         while j < len(nums):
#             element = nums[j]
#             if element == val:
#                 nums.pop(j)
#                 # 弹出后需要后移修正下标
#                 j -= 1
#             j += 1
#         return len(nums)


# 移除list的多个元素时，采用倒序遍历
# 如果需要在正向遍历的过程中，删除list的多个元素，需要判断，如果删除，index值不能变，比较麻烦
# 反向遍历就不会存在这个问题，代码也就简单了很多。
# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         for i in range(len(nums) - 1, -1, -1):
#             if (nums[i] == val):
#                 nums.pop(i)
#         return len(nums)


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)

solution = Solution()
inputArr = [
    ([3, 2, 2, 3], 3),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2),
    ([], 1),
    ([10, 10, 10], 10),
    ([35, 35, 35], 10)
]
for one in inputArr:
    # print(one)
    lens = solution.removeElement(one[0], one[1])
    print("lens=%d" % lens)
    i = 0
    while i < lens:
        print(one[0][i], end=",")
        i += 1
    print("\n")
