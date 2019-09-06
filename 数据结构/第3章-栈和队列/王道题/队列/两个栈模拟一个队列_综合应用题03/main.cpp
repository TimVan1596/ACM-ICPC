#include <iostream>

#include "StackedQueue.h"
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
	StackedQueue<string> strQueue(LEN);

	cout<<" isEmpty = "<< strQueue.QueueEmpty()<<endl;

	cout<<"strQueue.Enqueue(Jack,Pony,Tim,Jobs,Bill)"<<endl;
	string strArr[LEN] = {"Jack","Pony","Tim","Jobs","Bill"};
	for(int i = 0 ; i < LEN ; ++i) {
		strQueue.Enqueue(strArr[i]);
	}
	strQueue.Enqueue("Hello");

	string element;

	cout<<" isEmpty = "<< strQueue.QueueEmpty()<<endl;

	cout<<"---- DequeueAll ----"<<endl;
	while(!strQueue.QueueEmpty()) {
		strQueue.Dequeue(element);
		cout<<" Dequeue = "<<element <<endl;
	}
	cout<<"----  ----"<<endl;

	strQueue.Enqueue("1024");
	cout<<" strQueue.Enqueue(1024) "<<endl;
	cout<<" isEmpty = "<< strQueue.QueueEmpty()<<endl;

	cout<<"strQueue.Enqueue(13,cup,-MiB)"<<endl;
	string arr2[3] = {"13","cup","-MiB"};
	for(int i = 0 ; i < 3 ; ++i) {
		strQueue.Enqueue(arr2[i]);
	}

	strQueue.Dequeue(element);
	cout<<" strQueue.Dequeue(element) = "<< element<<endl;

	strQueue.Enqueue("2019");
	cout<<"strQueue.Enqueue(2019)"<<endl;

	cout<<"---- DequeueAll ----"<<endl;
	while(!strQueue.QueueEmpty()) {
		strQueue.Dequeue(element);
		cout<<" Dequeue = "<<element <<endl;
	}
	cout<<"----  ----"<<endl;


	return 0;
}
