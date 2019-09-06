#ifndef TAGCIRCLEQUEUE_H
#define TAGCIRCLEQUEUE_H

#include<iostream>
#include "Queue.h"
using namespace std;


//带标志域tag的循环队列
template<typename T>
class TagCircleQueue:public Queue<T> {
	private:
		int front,rear;
		int maxSize;
		T *arr;

		//头、尾指针值相同时
		//tag==0 -> 队列为空
		//tag==1 -> 队列为满
		int tag;

		static const int EMPTY_LEN;
	public:
		TagCircleQueue(int size) {
			maxSize = size;
			//因rear在第一次进队操作时执行 rear+1%maxSize操作
			front = 0;
			rear = 0;
			arr = new T[maxSize];

			tag = 0;
		}

		~TagCircleQueue() {
			delete[] arr;
		}

		bool isEmpty() const {
			return (front==rear) && (tag == 0);
		}
		bool isFull() const {
			return (front==rear) && (tag == 1);
		}
		bool getHead(T &element) const;
		bool enQueue(T element) ;
		bool deQueue(T &element);
		bool clear();

		void selectAll() {
			cout<<"--- SelectAll  Queue={   ---"<<endl;

			cout<<" front = "<< front<<endl;
			cout<<" rear = "<< rear<<endl;
			cout<<" tag = "<< tag<<endl;

			for(int i = 0 ; i < maxSize; ++i ) {
				cout<<i<<"->"<<arr[i]<<endl;
			}
			cout<<"---  }   ---  "<<endl<<endl;
		}

		void deQueueAll() {
			cout<<"*****  deQueueAll ={   *****"<<endl;
			int element = 0;
			while(!isEmpty()) {
				deQueue(element);
				cout<<" deQueue = "<<element <<endl;
			}
			cout<<"*****  }   *****"<<endl<<endl;
		}
};

template<typename T>
bool TagCircleQueue<T>::getHead(T &element) const {
	if(isEmpty()) {
		cout<<"getHead:[ERROR] TagCircleQueue is Empty "<<endl;
		return false;
	}

	element = arr[rear];

	return true;
}

template<typename T>
bool  TagCircleQueue<T>::enQueue(T element) {
	if(isFull()) {
		cout<<"enQueue:[ERROR] TagCircleQueue is Full "<<endl;
		return false;
	}

	arr[rear] = element;
	rear = (rear+1)%maxSize;

	if(rear == front) {
		tag = 1;
	}

	return true;
}

template<typename T>
bool TagCircleQueue<T>::deQueue(T &element) {
	if(isEmpty()) {
		cout<<"deQueue:[ERROR] TagCircleQueue is Empty "<<endl;
		return false;
	}

	element = arr[front];
	front = (front+1)%maxSize;

	if(rear == front) {
		tag = 0;
	}

	return true;
}

template<typename T>
bool TagCircleQueue<T>::clear() {

	front = 0;
	rear = 0;
	tag = 0;

	return true;
}

template<typename T>
const int TagCircleQueue<T>::EMPTY_LEN = -1;
#endif
