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
        if len(needle) <= 0:
            return 0
        if len(haystack) <= 0 or len(haystack) < len(needle):
            return -1
        i = 0
        lens = len(haystack)
        index = 0
        needleIndex = 0
        isInSearch = False
        while i < lens:
            # 若未进入查找程序 且 首字符相同
            if (isInSearch is False) and haystack[i] == needle[needleIndex]:
                index = i
                needleIndex += 1
                if needleIndex == len(needle):
                    return index
                isInSearch = True
            # 进入查找程序，注意是 elif
            elif isInSearch:
                # 若相同
                if haystack[i] == needle[needleIndex]:
                    needleIndex += 1
                    if needleIndex == len(needle):
                        return index
                # 若不相同则跳回
                else:
                    i = index
                    needleIndex = 0
                    isInSearch = False
            i += 1
        return -1


solution = Solution()
inputArr = [
    ("hello", "ll")
    , ("aaaaa", "bba")
    , ("hebbba", "bba")
    , ("", "str")
    , ("", "")
    , ("haystackstackstacka", "stack")
    , ("bbbbb", "")
    , ("你好!Hello+。。+", "+。")
    ,
    ("a", "a")]
for one in inputArr:
    print(solution.strStr(one[0], one[1]))
