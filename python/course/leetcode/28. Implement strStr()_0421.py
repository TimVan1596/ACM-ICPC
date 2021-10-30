# -*- coding:utf-8 -*-
# @Time:2020/6/23 16:10
# @Author:TimVan
# @File:28. Implement strStr().py
# @Software:PyCharm

# 28. Implement strStr()
# Implement strStr().
# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Clarification:
# What should we return when needle is an empty string?
# This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 极端情况的判断
        if len(needle) <= 0:
            return 0
        if len(haystack) <= 0 or len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle):
            return 0 if haystack == needle else -1
        # 滑动窗口判断
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:len(needle) + i] == needle:
                return i
            # print(haystack[i:len(needle) + i])
        return -1


solution = Solution()
inputArr = [
    # ("hello", "ll")
    # , ("aaaaa", "bba")
    # , ("hebbba", "bba")
    # , ("", "str")
    # , ("", "")
    # , ("haystackstackstacka", "stack")
    # , ("bbbbb", "")
    # , ("你好!Hello+。。+", "+。")
    # , ("a", "a")
    # ,
    ("abc", "c")
]
for one in inputArr:
    print(solution.strStr(one[0], one[1]))
