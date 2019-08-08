#include <iostream>

#include "LinkedStack.h"
using namespace std;

//Á´Ê½Õ»
int main(int argc, char** argv) {
	const int LEN = 5;
	LinkedStack<int> stack;

	cout<<"stack isEmpty = "<< stack.isEmpty()<<endl;
	cout<<" isFull = "<< stack.isFull()<<endl;

	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i) {
		stack.push(arr[i]);
	}

	int element = 0;
	stack.top(element);
	cout<<" top = "<<element <<endl;

	cout<<" isEmpty = "<< stack.isEmpty()<<endl;
	cout<<" isFull = "<< stack.isFull()<<endl;

	while(!stack.isEmpty()) {
		stack.pop(element);
		cout<<" pop = "<<element <<endl;

	}

	cout<<" isEmpty = "<< stack.isEmpty()<<endl;
	cout<<" isFull = "<< stack.isFull()<<endl;

	stack.push(1024);
	stack.clear();

	cout<<" isEmpty = "<< stack.isEmpty()<<endl;
	cout<<" isFull = "<< stack.isFull()<<endl;

	return 0;
}
