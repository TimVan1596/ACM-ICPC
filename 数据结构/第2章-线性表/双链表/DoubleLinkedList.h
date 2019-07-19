#ifndef DOUBLELINKEDLIST_H
#define DOUBLELINKEDLIST_H

#include <iostream>
#include "LinearList.h"
#include "Node.h"
using namespace std;

template<typename T>
class DoubleDoubleLinkedList:public LinearList<T>
{
	private:
		Node<T> *head;
		bool checkIndexOutOfBound(int index) const;

	public:
		DoubleDoubleLinkedList();
		//拷贝构造函数
		DoubleDoubleLinkedList(const DoubleLinkedList &c);
		~DoubleLinkedList();

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


};
#endif

template<typename T>
DoubleLinkedList<T>::DoubleLinkedList()
{
	head = new Node<T>(0,NULL);
	this->currLength = 0;
}

template<typename T>
DoubleLinkedList<T>::DoubleLinkedList(const DoubleLinkedList &c)
{

	Node<T> *c_p = c.head;
	this->head = new Node<T>(c_p->element,NULL);
	c_p = c_p->next;
	//相当于精简版的insert函数
	Node<T> *p = this->head;
	while(c_p)
	{

		Node<T> *node = new Node<T>(c_p->element,p->next);
		p->next = node;

		c_p = c_p->next;
		p = p->next;
	}
	this->currLength = c.getCurrLength();
}

template<typename T>
DoubleLinkedList<T>::~DoubleLinkedList()
{
	Node<T> *p = head;
	int index = 0;
	while(p)
	{
		Node<T> *next = p->next;
		delete p;
		p = next;
	}
}


template<typename T>
bool DoubleLinkedList<T>::select (int i, T& element) const
{

	if(!checkIndexOutOfBound(i))
	{
		return false;
	}

	Node<T> *p = head->next;
	int current = 0;
	while(p)
	{
		if(current==i)
		{
			element = p->element;
			break;
		}
		p = p->next;
		current++;
	}

	return true;
}

template<typename T>
bool DoubleLinkedList<T>::insert (int i, T element)
{

	if(i<0 || i > this->currLength)
	{
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	Node<int> *p =  head;
	int current = 0;

	while(p)
	{

		if(current >= i)
		{
			break;
		}
		p = p->next;
		current++;
	}

	Node<T> *node = new Node<T>(element,p->next);
	p->next = node;

	this->currLength++;
	return true;
}

template<typename T>
bool DoubleLinkedList<T>::deleteByIndex (int i, T& element)
{
	if(!checkIndexOutOfBound(i))
	{
		return false;
	}

	Node<T> *p = head->next;
	Node<T> *last = head;
	int current = 0;
	while(p)
	{
		if(current==i)
		{
			last->next = p->next;
			element = p->element;
			delete p;
			break;
		}
		last = p;
		p = p->next;
		current++;
	}

	this->currLength--;
	return true;
}

template<typename T>
bool DoubleLinkedList<T>::update (int i, T element)
{
	if(!checkIndexOutOfBound(i))
	{
		return false;
	}

	Node<T> *p = head->next;
	int current = 0;
	while(p)
	{
		if(current==i)
		{
			p->element = element ;
			break;
		}
		p = p->next;
		current++;
	}
	return true;
}

template<typename T>
bool DoubleLinkedList<T>::checkIndexOutOfBound(int index) const
{
	if(index<0 || index >= this->currLength)
	{
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	return true;
}



