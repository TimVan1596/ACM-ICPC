# -*- coding:utf-8 -*-
# @Time:2020/6/18 11:59
# @Author:TimVan
# @File:7. Reverse Integer.py
# @Software:PyCharm

# Given a 32-bit signed integer, reverse digits of an integer.
# Example 1:
# Input: 123
# Output: 321
#
# Example 2:
# Input: -123
# Output: -321
#
# Example 3:
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        leadingZero = True
        isMinus = False
        if x < 0:
            isMinus = True
            x = -x
        while x > 0:
            rest = x % 10
            if leadingZero and (rest != 0):
                leadingZero = False
            if not leadingZero:
                n *= 10
                n += rest
            x //= 10
        if isMinus:
            n = -n
        # 越界检测
        if n < (-2 ** 31) or n > (2 ** 31 + 1):
            n = 0
        return n


myX: int = 123
myX = -10200
myX = 4294967296
solution = Solution()
print(solution.reverse(myX))
