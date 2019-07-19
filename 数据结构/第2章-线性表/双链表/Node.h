#ifndef NODE_H
#define NODE_H

#include <iostream>
using namespace std;

template<typename T>
class LinkedList;

template<typename T>
class Node
{
	private:
		Node<T> *previous;
		Node<T> *next;
		T element;
		friend class LinkedList<T>;
	public:
		Node()
		{
			this->next = NULL;
			this->element = 0;
		}
		Node(T _element,Node<T> *_next)
		{
			this->next = _next;
			this->element = _element;
		}

};

#endif
