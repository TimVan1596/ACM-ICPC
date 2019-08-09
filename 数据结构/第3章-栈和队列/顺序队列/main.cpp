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
		queue.getHead(element);
		cout<<" pop = "<<element <<endl;

	}

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	queue.enQueue(1024);
	queue.clear();

	cout<<" isEmpty = "<< queue.isEmpty()<<endl;
	cout<<" isFull = "<< queue.isFull()<<endl;

	return 0;
}
