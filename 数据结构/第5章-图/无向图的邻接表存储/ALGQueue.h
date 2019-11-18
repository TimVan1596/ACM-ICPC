#ifndef ALGQUEUE_H
#define ALGQUEUE_H

#include "VNode.h"
#include <iostream>

using namespace std;

//�ڽӱ�ר�ö���
//ѭ������(����һ����λ)
class ALGQueue {
	private:
		int maxSize;
		//ѭ������
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
