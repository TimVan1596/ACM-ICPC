#ifndef EMPTYONESEQCIRCLEQUEUE_H
#define EMPTYONESEQCIRCLEQUEUE_H

#include<iostream>
#include "Queue.h"
using namespace std;

//牺牲一个单元的顺序循环队列
template<typename T>
class EmptyOneSeqCircleQueue: public Queue<T> {
	private:
		int front,rear;
		int maxSize;
		T *arr;

		static const int EMPTY_LEN;
	public:

		EmptyOneSeqCircleQueue(int size) {
			//注意！数组头从0开始
			maxSize = size;
			front = rear = 0;
			//头牺牲一个单元来区分队空和队满
			arr = new T[maxSize+1];
		}
		bool isEmpty() const {
			return front == rear;
		}
		bool isFull() const {
			return (rear - front) >= maxSize;
		}
		bool getHead(T &element) const;
		bool enQueue(T element);
		bool deQueue(T &element);
		bool clear() {
			front = rear = EMPTY_LEN;
		}

		void selectAll() {
			cout<<"---  arr={   ---"<<endl;

			cout<<" front = "<< front<<endl;
			cout<<" rear = "<< rear<<endl;
			cout<<" rear% = "<< rear%(maxSize+1)<<endl;

			for(int i = 0 ; i < maxSize; ++i ) {
				cout<<i<<"->"<<arr[i]<<endl;
			}
			cout<<"---  }   ---  "<<endl<<endl;
		}
};


template<typename T>
bool EmptyOneSeqCircleQueue<T>::getHead(T &element) const {
	if(isEmpty()) {
		cout<<"[ERROR] EmptyOneSeqCircleQueue is Empty "<<endl;
		return false;
	}

	element = arr[front%maxSize];

	return true;
}

template<typename T>
bool EmptyOneSeqCircleQueue<T>::enQueue(T element)  {
	if(isFull()) {
		cout<<"[ERROR] EmptyOneSeqCircleQueue is Full "<<endl;
		return false;
	}

	if(front == EMPTY_LEN) {
		front = 0;
		rear = 0;
	}

	arr[rear%(maxSize)] = element;
	rear++;

//	cout<<"{enQueue:"<<endl;
//	cout<<" element = "<< element<<endl;
//	cout<<" front = "<< front<<endl;
//	cout<<" rear = "<< rear<<endl;
//	cout<<" arr["<<(rear-1)%maxSize<<"] = "<< arr[(rear-1)%maxSize]<<endl;
//	cout<<"}"<<endl;

	return true;
}

template<typename T>
bool EmptyOneSeqCircleQueue<T>::deQueue(T& element)  {

	if(isEmpty()) {
		cout<<"[ERROR] EmptyOneSeqCircleQueue is Empty "<<endl;
		return false;
	}

	element = arr[front%maxSize];
	front++;

//	cout<<"{deQueue:"<<endl;
//	cout<<" element = "<< element<<endl;
//	cout<<" front = "<< front<<endl;
//	cout<<" rear = "<< rear<<endl;
//	cout<<"}"<<endl;

	return true;
}

template<typename T>
const int EmptyOneSeqCircleQueue<T>::EMPTY_LEN = -1;
#endif
