#include <iostream>

#include "X_SeqStack.h"
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
