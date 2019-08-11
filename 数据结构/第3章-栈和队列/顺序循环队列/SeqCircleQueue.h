#ifndef SEQCIRCLESTACK_H
#define SEQCIRCLESTACK_H

#include<iostream>
#include "Queue.h"
using namespace std;

//À≥–Ú—≠ª∑’ª
template<typename T>
class SeqCircleQueue: public Queue<T> {
	private:
		int front,rear;
		int maxSize;
		T *arr;

		static const int EMPTY_LEN;
	public:

		SeqCircleQueue(int size) {
			maxSize = size;
			front = rear = EMPTY_LEN;
			arr = new T[maxSize];
		}
		bool isEmpty() const;
		bool isFull() const;
		bool getHead(T &element) const;
		bool enQueue(T element);
		bool deQueue(T &element);
		bool clear();
};

template<typename T>
bool SeqCircleQueue<T>::isEmpty() const {

	return true;
}

template<typename T>
bool SeqCircleQueue<T>::isFull() const {

	return true;
}

template<typename T>
bool SeqCircleQueue<T>::getHead(T &element) const {

	return true;
}

template<typename T>
bool SeqCircleQueue<T>::enQueue(T element)  {

	return true;
}

template<typename T>
bool SeqCircleQueue<T>::deQueue(T& element)  {

	return true;
}

template<typename T>
bool SeqCircleQueue<T>::clear() {

	return true;
}

template<typename T>
const int SeqCircleQueue<T>::EMPTY_LEN = -1;
#endif
