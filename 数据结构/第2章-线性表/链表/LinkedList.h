#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>
#include "LinearList.h"
#include "Node.h"
using namespace std;

template<typename T>
class LinkedList:public LinearList<T>
{
	private:
		Node<T> *head;
		bool checkIndexOutOfBound(int index) const;

	public:
		LinkedList();
		~LinkedList();

		//查找
		bool select (int i, T& element) const;
		//插入
		bool insert (int i, T element);
		//删除
		bool deleteByIndex (int i, T &element);
		//更新
		bool update (int i, T element);

		int getCurrLength() const
		{
			return this->currLength;
		}

		void print()
		{
			cout<<"print"<<endl;
		}
};
#endif

template<typename T>
LinkedList<T>::LinkedList()
{
	head = NULL;
	this->currLength = 0;
	cout<<"currLength="<<this->currLength<<endl;
}

template<typename T>
LinkedList<T>::~LinkedList()
{
	Node<T> *p;
	while(head)
	{
		p = head->next;
		delete head;
		head = p;
	}
}


template<typename T>
bool LinkedList<T>::select (int i, T& element) const
{
	if(checkIndexOutOfBound(i))
	{
		return false;
	}

	Node<T> *p = head;
	int index = 0;
	while(p)
	{
		if(index==i)
		{
			element = p->element;
			break;
		}
		p = p->next;
		index++;
	}

	return true;
}

template<typename T>
bool LinkedList<T>::insert (int i, T element)
{

	if(!checkIndexOutOfBound(i))
	{
		return false;
	}

	if(currLength==i)
	{
		node = new Node<T>(element,NULL);
	}
	else
	{
		Node<int> *p;
		p = head;

		printf("p = %p\n",p);
		printf("head = %p\n",head);

//	int current = 0;
//	while(p) {
//
//		cout<<"进入while"<<endl;
//
//		if(current == i) {
//			break;
//		}
//		p = p->next;
//		current++;
//	}

		Node<T> *node = new Node<T>(element,NULL);
		cout<<"node";
		Node<T>::print(node);
		p = node;
		cout<<"p";
		Node<T>::print(p);
//	cout<<"head";
//	Node<T>::print(head);
//
//
//	if(i == 0) {
//
//		printf("p = %p\n",p);
//		printf("head = %p\n",head);
//
//		cout<<"i = 0 , p->element="<<p->element<<endl;
////		cout<<"i = 0 , head->element="<<head->element<<endl;
//	}
	}



	this->currLength++;
	return true;
}

template<typename T>
bool LinkedList<T>::deleteByIndex (int i, T& element)
{
	return true;
}

template<typename T>
bool LinkedList<T>::update (int i, T element)
{
	return true;
}

template<typename T>
bool LinkedList<T>::checkIndexOutOfBound(int index) const
{
	if(index<0 || index > this->currLength)
	{
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	return true;
}



