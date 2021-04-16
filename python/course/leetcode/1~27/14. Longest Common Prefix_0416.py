# -*- coding:utf-8 -*-
# @Time:2020/6/20 12:04
# @Author:TimVan
# @File:14. Longest Common Prefix.py
# @Software:PyCharm


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = 1000
        if len(strs) <= 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs)):
            if len(strs[i]) <= 0:
                return ""
            elif len(strs[i]) < minLen:
                minLen = len(strs[i])
        commonPrefix = ""
        for i in range(minLen):
            currChar = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != currChar:
                    return commonPrefix
            commonPrefix += currChar
        return commonPrefix


solution = Solution()
myStrArrayList = [["flower", "flow", "flight"]
    , ["dog", "racecar", "car"]
    , ["self", "self", "self"]
    , ["gitee", "github", "gitlab"]
    , []
    , ["ab", "a"]]
for myStrS in myStrArrayList:
    print("***", solution.longestCommonPrefix(myStrS))
