#ifndef NODE_H
#define NODE_H

#include "LinkedQueue.h"

template<typename T>
class LinkedQueue;

template<typename T>
class Node {
	private:
		T element;
		Node<T> *next;
	public:
		Node(T _element , Node<T> *_next){
			this->element = _element;
			this->next = _next;
		}
		friend class LinkedQueue<T>;
};

#endif
