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

		//���ý������Һ��ӽ��ָ��
		void setLeftChild(BinaryTreeNode *_lChild) {
			lChild = _lChild;
		}

		void setRightChild(BinaryTreeNode *_rChild) {
			rChild = _rChild;
		}

		T data;
		//���Һ���ָ��
		BinaryTreeNode *lChild;
		BinaryTreeNode *rChild;
};

#endif
