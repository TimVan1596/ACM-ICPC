# -*- coding:utf-8 -*-
# @Time:2020/6/16 11:40
# @Author:TimVan
# @File:2. Add Two Numbers.py
# @Software:PyCharm

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         p1 = l1
#         p2 = l2
#         listNode3 = ListNode(0)
#         p3 = listNode3
#         # 每次相加的进位
#         rest = 0
#         while (p1 is not None) or (p2 is not None):
#             if p1 is None:
#                 p1 = ListNode(0)
#             if p2 is None:
#                 p2 = ListNode(0)
#
#             val1 = p1.val
#             val2 = p2.val
#
#             p3.val = (rest + val1 + val2) % 10
#             rest = int((rest + val1 + val2) / 10)
#
#             # 是否还有下一位
#             if p1.next is not None:
#                 p1 = p1.next
#             else:
#                 p1 = None
#             if p2.next is not None:
#                 p2 = p2.next
#             else:
#                 p2 = None
#
#             if (p1 is not None) or (p2 is not None):
#                 p3.next = ListNode(0)
#                 p3 = p3.next
#             else:
#                 break
#         # 还余进位
#         if rest > 0:
#             p3.next = ListNode(rest)
#         return listNode3


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         # 保存头结点，返回结果
#         dummy = p = ListNode(None)
#         # 每一步的求和暂存变量
#         s = 0
#         # 循环条件：l1 或者l2（没有遍历完成），s(进位)不为0
#         while l1 or l2 or s:
#             # 这其实是好多代码，我自己写了好多行，但是作者这样写非常简洁，赞
#             s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
#             # 构建新的list存储结果，其实用较长的加数链表存也可以，%10：求个位
#             p.next = ListNode(s % 10)
#             p = p.next
#             # 求进位
#             s //= 10
#             l1 = l1.next if l1 else None
#             l2 = l2.next if l2 else None
#         return dummy.next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:


myL1 = ListNode(2)
myL1.next = ListNode(4)
myL1.next.next = ListNode(3)
myL2 = ListNode(5)
myL2.next = ListNode(6)
myL2.next.next = ListNode(4)

# myL1 = ListNode(5)
# myL2 = ListNode(4)

solution = Solution()
listNode = solution.addTwoNumbers(myL1, myL2)
while listNode is not None:
    print(listNode.val)
    listNode = listNode.next
