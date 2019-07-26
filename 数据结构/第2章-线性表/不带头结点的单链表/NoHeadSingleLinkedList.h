#ifndef NOHEADSINGLELINKEDLIST_H
#define NOHEADSINGLELINKEDLIST_H

#include <iostream>
#include "LinearList.h"
#include "Node.h"
using namespace std;

//����ͷ���ĵ�����
template<typename T>
class NoHeadSingleLinkedList:public LinearList<T> {
	private:
		Node<T> *head;
		Node<T> *tail;
		bool checkIndexOutOfBound(int index) const;

	public:
		NoHeadSingleLinkedList();
		//�������캯��
		NoHeadSingleLinkedList(const NoHeadSingleLinkedList &c);
		~NoHeadSingleLinkedList();

		//����
		bool select (int i, T& element) const;
		//����
		bool insert (int i, T element);
		//ɾ��
		bool deleteByIndex (int i, T &element);
		//����
		bool update (int i, T element);

		//��˳�򷵻�һ������������Ԫ�ص�����
		T* toArray();
		//����Ԫ����
		int size() const {
			return this->currLength;
		}


};
#endif

template<typename T>
NoHeadSingleLinkedList<T>::NoHeadSingleLinkedList() {
	head = NULL;
	tail = NULL;
	this->currLength = 0;
}

template<typename T>
NoHeadSingleLinkedList<T>::NoHeadSingleLinkedList(const NoHeadSingleLinkedList &c) {

	Node<T> *c_p = c.head;
	this->head = new Node<T>(c_p->element,NULL);
	c_p = c_p->next;
	//�൱�ھ�����insert����
	Node<T> *p = this->head;
	while(c_p) {

		Node<T> *node = new Node<T>(c_p->element,p->next);
		p->next = node;

		if(c_p->next == NULL) {
			this->tail = c_p;
		}
		c_p = c_p->next;
		p = p->next;
	}

	this->currLength = c.size();
}

template<typename T>
NoHeadSingleLinkedList<T>::~NoHeadSingleLinkedList() {
	Node<T> *p = head;
	int index = 0;
	while(p) {
		Node<T> *next = p->next;
		delete p;
		p = next;
	}
}


template<typename T>
bool NoHeadSingleLinkedList<T>::select (int i, T& element) const {

	if(!checkIndexOutOfBound(i)) {
		return false;
	}
	Node<T> *p = NULL;
	if(i==this->size()-1) {
		p = tail;
		element = p->element;
	} else {
		p = head;
		int current = 0;
		while(p) {
			if(current==i) {
				element = p->element;
				break;
			}
			p = p->next;
			current++;
		}
	}


	return true;
}

template<typename T>
bool NoHeadSingleLinkedList<T>::insert (int i, T element) {

	if(i<0 || i > this->currLength) {
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	if(i==0) {
		if(head == NULL) {
			head = new Node<T>(element,NULL);
			tail = head;
		} else {
			Node<T> *node = new Node<T>(head->element,head->next);
			head = new Node<T>(element,node);
			if(i == this->currLength) {
				tail = node;
			}

		}


	} else {
		Node<int> *p =  head;
		int current = 0;

		while(p) {

			if(current >= i-1) {
				break;
			}
			p = p->next;
			current++;
		}

		Node<T> *node = new Node<T>(element,p->next);
		p->next = node;

		if(i == this->currLength) {
			tail = node;
		}

	}

//	if(this->currLength==5 && i==0) {
//		cout<<"head->element="<<head->element<<endl;
//	}
	this->currLength++;

	return true;
}

template<typename T>
bool NoHeadSingleLinkedList<T>::deleteByIndex (int i, T& element) {
	if(!checkIndexOutOfBound(i)) {
		return false;
	}

	Node<T> *p = head->next;
	Node<T> *last = head;
	int current = 0;
	while(p) {
		if(current==i) {
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
bool NoHeadSingleLinkedList<T>::update (int i, T element) {
	if(!checkIndexOutOfBound(i)) {
		return false;
	}

	Node<T> *p = head->next;
	int current = 0;
	while(p) {
		if(current==i) {
			p->element = element ;
			break;
		}
		p = p->next;
		current++;
	}
	return true;
}

template<typename T>
bool NoHeadSingleLinkedList<T>::checkIndexOutOfBound(int index) const {
	if(index<0 || index >= this->currLength) {
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}

	return true;
}

template<typename T>
T* NoHeadSingleLinkedList<T>::toArray() {
	T* t;
	return t;
}


