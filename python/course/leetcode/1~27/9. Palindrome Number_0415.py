# -*- coding:utf-8 -*-
# @Time:2020/6/19 11:53
# @Author:TimVan
# @File:9. Palindrome Number.py
# @Software:PyCharm

# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
# Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
# Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]


solution = Solution()
num = 330001230132100033
print(solution.isPalindrome(num))
num = 123321
print(solution.isPalindrome(num))
num = 10
print(solution.isPalindrome(num))
num = 121
print(solution.isPalindrome(num))