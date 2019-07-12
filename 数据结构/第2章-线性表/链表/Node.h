#ifndef NODE_H
#define NODE_H

template<typename T>
class LinkedList;

template<typename T>
class Node {
	private:
		Node<T> *next;
		T element;
		friend class LinkedList<T>;
	public:
		Node() {

		}
		Node(T _element,Node<T> *_next) {
			this->next = _next;
			this->element = _element;
		}
};

#endif
