#include <iostream>
#include "BinaryTree.h"
using namespace std;

//�������ı���
int main(int argc, char** argv) {
	BinaryTree<char> biTree;


//	//��ӡ���ڵ㵽Ҷ�ڵ��·��
//	cout<<"---- ��ӡҶ�ڵ��·��  -----"<<endl;
//	biTree.printTrack();
//	cout<<"---- ---- -----"<<endl<<endl;
//
//	//����Ҷ�ڵ����
//	cout<<"---- ����Ҷ�ڵ����  -----"<<endl;
//	biTree.countLeaf();
//	cout<<"---- ---- -----"<<endl<<endl;

	//�������ĸ߶� 
	cout<<"---- �������ĸ߶�   -----"<<endl;
	cout<<biTree.getHeight()<<endl;
	cout<<"---- ---- -----"<<endl<<endl;

	return 0;
}
