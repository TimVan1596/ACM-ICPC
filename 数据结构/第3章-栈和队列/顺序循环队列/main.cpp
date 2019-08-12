#include <iostream>

#include "SeqCircleQueue.h"
using namespace std;

int main(int argc, char** argv) {

	const int LEN = 5;
	SeqCircleQueue<int> queue(LEN);

	cout<<"SeqCircleQueue isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(arr[i]);
	}

	int element = 0;
	queue.getHead(element);
	cout<<"getHead = "<<element <<endl;

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	while(!queue.isEmpty()) {
		queue.deQueue(element);
		cout<<" deQueue = "<<element <<endl;

	}

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl<<endl;

	queue.enQueue(1024);
	cout<<" queue.enQueue(1024) "<<endl;
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl<<endl;
	queue.clear();
	cout<<" queue.clear() "<<endl;
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl<<endl;

	int arr2[7] = {13,2,8,20,19,8,11};
	for(int i = 0 ; i < 7 ; ++i) {
		queue.enQueue(arr2[i]);
	}
	
	queue.selectAll();

//	while(!queue.isEmpty()) {
//		queue.deQueue(element);
//		cout<<" deQueue = "<<element <<endl;
//
//	}


	return 0;
}
