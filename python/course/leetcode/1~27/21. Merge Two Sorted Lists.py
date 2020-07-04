# -*- coding:utf-8 -*-
# @Time:2020/6/21 17:13
# @Author:TimVan
# @File:21. Merge Two Sorted Lists.py
# @Software:PyCharm

# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example 1:
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
# Example 2:
# Input: 1->7->10->44->100, 2->3->4
# Output: 1->2->3->4->7->10->44->100

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 解法1 正常思路，考虑链表本身
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        q = l2
        # 带头结点的链表
        newListNode = ListNode(0)
        m = newListNode
        while p and q:
            first = p.val
            second = q.val
            if first <= second:
                m.next = ListNode(first)
                m = m.next
                p = p.next
            # 如果p和q相等，也执行
            if first >= second:
                m.next = ListNode(second)
                m = m.next
                q = q.next
        # 如果p和q还未空，直接拼接
        if p is not None:
            m.next = ListNode(p.val)
            m = m.next
            m.next = p.next
        elif q is not None:
            m.next = ListNode(q.val)
            m = m.next
            m.next = q.next
        return newListNode.next


# 解法2 直接链表相连，使用自定义sort（）方法
# 需要类排序，类比较

# 第一组
listNode1 = ListNode(1)
listNode1.next = ListNode(2)
listNode1.next.next = ListNode(4)
listNode2 = ListNode(1)
listNode2.next = ListNode(3)
listNode2.next.next = ListNode(4)

# 第二组
listNode3 = ListNode(1)
listNode3.next = ListNode(7)
listNode3.next.next = ListNode(10)
listNode3.next.next.next = ListNode(44)
listNode3.next.next.next.next = ListNode(100)
listNode4 = ListNode(2)
listNode4.next = ListNode(3)
listNode4.next.next = ListNode(4)

# 第二组
listNode5 = None
listNode6 = ListNode(0)

solution = Solution()
inputArr = [
    (listNode1, listNode2),
    (listNode3, listNode4),
    (listNode5, listNode6)
]
for one in inputArr:
    start = solution.mergeTwoLists(one[0], one[1])
    print("[", end="")
    while start:
        print(start.val, end=",")
        start = start.next
    print("]")
