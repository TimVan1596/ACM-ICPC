# -*- coding:utf-8 -*-
# @Time:2020/6/29 18:52
# @Author:TimVan
# @File:53. Maximum Subarray.py
# @Software:PyCharm


# 58. Length of Last Word
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word
# (last word means the last appearing word if we loop from left to right) in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a maximal substring consisting of non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        ret = s.find(' ')
        if ret < 0:
            return 1
        arr = s.split(' ')
        return len(arr[-1])



if __name__ == '__main__':
    solution = Solution()
    inputArr = [
        "Error Loading Project can not "
        ,"Hello World"
        ,"Given a string s consists of"
        ,'a'
    ]

    for one in inputArr:
        print(solution.lengthOfLastWord(one))
