#include <iostream>
#include "BinaryTree.h"
using namespace std;

//二叉树的遍历
int main(int argc, char** argv) {
	BinaryTree<char> biTree;


//	//打印根节点到叶节点的路径
//	cout<<"---- 打印叶节点的路径  -----"<<endl;
//	biTree.printTrack();
//	cout<<"---- ---- -----"<<endl<<endl;
//
//	//计算叶节点个数
//	cout<<"---- 计算叶节点个数  -----"<<endl;
//	biTree.countLeaf();
//	cout<<"---- ---- -----"<<endl<<endl;

	//计算树的高度 
	cout<<"---- 计算树的高度   -----"<<endl;
	cout<<biTree.getHeight()<<endl;
	cout<<"---- ---- -----"<<endl<<endl;

	return 0;
}
