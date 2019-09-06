#include <iostream>

#include "StackedQueue.h"
using namespace std;

//利用两个栈S1，S2来模拟一个队列，已知栈的4的运算定义如下：
//Push(S,x); 元素x入栈S
//Pop(S,x); S出栈并将出栈的值赋给x
//StackEmpty(S); 判断栈是否为空
//StackOverflow(S); 判断栈是否满
//那么如何利用栈的运算实现该队列的3个运算？
//Enqueue; 将元素x入队
//Dequeue; 出队，并将出队元素存储在x中
//QueueEmpty; 判断队列是否为空
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
