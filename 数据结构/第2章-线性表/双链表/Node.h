#ifndef NODE_H
#define NODE_H

#include <iostream>
using namespace std;

template<typename T>
class DoubleLinkedList;

template<typename T>
class Node
{
	private:
		Node<T> *previous;
		Node<T> *next;
		T element;
		friend class DoubleLinkedList<T>;
	public:
		Node()
		{
			this->next = NULL;
			this->element = 0;
		}

		Node(T _element,Node<T> *_previous,Node<T> *_next)
		{
			this->previous = _previous;
			this->next = _next;
			this->element = _element;
		}

};

#endif
