#include <iostream>

#include "LinkedQueue.h"
using namespace std;

int main(int argc, char** argv) {

	const int LEN = 7;
	LinkedQueue<int> queue;

	cout<<"LinkedQueue:"<<endl<<"isEmpty = "<< queue.isEmpty()<<endl;

	cout<<"queue.enQueue(2,4,8,16,32,64,128)"<<endl;
	int arr[LEN] = {2,4,8,16,32,64,128};
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(arr[i]);
	}
	int element = 0;
	queue.getHead(element);
	cout<<"getHead = "<<element <<endl;
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;

	queue.selectAll();
	queue.deQueueAll();

	cout<<"queue.clear()"<<endl;
	queue.clear();
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;


	cout<<"queue.enQueue(13,2,8)"<<endl;
	int arr2[3] = {13,2,8};
	for(int i = 0 ; i < 3 ; ++i) {
		queue.enQueue(arr2[i]);
	}
//	queue.deQueue(element);
//	cout<<" queue.deQueue(element) = "<< element<<endl;
//	queue.selectAll();
//	queue.deQueueAll();

//	queue.deQueue(element);
//	cout<<" queue.deQueue(element) = "<< element<<endl;
//
//	queue.deQueue(element);
//	cout<<" queue.deQueue(element) = "<< element<<endl;
//
//	queue.deQueue(element);
//	cout<<" queue.deQueue(element) = "<< element<<endl;

//
	queue.enQueue(2019);
	cout<<"queue.enQueue(2019)"<<endl;
	queue.selectAll();
	queue.deQueueAll();

	queue.selectAll();
	cout<<"queue.enQueue(0,1,2,3,4,5,6)"<<endl;

	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(i);
	}
	queue.selectAll();
	queue.deQueueAll();

	queue.deQueue(element);
	cout<<" queue.deQueue(element) = "<< element<<endl;
	queue.selectAll();


	cout<<"queue.enQueue(0,1,4,9,16,25,36)"<<endl;
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(i*i);
	}
	queue.selectAll();

	queue.deQueue(element);
	cout<<" queue.deQueue(element) = "<< element<<endl;

	cout<<"queue.enQueue(1024)"<<endl;
	queue.enQueue(1024);
	queue.selectAll();
	queue.deQueueAll();


	return 0;
}
