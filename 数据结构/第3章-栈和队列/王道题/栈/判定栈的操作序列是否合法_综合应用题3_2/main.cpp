#include <iostream>

#include "SeqStack.h"
using namespace std;

//������I��O�ֱ��ʾ��ջ�ͳ�ջ������ջ�ĳ�̬����̬��Ϊ�գ�
//��ջ�ͳ�ջ�Ĳ������пɱ�ʾΪ����I��O��ɵ�����
//�ƿ��Բ���������Ϊ�Ϸ����У������Ϊ�Ƿ����С�
//  (1)������ʾ����������Щ�ǺϷ���
//  A��IOIIOIOO  B��IOOIOIIO  C��IIIOIOIO D��IIIOOIOO
//  (2)ͨ����(1)�ķ�����д��һ���㷨���ж������Ĳ��������Ƿ�Ϸ���
//���Ϸ�������true�����򷵻�false(�ٶ����ж��Ĳ��������Ѵ���һά������)��
int main(int argc, char** argv) {

	const int LEN = 5;
	SeqStack<int> seqStack(LEN);

	cout<<"seqStack isEmpty = "<< seqStack.isEmpty()<<endl;
	cout<<" isFull = "<< seqStack.isFull()<<endl;

	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i) {
		seqStack.push(arr[i]);
	}

	int element = 0;
	seqStack.top(element);
	cout<<" top = "<<element <<endl;

	cout<<" isEmpty = "<< seqStack.isEmpty()<<endl;
	cout<<" isFull = "<< seqStack.isFull()<<endl;

	while(!seqStack.isEmpty()) {
		seqStack.pop(element);
		cout<<" pop = "<<element <<endl;

	}

	cout<<" isEmpty = "<< seqStack.isEmpty()<<endl;
	cout<<" isFull = "<< seqStack.isFull()<<endl;

	seqStack.push(1024);
	seqStack.clear();

	cout<<" isEmpty = "<< seqStack.isEmpty()<<endl;
	cout<<" isFull = "<< seqStack.isFull()<<endl;


	return 0;
}
