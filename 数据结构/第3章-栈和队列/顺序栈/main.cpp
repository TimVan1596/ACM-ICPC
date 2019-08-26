#include <iostream>

#include "SeqStack.h"
using namespace std;

int main(int argc, char** argv) {
	const int LEN = 5;
//	SeqStack<int> seqStack(LEN);
//
//	cout<<"Stack isEmpty = "<< seqStack.isEmpty()<<endl;
//	cout<<" isFull = "<< seqStack.isFull()<<endl;
//
//	int arr[LEN] = {2,4,8,16,32};
//	for(int i = 0 ; i < LEN ; ++i) {
//		cout<<" i = "<<i<<endl;
//		seqStack.push(arr[i]);
//	}
//
//	int element = 0;
//	seqStack.top(element);
//	cout<<" top = "<<element <<endl;
//
//	cout<<" isEmpty = "<< seqStack.isEmpty()<<endl;
//	cout<<" isFull = "<< seqStack.isFull()<<endl;
//
//	while(!seqStack.isEmpty()) {
//		seqStack.pop(element);
//		cout<<" pop = "<<element <<endl;
//
//	}
//
//	cout<<" isEmpty = "<< seqStack.isEmpty()<<endl;
//	cout<<" isFull = "<< seqStack.isFull()<<endl;
//
//	seqStack.push(1024);
//	seqStack.clear();
//
//	cout<<" isEmpty = "<< seqStack.isEmpty()<<endl;
//	cout<<" isFull = "<< seqStack.isFull()<<endl;

	SeqStack<string> strStack(LEN);
	string strArr[LEN] = {"Jack","Pony","Tim","Jobs","Bill"};


	for(int i = 0 ; i < LEN ; ++i) {
		cout<<"i="<<i<<"-- strArr["<<strArr[i]<<"]="<<strArr[i]<<endl;
		strStack.push(strArr[i]);
	}

	string element;

	strStack.isEmpty(); 
	while(!strStack.isEmpty()) {
		strStack.pop(element);
		cout<<" pop = "<<element <<endl;

	}

	return 0;
}
