#include <iostream>

#include "X_SeqStack.h"
using namespace std;

//��������ջS1��S2��ģ��һ�����У���֪ջ��4�����㶨�����£�
//Push(S,x); Ԫ��x��ջS
//Pop(S,x); S��ջ������ջ��ֵ����x
//StackEmpty(S); �ж�ջ�Ƿ�Ϊ��
//StackOverflow(S); �ж�ջ�Ƿ���
//��ô�������ջ������ʵ�ָö��е�3�����㣿
//Enqueue; ��Ԫ��x���
//Dequeue; ���ӣ���������Ԫ�ش洢��x��
//QueueEmpty; �ж϶����Ƿ�Ϊ��
int main(int argc, char** argv) {
	const int LEN = 5;
	X_SeqStack<string> strStack(LEN);

	string strArr[LEN] = {"Jack","Pony","Tim","Jobs","Bill"};


	for(int i = 0 ; i < LEN ; ++i) {
		cout<<"i="<<i<<"-- strArr["<<strArr[i]<<"]="<<strArr[i]<<endl;
		X_SeqStack<string>::Push(strStack,strArr[i]);
	}

	string element;

	cout<<"StackOverflow = "<<X_SeqStack<string>::StackOverflow(strStack)<<endl;
	while(!X_SeqStack<string>::StackEmpty(strStack)) {
		X_SeqStack<string>::Pop(strStack,element);
		cout<<" pop = "<<element <<endl;

	}

	return 0;
}
