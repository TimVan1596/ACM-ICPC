#include <iostream>

#include "TagCircleQueue.h"
using namespace std;

//如果希望循环队列中的元素都能得到利用，则需要设置一个标志域tag
//并以tag的值为0或1来区分尾指针和头指针值相同时的队列状态是“空”还是“满”。
//试编写与此结构相应的入队列和出队列的算法。
int main(int argc, char** argv) {

	const int LEN = 7;
	TagCircleQueue<int> queue(5);

	cout<<"TagCircleQueue:"<<endl<<"isEmpty = "<< queue.isEmpty()<<endl;

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
	queue.selectAll();


	cout<<"queue.clear()"<<endl;
	queue.clear();
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;


//	cout<<"queue.enQueue(13,2,8)"<<endl;
//	int arr2[3] = {13,2,8};
//	for(int i = 0 ; i < 3 ; ++i) {
//		queue.enQueue(arr2[i]);
//	}

	return 0;
}
