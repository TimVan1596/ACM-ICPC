#include <iostream>

#include "LinkedQueue.h"
using namespace std;

int main(int argc, char** argv) {

	const int LEN = 7;
	LinkedQueue<int> queue;

//
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
	queue.deQueue(element);
	cout<<" queue.deQueue(element) = "<< element<<endl;
	queue.selectAll();


	return 0;
}
