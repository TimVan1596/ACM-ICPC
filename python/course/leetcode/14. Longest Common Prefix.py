# -*- coding:utf-8 -*-
# @Time:2020/6/20 12:04
# @Author:TimVan
# @File:14. Longest Common Prefix.py
# @Software:PyCharm

# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
#
# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
# All given inputs are in lowercase letters a-z.
from typing import List


# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         if len(strs) < 1:
#             return ""
#
#         commonPrefix = strs[0]
#         i = 1
#         lens = len(strs)
#         while i < lens:
#             strSingle = strs[i]
#             j = 0
#             lenStr = len(strSingle)
#             lenCommonPrefix = len(commonPrefix)
#             cacheCommon = ""
#             # 字符数需要小于公共串和每个单词
#             while j < min(lenStr, lenCommonPrefix):
#                 if commonPrefix[j] == strSingle[j]:
#                     cacheCommon += commonPrefix[j]
#                     j += 1
#                 else:
#                     # 若第一个字母不同，说明直接无公共字符
#                     if j == 0:
#                         return ""
#                     # 跳出循环尝试下一个
#                     else:
#                         break
#             commonPrefix = cacheCommon
#             # print(i, "-", commonPrefix)
#             i += 1
#
#         return commonPrefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for one in zip(*strs):
            if len(set(one)) == 1:
                s += one[0]
            else:
                break
        return s


solution = Solution()
myStrArrayList = [["flower", "flow", "flight"]
    , ["dog", "racecar", "car"]
    , ["self", "self", "self"]
    , ["gitee", "github", "gitlab"]
    , []]
for myStrS in myStrArrayList:
    print("***", solution.longestCommonPrefix(myStrS))
