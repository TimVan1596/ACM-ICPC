# -*- coding:utf-8 -*-
# @Time:2021/9/7 21:15
# @Author:TimVan
# @File:102. 二叉树的层序遍历.py
# @Software:PyCharm

# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
# 示例：
# 二叉树：[3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层序遍历结果：
#
# [
#   [3],
#   [9,20],
#   [15,7]
# ]


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []

        ret = []
        prev = [root]
        rear = []
        cache = []
        # print(root.val)
        while len(prev) > 0:
            p = prev.pop(0)
            cache.append(p.val)
            if p.left is not None:
                rear.append(p.left)
            if p.right is not None:
                rear.append(p.right)
            if len(prev) <= 0:
                ret.append(cache)
                cache = []
                prev = rear
                rear = []
        return ret


if __name__ == '__main__':
    treeNode1 = TreeNode(3)
    treeNode2 = TreeNode(9)
    treeNode3 = TreeNode(20)
    treeNode4 = TreeNode(15)
    treeNode5 = TreeNode(7)
    treeNode1.left = treeNode2
    treeNode1.right = treeNode3
    treeNode3.left = treeNode4
    treeNode3.right = treeNode5

    solution = Solution()
    print(solution.levelOrder(treeNode1))
