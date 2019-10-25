#include <iostream>
#include "BinaryTree.h"
using namespace std;

//二叉树的遍历
int main(int argc, char** argv) {
	BinaryTree<char> biTree;
//	//先序遍历 DLR
//	cout<<"---- 先序遍历 -----"<<endl;
//	BinaryTree<char>::preOrder(biTree.root);
//	cout<<"---- ---- -----"<<endl<<endl;

//	//中序遍历 LDR
//	cout<<"---- 中序遍历 -----"<<endl;
//	BinaryTree<char>::inOrder(biTree.root);
//	cout<<"---- ---- -----"<<endl<<endl;

	//非递归中序遍历 LDR
	cout<<"---- 非递归中序遍历 -----"<<endl;
	BinaryTree<char>::inOrderNoCircle(biTree.root);
	cout<<"---- ---- -----"<<endl<<endl;

	return 0;
}
