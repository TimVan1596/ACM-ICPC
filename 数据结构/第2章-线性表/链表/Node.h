#ifndef NODE_H
#define NODE_H

#include <iostream>
using namespace std;

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
			cout<<"¹¹Ôìº¯Êý"<<endl;

			this->next = _next;
			this->element = _element;
		}
		static void print(Node<T> *node ) {
			cout<<"{"<<endl;
			cout<<"next:"<<node->next<<endl;
			cout<<"element:"<<node->element<<endl;
			cout<<"}"<<endl;

		}
};

#endif
