#ifndef LINKEDQUEUE_H
#define LINKEDQUEUE_H

#include<iostream>

#include "Queue.h"
#include "Node.h"
using namespace std;

template<typename T>
class LinkedQueue: public Queue<T> {
	private:
		//使用带头结点、尾结点的链表
		Node<T> *front;
		Node<T> *rear;
	public:
		LinkedQueue() {
			int size = 0;
			front = new Node<T>(size,NULL);
			rear = front;
		}
		bool isEmpty() const {
			return front->next == NULL;
		}
		bool isFull() const {
			return false;
		}
		bool getHead(T &element) const;
		bool enQueue(T element);
		bool deQueue(T &element);
		bool clear();
};

template<typename T>
bool LinkedQueue<T>::getHead(T &element) const {
	if(isEmpty()) {
		cout<<"[ERROR] SeqQueue is Empty "<<endl;
		return false;
	}

	element = rear->element;
	return true;
}

template<typename T>
bool LinkedQueue<T>::enQueue(T element) {
//	Node<T> node = new Node<element,front->next;
//	front->next = node;

	return true;
}

template<typename T>
bool LinkedQueue<T>::deQueue(T &element) {

	return true;
}

template<typename T>
bool LinkedQueue<T>::clear() {

	return true;
}

#endif
