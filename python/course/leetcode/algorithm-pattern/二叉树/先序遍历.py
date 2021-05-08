# -*- coding:utf-8 -*-
# @Time:2021/5/8 13:22
# @Author:TimVan
# @File:先序遍历.py
# @Software:PyCharm

# 二叉树
class Node:
    def __init__(self, element):
        self.element = element
        self.leftNode = None
        self.rightNode = None

    def __repr__(self):
        return self.element


class BinaryTree:
    def __init__(self, element):
        self.root = Node(element)

    # 驱动函数
    def preOrderDerivativeDriver(self):
        self.preOrderDerivative(self.root)

    # 递归的先序遍历，中左右
    def preOrderDerivative(self, node):
        if node is not None:
            print(node)
            self.preOrderDerivative(node.leftNode)
            self.preOrderDerivative(node.rightNode)




#         A
#    B        C
#  D  E      F  G
myBinaryTree = BinaryTree('A')
BNode = Node('B')
CNode = Node('C')
DNode = Node('D')
ENode = Node('E')
FNode = Node('F')
GNode = Node('G')
myBinaryTree.root.leftNode = BNode
myBinaryTree.root.leftNode.leftNode = DNode
myBinaryTree.root.leftNode.rightNode = ENode
myBinaryTree.root.rightNode = CNode
myBinaryTree.root.rightNode.leftNode = FNode
myBinaryTree.root.rightNode.rightNode = GNode
myBinaryTree.preOrderDerivativeDriver()
