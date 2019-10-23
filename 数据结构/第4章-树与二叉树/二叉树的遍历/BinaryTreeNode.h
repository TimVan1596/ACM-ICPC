#ifndef BINARYTREENODE_H
#define BINARYTREENODE_H

#include <iostream>
using namespace std;

template<typename T>
class BinaryTreeNode {
	private:
	public:


		BinaryTreeNode(T _data,
		               BinaryTreeNode *_lChild,
		               BinaryTreeNode *_rChild) {
			data = _data;
			lChild = _lChild;
			rChild = _rChild;
		}

		BinaryTreeNode(T _data) {
			data = _data;
			lChild = NULL;
			rChild = NULL;
		}

		//设置结点的左右孩子结点指针
		void setLeftChild(BinaryTreeNode *_lChild) {
			lChild = _lChild;
		}

		void setRightChild(BinaryTreeNode *_rChild) {
			rChild = _rChild;
		}

		T data;
		//左右孩子指针
		BinaryTreeNode *lChild;
		BinaryTreeNode *rChild;
};

#endif
