#ifndef LINKEDSTACK_H
#define LINKEDSTACK_H

#include <iostream>

#include "Stack.h"
#include "LinkedList.h"
using namespace std;

//����ͷ������ʽջ
template<typename T>
class LinkedStack:public Stack<T> {
	private:
		LinkedList<T> list;
		//ָ��ջ��
		int topIndex;

		static const int EMPTY_LEN;
	public:
		LinkedStack() {
			topIndex = EMPTY_LEN;
		}

		bool isEmpty() const {
			return (topIndex == EMPTY_LEN);
		}
		bool isFull() const {
			return false;
		}
		//����ջ��Ԫ��
		bool top(T &x) const;
		//��ջ������Ԫ��
		bool push(T x);
		//����ջ��Ԫ��
		bool pop(T& element);
		bool clear();
};

template<typename T>
bool LinkedStack<T>::top(T &x) const {
	if(isEmpty()) {
		cout<<"[ERROR] SeqStack is Empty "<<endl;
		return false;
	}
	list.select(0,x);

	return true;
}

template<typename T>
bool LinkedStack<T>::push(T x) {
	if(isFull()) {
		cout<<"[ERROR] SeqStack is Full "<<endl;
		return false;
	}
	list.insert(0,x);
	topIndex++;
	return true;
}

template<typename T>
bool LinkedStack<T>::pop(T& element) {
	if(isEmpty()) {
		cout<<"[ERROR] SeqStack is Empty "<<endl;
		return false;
	}
	list.deleteByIndex(0,element);
	topIndex--;
	return true;
}

template<typename T>
bool LinkedStack<T>::clear() {
	return true;
}

template<typename T>
const int LinkedStack<T>::EMPTY_LEN = -1;
#endif
