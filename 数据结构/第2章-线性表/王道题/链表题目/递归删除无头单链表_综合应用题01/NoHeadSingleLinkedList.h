#ifndef NOHEADSINGLELINKEDLIST_H
#define NOHEADSINGLELINKEDLIST_H

#include <iostream>
#include "LinearList.h"
#include "Node.h"
using namespace std;

//不带头结点的单链表
template<typename T>
class NoHeadSingleLinkedList:public LinearList<T> {
	private:
		Node<T> *head;
		Node<T> *tail;
		bool checkIndexOutOfBound(int index) const;

	public:
		NoHeadSingleLinkedList();
		//拷贝构造函数
		NoHeadSingleLinkedList(const NoHeadSingleLinkedList &c);
		~NoHeadSingleLinkedList();

		//查找
		bool select (int i, T& element) const;
		//插入
		bool insert (int i, T element);
		//删除
		bool deleteByIndex (int i, T &element);
		//更新
		bool update (int i, T element);

		//以顺序返回一个包含此所有元素的数组
		T* toArray();
		//返回元素数
		int size() const {
			return this->currLength;
		}

		void print() const {
			cout<<"---------------------------------"<<endl;
			cout<<"tail->element="<<this->tail->element<<endl;
			cout<<"---------------------------------"<<endl;
		}

		void selectAll() const {
			cout<<"NoHeadSingleLinkedList={"<<endl;
			for(int i = 0 ; i < size(); ++i ) {

				int element  = 0;
				if(select(i,element)) {
					cout<<"  "<<i<<"->"<<element<<endl;
				} else {
					cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
				}
			}
			cout<<"}"<<endl;
		}

		//递归删除所有值为x的结点
		void recurveDelete(T element);
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
	int cElement = c.tail->element;
//	cout<<"c.tail->element="<<c.tail->element<<endl;
	cout<<"-----1------"<<endl;
	c.selectAll();
	cout<<"-----1------"<<endl;

//	this->head = new Node<T>(123,NULL);
	
	cout<<"-----2------"<<endl;
	c.selectAll();
	cout<<"-----2------"<<endl;
	//c.tail->element = cElement;
//	cout<<"c.tail->element="<<c.tail->element<<endl;
	c_p = c_p->next;
	//相当于精简版的insert函数
	Node<T> *p = this->head;

	while(c_p) {

		Node<T> *node = new Node<T>(c_p->element,p->next);
		p->next = node;
//		tail = p->next;

		c_p = c_p->next;
		p = p->next;
		if(!c_p) {
			tail = p;
			cout<<"this->tail->element="<<this->tail->element<<endl;
			cout<<"c.tail->element="<<c.tail->element<<endl;
			c.selectAll();
			cout<<"-----------"<<endl;
		}
	}


//	c.tail->element = cElement;
//	this->tail = new Node<T>(cElement,NULL);
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

	this->currLength++;

	return true;
}

template<typename T>
bool NoHeadSingleLinkedList<T>::deleteByIndex (int i, T& element) {
	if(!checkIndexOutOfBound(i)) {
		return false;
	}

	if(i==0) {
		element = head->element;
		if(this->currLength==1) {
			head = NULL;
			tail = NULL;
		} else {
			head = head->next;
		}


	} else {
		Node<T> *p = head->next;
		Node<T> *last = head;
		int current = 1;
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
	}
	this->currLength--;
	return true;
}

template<typename T>
bool NoHeadSingleLinkedList<T>::update (int i, T element) {

	if(!checkIndexOutOfBound(i)) {
		return false;
	}
	Node<T> *p = NULL;

	if(i==(this->size()-1)) {
		tail->element = element ;

	} else {
		p = head;
		int current = 0;
		while(p) {
			if(current==i) {
				p->element = element ;
				break;
			}
			p = p->next;
			current++;
		}
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

template<typename T>
void NoHeadSingleLinkedList<T>::recurveDelete(T element){
	cout<<"递归删除"<<endl;
}
