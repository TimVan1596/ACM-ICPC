#ifndef SEQQUEUE_H
#define SEQQUEUE_H

#include <iostream>
#include "Queue.h"
using namespace std;

template<typename T>
class SeqQueue {
	private:
		//队头 和 队尾
		int front , rear;
		int maxSize;
		T *arr;

		static const int EMPTY_LEN;
	public:
		SeqQueue(int size) {
			maxSize = size;
			arr = new T[size];

			front = EMPTY_LEN;
			rear = EMPTY_LEN;
		}
		//是否为空
		bool isEmpty() const {
			return rear == EMPTY_LEN;
		}
		//是否已满
		bool isFull() const {
			return rear == maxSize;
		}
		bool getHead(T &element) const;
		bool enQueue(T element);
		bool deQueue(T &element);
		bool clear();
};

template<typename T>
bool SeqQueue<T>::getHead(T &element) const {
	if(isEmpty()) {
		cout<<"[ERROR] SeqQueue is Empty "<<endl;
		return false;
	}

	element = arr[rear];
	return true;
}

template<typename T>
bool SeqQueue<T>::enQueue(T element)  {
	if(isFull()) {
		cout<<"[ERROR] SeqQueue is Full "<<endl;
		return false;
	}

	for(int i = rear+1 ; i > 0 ; --i) {
		arr[i] = arr[i-1];
	}

	arr[0] = element;
	rear++;

	return true;
}

template<typename T>
bool SeqQueue<T>::deQueue(T &element)  {
	if(isEmpty()) {
		cout<<"[ERROR] SeqQueue is Empty "<<endl;
		return false;
	}
	
	rear--;	
	return true;
}

template<typename T>
bool SeqQueue<T>::clear() {
	rear = EMPTY_LEN;
	return true;
}

template<typename T>
const int SeqQueue<T>::EMPTY_LEN = -1;
#endif
