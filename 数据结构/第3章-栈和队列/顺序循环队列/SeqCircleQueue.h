#ifndef SEQCIRCLESTACK_H
#define SEQCIRCLESTACK_H

#include<iostream>
#include "Queue.h"
using namespace std;

//顺序循环栈
template<typename T>
class SeqCircleQueue: public Queue<T> {
	private:
		int front,rear;
		int maxSize;
		T *arr;

		static const int EMPTY_LEN;
	public:

		SeqCircleQueue(int size) {
			//注意！数组头从0开始
			maxSize = size;
			front = rear = 0;
			arr = new T[maxSize];
		}
		bool isEmpty() const {
			return front == rear;
		}
		bool isFull() const {
			//头指针指向为空,故要多一个
			return (rear - front) >= maxSize;
		}
		bool getHead(T &element) const;
		bool enQueue(T element);
		bool deQueue(T &element);
		bool clear() {
			front = rear = 0;
		}

		void selectAll() {
			cout<<"arr={"<<endl;

			cout<<" front = "<< front<<endl;
			cout<<" rear = "<< rear<<endl;

			for(int i = 0 ; i < maxSize; ++i ) {
				cout<<i<<"->"<<arr[i]<<endl;
			}
			cout<<"}"<<endl;
		}
};


template<typename T>
bool SeqCircleQueue<T>::getHead(T &element) const {
	if(isEmpty()) {
		cout<<"[ERROR] SeqCircleQueue is Empty "<<endl;
		return false;
	}

	element = arr[front%maxSize];

	return true;
}

template<typename T>
bool SeqCircleQueue<T>::enQueue(T element)  {
	if(isFull()) {
		cout<<"[ERROR] SeqCircleQueue is Full "<<endl;
		return false;
	}

	arr[rear%(maxSize+1)] = element;
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
bool SeqCircleQueue<T>::deQueue(T& element)  {

	if(isEmpty()) {
		cout<<"[ERROR] SeqCircleQueue is Empty "<<endl;
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
const int SeqCircleQueue<T>::EMPTY_LEN = -1;
#endif
