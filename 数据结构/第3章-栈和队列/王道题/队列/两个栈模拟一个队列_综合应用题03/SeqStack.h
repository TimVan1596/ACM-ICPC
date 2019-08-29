#ifndef SEQSTACK_H
#define SEQSTACK_H

#include <iostream>

#include "Stack.h"
using namespace std;

template<typename T>
class SeqStack:public Stack<T> {
	private:
		T *arr;
		//ָ��ջ��
		int topIndex;
		//�������
		int maxTop;

		static const int EMPTY_LEN;
	public:

		T* getArr() const {
			return arr;
		};
		int getTopIndex() const {
			return topIndex;
		}
		int getMaxTop() const {
			return maxTop;
		}

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
		//����ջ��Ԫ��
		bool top(T& element) const;
		//��ջ������Ԫ��
		bool push(T element);
		//����ջ��Ԫ��
		bool pop(T& element);
		bool clear();

		void selectAll() {
			cout<<"-----  selectAll  -----"<<endl;
			cout<<"topIndex = "<<topIndex<<endl;
			cout<<"maxTop = "<<maxTop<<endl;
			cout<<"SeqStacks={"<<endl;
			for(int i = 0 ; i <= topIndex; ++i ) {
				cout<<"  "<<i<<"->"<<arr[i]<<endl;

			}
			cout<<"}"<<endl;
			cout<<"--------  -------"<<endl;
		}
};

template<typename T>
bool SeqStack<T>::top(T& element) const {

	if(isEmpty()) {
		cout<<"[ERROR] SeqStack is Empty "<<endl;
		return false;
	}
	element = arr[topIndex];
	return true;

}

template<typename T>
bool SeqStack<T>::push(T element) {
	if(isFull()) {
		cout<<"[ERROR] SeqStack is Full "<<endl;
		return false;
	}

	arr[++topIndex] = element;
	return true;
}

template<typename T>
bool SeqStack<T>::pop(T& element) {

	if(isEmpty()) {
		cout<<"[ERROR] SeqStack is Empty "<<endl;
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


