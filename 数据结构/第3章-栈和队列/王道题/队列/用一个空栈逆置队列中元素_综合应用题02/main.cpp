#include <iostream>

#include "SeqCircleQueue.h"
#include "SeqStack.h"
using namespace std;

/* ��֪Q��һ���ǿն���,S��һ����ջ��
���ö��к�ջ�Ĳ�����дһ���㷨,������Q�е�����Ԫ�����á� */
int main(int argc, char** argv) {

	const int LEN = 5;
	string element;
	SeqCircleQueue<string> queue(LEN);
	SeqStack<string> stack(LEN);

	//��������
	cout<<"queue.enQueue(Jack,Pony,Tim,Jobs,Bill)"<<endl;
	string arr[LEN] = {"Jack","Pony","Tim","Jobs","Bill"};
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue((arr[i]));
	}

	//��������ֱ�ӽ�ջ
	while(!queue.isEmpty()) {
		queue.deQueue(element);
		stack.push(element);
	}


	cout<<"--- stack.popAll ---- "<<endl;
	while(!stack.isEmpty()) {
		stack.pop(element);
		cout<<"pop = "<<element <<endl;
	}
	return 0;
}
