# -*- coding:utf-8 -*-
# @Time:2020/6/29 18:52
# @Author:TimVan
# @File:53. Maximum Subarray.py
# @Software:PyCharm

# 53. Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach, which is more subtle.

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        lens = len(nums)
        for i in range(0, lens, 1):
            base = nums[i]
            if base > maxSum:
                maxSum = base
            for j in range(i + 1, lens, 1):
                # print("%d~%d" % (i, j))
                base += nums[j]
                if base > maxSum:
                    maxSum = base
        return maxSum


solution = Solution()
inputArr = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    , [100]
    ,
    [-1, 100]
    ,
    [-2, 1]
]

for one in inputArr:
    print(solution.maxSubArray(one))
