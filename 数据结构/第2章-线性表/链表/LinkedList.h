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
		//查找全部 
		void selectAll ();
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
LinkedList<T>::LinkedList()
{
	head = new Node<T>(233,NULL);
	this->currLength = 0;
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
	
	if(!checkIndexOutOfBound(i))
	{
		return false;
	}

	Node<T> *p = head;
	int current = -1;
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
bool LinkedList<T>::insert (int i, T element)
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
	if(index<0 || index >= this->currLength)
	{
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	return true;
}

template<typename T>
void LinkedList<T>::selectAll ()
{
	cout<<"LinkedList={"<<endl;
	Node<T> *p = head->next;
	int index = 0;
	while(p)
	{
		cout<<"  "<<index<<"->"<<p->element<<endl;
		p = p->next;
		index++;
	}
	cout<<"}"<<endl;

}


