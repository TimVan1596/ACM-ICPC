#ifndef ALGQUEUE_H
#define ALGQUEUE_H

#include "VNode.h"
#include <iostream>

using namespace std;

//邻接表专用队列
//循环队列(牺牲一个单位)
class ALGQueue {
	private:
		int maxSize;
		//循环数组
		VNode *data;
		int front;
		int rear;
	public:
		ALGQueue(int _maxSize) {
			maxSize = _maxSize;
			data = new VNode[maxSize];
			front = 0;
			rear = 0;
		}
		bool enQueue(VNode vnode) {
			bool isSuccess = true;

			if(!isFull()) {
				data[rear] = vnode;
				rear = (rear+1)%(maxSize);
			} else {
				isSuccess = false;
			}
			return isSuccess;
		}

		VNode* deQueue() {
			VNode *vnode;

			if(!isEmpty()) {
				vnode = new VNode();
				vnode->data = data[front].data;
				vnode->first = data[front].first;
				front = (front+1)%(maxSize);
			}else{
				vnode = NULL;
			} 

			return vnode;
		}

		bool isEmpty() {
			return front == rear;
		}
		bool isFull() {
//			cout<<"(rear+1)%(maxSize) = "<<(rear+1)%(maxSize)<<endl;
//			cout<<"front = "<<front<<endl;
//			cout<<"rear = "<<rear<<endl;
//			cout<<"maxSize = "<<maxSize<<endl;
			return (rear+1)%(maxSize) == front;
		}
};

#endif
