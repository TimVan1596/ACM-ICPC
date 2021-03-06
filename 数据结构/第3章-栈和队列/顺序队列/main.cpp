#include <iostream>

#include "SeqQueue.h"
using namespace std;

int main(int argc, char** argv) {

	const int LEN = 5;
	SeqQueue<int> queue(LEN);

	cout<<"SeqQueue isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(arr[i]);
	}

	int element = 0;
	queue.getHead(element);
	cout<<" getHead = "<<element <<endl;

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	while(!queue.isEmpty()) {
		queue.deQueue(element);
		cout<<" deQueue = "<<element <<endl;

	}

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	queue.enQueue(1024);
	queue.clear();

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	int arr2[7] = {13,2,8,20,19,8,11};
	for(int i = 0 ; i < 7 ; ++i) {
		queue.enQueue(arr2[i]);
	}

	while(!queue.isEmpty()) {
		queue.deQueue(element);
		cout<<" deQueue = "<<element <<endl;

	}


	return 0;
}
