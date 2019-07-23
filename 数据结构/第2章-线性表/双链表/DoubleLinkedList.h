#ifndef DOUBLELINKEDLIST_H
#define DOUBLELINKEDLIST_H

#include <iostream>
#include "LinearList.h"
#include "Node.h"
using namespace std;

/** 双向循环链表 */
template<typename T>
class DoubleLinkedList:public LinearList<T> {
	private:
		Node<T> *head;
		bool checkIndexOutOfBound(int index) const;

	public:
		DoubleLinkedList();
		//拷贝构造函数
		DoubleLinkedList(const DoubleLinkedList &c);
		~DoubleLinkedList();

		//查找
		bool select (int i, T& element) const;
		//逆向查找
		bool reverseSelect (int i, T& element) const;
		//插入
		bool insert (int i, T element);
		//头插
		void insertHead (T element);
		//尾插
		void insertEnd (T element);
		//删除
		bool deleteByIndex (int i, T &element);
		//更新
		bool update (int i, T element);

		int getCurrLength() const {
			return this->currLength;
		}


};
#endif

template<typename T>
DoubleLinkedList<T>::DoubleLinkedList() {
	head = new Node<T>(0,NULL,NULL);
	head->next = head;
	head->previous = head;
	this->currLength = 0;
}

template<typename T>
DoubleLinkedList<T>::DoubleLinkedList(const DoubleLinkedList &c) {

	Node<T> *c_p = c.head;
	this->head = new Node<T>(c_p->element,NULL,NULL);
	head->next = head;
	head->previous = head;
	c_p = c_p->next;
	//相当于精简版的insert函数
	Node<T> *p = this->head;
	while(c_p!=c.head) {
		Node<T> *node = new Node<T>(c_p->element,p,p->next);
		p->next->previous = node;
		p->next = node;

		c_p = c_p->next;
		p = p->next;
	}
	this->currLength = c.getCurrLength();

}

template<typename T>
DoubleLinkedList<T>::~DoubleLinkedList() {


	Node<T> *p = head->next;
	while(p!=head) {
		Node<T> *next = p->next;
		delete p;
		p = next;
	}
}


template<typename T>
bool DoubleLinkedList<T>::select (int i, T& element) const {

	if(!checkIndexOutOfBound(i)) {
		return false;
	}

	int currLength = this->getCurrLength();

	Node<T> *p = NULL;
	int current = 0;
	if(i<(currLength/2)) {
		p = head->next;

		while(p) {
			if(current==i) {
				element = p->element;
				break;
			}
			p = p->next;
			current++;
		}
	} else {
		p = head->previous;
		current = this->getCurrLength()-1;
		while(p) {
			if(current==i) {
				element = p->element;
				break;
			}
			p = p->previous;
			current--;
		}
	}

	return true;
}

template<typename T>
bool DoubleLinkedList<T>::insert (int i, T element) {

	if(i<0 || i > this->currLength) {
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	int currLength = this->getCurrLength();

	Node<T> *p = head;
	int current = 0;
	if(i<(currLength/2)) {
		while(p) {

			if(current >= i) {
				break;
			}
			p = p->next;
			current++;
		}

		Node<T> *node = new Node<T>(element,p,p->next);
		p->next->previous = node;
		p->next = node;

	} else {
		current = this->getCurrLength();
		while(p) {

			if(current <= i) {
				break;
			}
			p = p->previous;
			current--;
		}

		Node<T> *node = new Node<T>(element,p->previous,p);
		p->previous->next = node;
		p->previous = node;

	}
	this->currLength++;
	return true;
}

template<typename T>
void DoubleLinkedList<T>::insertEnd ( T element) {

	Node<T> *node = new Node<T>(element,head->previous,head);
	head->previous->next = node;
	head->previous = node;

	this->currLength++;
}

template<typename T>
void DoubleLinkedList<T>::insertHead (T element) {
	Node<T> *node = new Node<T>(element,head,head->next);
	head->next->previous = node;
	head->next= node;

	this->currLength++;
}


template<typename T>
bool DoubleLinkedList<T>::deleteByIndex (int i, T& element) {
	if(!checkIndexOutOfBound(i)) {
		return false;
	}

	Node<T> *last = head;

	int currLength = this->getCurrLength();

	Node<T> *p = NULL;
	int current = 0;
	if(i<(currLength/2)) {
		p = head->next;
		while(p) {
			if(current>=i) {
				last->next = p->next;
				p->previous = p;
				element = p->element;
				delete p;
				break;
			}
			last = p;
			p = p->next;
			current++;
		}
	} else {
		p = head->previous;
		current = getCurrLength()-1;
		while(p) {
			if(current<=i) {
				last->previous = p->previous;
				p->previous->next = last;
				element = p->element;
				delete p;
				break;
			}
			last = p;
			p = p->previous;
			current--;
		}
	}



	this->currLength--;
	return true;
}

template<typename T>
bool DoubleLinkedList<T>::update (int i, T element) {
	if(!checkIndexOutOfBound(i)) {
		return false;
	}


	int currLength = this->getCurrLength();

	Node<T> *p = NULL;
	int current = 0;
	if(i<(currLength/2)) {
		p = head->next;
		while(p) {
			if(current==i) {
				p->element = element;
				break;
			}
			p = p->next;
			current++;
		}
	} else {
		p = head->previous;
		current = this->getCurrLength()-1;
		while(p) {
			if(current==i) {
				p->element = element;
				break;
			}
			p = p->previous;
			current--;
		}
	}
	return true;
}

template<typename T>
bool DoubleLinkedList<T>::checkIndexOutOfBound(int index) const {
	if(index<0 || index >= this->currLength) {
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	return true;
}



