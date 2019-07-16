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
//		//拷贝构造函数
//		Node(const Node<T>& node)
//		{
//			cout<<"调用Node的拷贝构造函数"<<endl;
//			this->next = node.next;
//			this->element = node.element;
//		}
		static void print(Node<T> *node )
		{
			cout<<"{"<<endl;
			cout<<"next:"<<node->next<<endl;
			cout<<"element:"<<node->element<<endl;
			cout<<"}"<<endl;

		}
};

#endif
