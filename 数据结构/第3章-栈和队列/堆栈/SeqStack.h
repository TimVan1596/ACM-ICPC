#ifndef SEQSTACK_H
#define SEQSTACK_H

#include "Stack.h"

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
		SeqStack(int size){
			arr = new int[size];
			maxTop = size;
		};
		~SeqStack() {
			delete[] arr;
		}

		bool isEmpty() const {
			return topIndex == EMPTY_LEN;
		}
		bool isFull() const;
		//返回栈顶元素
		bool top(T& element) const;
		//往栈顶插入元素
		bool push(T element);
		//弹出栈顶元素
		bool pop(T& element);
		bool clear();
};

template<typename T>
bool SeqStack<T>::isFull() const {
	return false;
}

template<typename T>
bool SeqStack<T>::top(T& element) const {
	return false;
}

template<typename T>
bool SeqStack<T>::push(T element) {
	return false;
}

template<typename T>
bool SeqStack<T>::pop(T& element) {
	return false;
}

template<typename T>
bool SeqStack<T>::clear() {
	return false;
}


template<typename T>
const int SeqStack<T>::EMPTY_LEN = -1;
#endif


