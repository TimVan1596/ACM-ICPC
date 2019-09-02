#ifndef SEQSTACK_H
#define SEQSTACK_H

#include <iostream>

#include "Stack.h"
using namespace std;

template<typename T>
class SeqStack:public Stack<T> {
	private:
		T *arr;
		//指向栈顶
		int topIndex;
		//最大容量
		int maxTop;

		static const int EMPTY_LEN;
	public:
		SeqStack(int size) {
			topIndex = EMPTY_LEN;
			maxTop = size;
			arr = new T[maxTop];

		};
		~SeqStack() {
			delete[] arr;
		}

		bool isEmpty() const {
			return topIndex == EMPTY_LEN;
		}
		bool isFull() const {
			return topIndex == maxTop;
		}
		//返回栈顶元素
		bool top(T& element) const;
		//往栈顶插入元素
		bool push(T element);
		//弹出栈顶元素
		bool pop(T& element);
		bool clear();
};

template<typename T>
bool SeqStack<T>::top(T& element) const {

	if(isEmpty()) {
		cout<<"top:[ERROR] SeqStack is Empty "<<endl;
		return false;
	}
	element = arr[topIndex];
	return true;

}

template<typename T>
bool SeqStack<T>::push(T element) {

	if(isFull()) {
		cout<<"push:[ERROR] SeqStack is Full "<<endl;
		return false;
	}


	arr[++topIndex] = element;

	return true;
}

template<typename T>
bool SeqStack<T>::pop(T& element) {

	if(isEmpty()) {
		cout<<"pop:[ERROR] SeqStack is Empty "<<endl;
		return false;
	}
	element = arr[topIndex--];
	return true;
}

template<typename T>
bool SeqStack<T>::clear() {
	topIndex = EMPTY_LEN;
	return false;
}


template<typename T>
const int SeqStack<T>::EMPTY_LEN = -1;
#endif


