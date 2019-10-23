#ifndef BINARYTREE_H
#define BINARYTREE_H

#include "BinaryTreeNode.h"
using namespace std;

template<typename T>
class BinaryTree {
	private:

	public:
		BinaryTreeNode<T>* root;
		BinaryTree() {
			tempGenerateBinaryTree();
		}

		//先(根)序遍历 DLR
		static void preOrder(BinaryTreeNode<T> *root) {

			if(root != NULL) {
				visit(root);
				preOrder(root->lChild);
				preOrder(root->rChild);
			}

		}

		//中(根)序遍历 LDR
		static void inOrder(BinaryTreeNode<T> *root) {

			if(root != NULL) {
				inOrder(root->lChild);
				visit(root);
				inOrder(root->rChild);
			}

		}

		//具体对结点的访问
		static void visit(BinaryTreeNode<T> *node) {
			cout<<"node = '"<<node->data<<"'"<<endl;
		}


		void tempGenerateBinaryTree() {

			cout<<"---- 已进行默认的二叉树构造 -----"<<endl;
			//根节点的初始化
			root = new BinaryTreeNode<char>('A');

			//BC结点的初始化
			BinaryTreeNode<char> *B
			    = new BinaryTreeNode<char>('B');
			BinaryTreeNode<char> *C
			    = new BinaryTreeNode<char>('C');
			root->setLeftChild(B);
			root->setRightChild(C);

			//DEF结点的初始化
			BinaryTreeNode<char> *D
			    = new BinaryTreeNode<char>('D');
			BinaryTreeNode<char> *E
			    = new BinaryTreeNode<char>('E');
			BinaryTreeNode<char> *F
			    = new BinaryTreeNode<char>('F');
			B->setLeftChild(D);
			C->setLeftChild(E);
			C->setRightChild(F);

			//GHI结点的初始化
			BinaryTreeNode<char> *G
			    = new BinaryTreeNode<char>('G');
			BinaryTreeNode<char> *H
			    = new BinaryTreeNode<char>('H');
			BinaryTreeNode<char> *I
			    = new BinaryTreeNode<char>('I');
			E->setLeftChild(G);
			F->setLeftChild(H);
			F->setRightChild(I);


		}
};

#endif
