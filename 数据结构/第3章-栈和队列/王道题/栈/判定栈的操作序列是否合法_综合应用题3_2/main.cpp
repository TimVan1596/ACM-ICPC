#include <iostream>

#include "SeqStack.h"
using namespace std;

//假设以I和O分别表示入栈和出栈操作。栈的初态和终态均为空，
//入栈和出栈的操作序列可表示为仅由I和O组成的序列
//称可以操作的序列为合法序列，否则称为非法序列。
//  (1)下面所示的序列中哪些是合法的
//  A．IOIIOIOO  B．IOOIOIIO  C．IIIOIOIO D．IIIOOIOO
//  (2)通过对(1)的分析，写出一个算法，判定所给的操作序列是否合法。
//若合法，返回true，否则返回false(假定被判定的操作序列已存入一维数组中)。
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
