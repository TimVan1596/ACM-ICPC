#include <iostream>
#include "BinaryTree.h"
using namespace std;

//�������ı���
int main(int argc, char** argv) {
	BinaryTree<char> biTree;
//	//������� DLR
//	cout<<"---- ������� -----"<<endl;
//	BinaryTree<char>::preOrder(biTree.root);
//	cout<<"---- ---- -----"<<endl<<endl;

//	//������� LDR
//	//DBAGECHFFI
//	cout<<"---- ������� -----"<<endl;
//	BinaryTree<char>::inOrder(biTree.root);
//	cout<<"---- ---- -----"<<endl<<endl;

	//�ǵݹ�������� LDR
	//DBAGECHFFI
	cout<<"---- �ǵݹ�������� -----"<<endl;
	BinaryTree<char>::inOrderNoCircle(biTree.root);
	cout<<"---- ---- -----"<<endl<<endl;

	//��α��� 
	//ABCDEFGHI
	cout<<"---- ��α���  -----"<<endl;
	BinaryTree<char>::levelOrder(biTree.root);
	cout<<"---- ---- -----"<<endl<<endl;

	return 0;
}
