#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <iostream>
#include "LinearList.h"
#include "Node.h"
using namespace std;

template<typename T>
class LinkedList:public LinearList<T> {

	private:
		Node<T> *head;
		bool checkIndexOutOfBound(int index) const;

	public:
		LinkedList();
		~LinkedList();

		//查找
		bool select (int i, T& element) const = 0;
		//插入
		bool insert (int i, T element) = 0;
		//删除
		bool deleteByIndex (int i, T &element)= 0;
		//更新
		bool update (int i, T element) = 0;


};
#endif

template<typename T>
LinkedList<T>::LinkedList() {
	head = NULL;
	this->currLength = 0;
	cout<<"currLength="<<this->currLength<<endl;
}

template<typename T>
LinkedList<T>::~LinkedList() {
	Node<T> *p;
	while(head) {
		p = head->next;
		delete head;
		head = p;
	}
}


template<typename T>
bool LinkedList<T>::select (int i, T& element) const {
	if(checkIndexOutOfBound(i)) {
		return false;
	}

	Node<T> *p = head;
	int index = 0;
	while(p) {
		if(index==i){
			element = p.Node();
			break;
		}
		p = p->next;
		index++;
	}

	return true;
}

template<typename T>
bool LinkedList<T>::insert (int i, T element) {

	if(checkIndexOutOfBound(i)) {
		return false;
	}

	Node<T> *p = head;
	int current = 0;
	while(p) {
		if(current == i) {
			break;
		}
		p = p->head;
		current++;
	}


	Node<T> *node = new Node<T>(element,p);
	p = node;

	this->currLength++;
	return true;
}

template<typename T>
bool LinkedList<T>::deleteByIndex (int i, T& element) {
	return true;
}

template<typename T>
bool LinkedList<T>::update (int i, T element) {
	return true;
}


template<typename T>
bool LinkedList<T>::checkIndexOutOfBound(int index) const {
	if(index<0 || index > currLength) {
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}
	return true;
}
