#include <iostream>

#include "SeqCircleQueue.h"
using namespace std;

int main(int argc, char** argv) {

	const int LEN = 7;
	SeqCircleQueue<int> queue(5);

	cout<<"SeqCircleQueue isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	int arr[LEN] = {2,4,8,16,32,64,128};
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

	int arr2[3] = {13,2,8};
	for(int i = 0 ; i < 3 ; ++i) {
		queue.enQueue(arr2[i]);
	}
	queue.deQueue(element);
	cout<<" queue.deQueue(element) = "<< element<<endl;
	queue.enQueue(2019);

	cout<<" queue.enQueue(2019)"<<endl;


	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(i);
	}


//	queue.selectAll();

	while(!queue.isEmpty()) {
		queue.deQueue(element);
		cout<<" deQueue = "<<element <<endl;

	}


	return 0;
}
