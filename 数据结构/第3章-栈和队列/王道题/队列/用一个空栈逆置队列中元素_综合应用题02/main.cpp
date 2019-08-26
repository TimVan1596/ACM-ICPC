#include <iostream>

#include "SeqCircleQueue.h"
#include "SeqStack.h"
using namespace std;

/* 已知Q是一个非空队列,S是一个空栈。
仅用队列和栈的操作编写一个算法,将队列Q中的所有元素逆置。 */
int main(int argc, char** argv) {

	const int LEN = 5;
	string element;
	SeqCircleQueue<string> queue(LEN);
	SeqStack<string> stack(LEN);

	//进队数据
	cout<<"queue.enQueue(Jack,Pony,Tim,Jobs,Bill)"<<endl;
	string arr[LEN] = {"Jack","Pony","Tim","Jobs","Bill"};
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue((arr[i]));
	}

	//出队数据直接进栈
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
