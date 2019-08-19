#ifndef LINKEDQUEUE_H
#define LINKEDQUEUE_H

#include<iostream>

#include "Queue.h"
#include "Node.h"
using namespace std;

template<typename T>
class LinkedQueue: public Queue<T> {
	private:
		//使用带头结点、尾结点的链表
		Node<T> *head;
		Node<T> *rear;
	public:
		LinkedQueue() {
			int size = 0;
			head = new Node<T>(size,NULL);
			rear = head;
		}
		bool isEmpty() const {
			return head->next == NULL;
		}
		bool isFull() const {
			return false;
		}
		bool getHead(T &element) const;
		bool enQueue(T element);
		bool deQueue(T &element);
		bool clear();

		void selectAll() {
			cout<<"---  Node={   ---"<<endl;

			if(head->next) {
				cout<<" head->next->e = "<< head->next->element<<endl;
			} else {
				cout<<" head->next->e = NULL"<<endl;

			}
			cout<<" rear->e = "<< rear->element<<endl;

			Node<T> *p = head->next;
			int i = 0;
			while(p) {
				cout<<i++<<"->"<<p->element<<endl;
				p = p->next;
			}

			cout<<"---  }   ---  "<<endl<<endl;
		}

		void deQueueAll() {
			cout<<"*****  deQueueAll ={   *****"<<endl;
			int element = 0, i = 0;
			while(!this->isEmpty()) {
				this->deQueue(element);
				cout<<i++<<"->"<<element <<endl;
			}
			cout<<"*****  }   *****"<<endl<<endl;
		}
};

template<typename T>
bool LinkedQueue<T>::getHead(T &element) const {
	if(isEmpty()) {
		cout<<"[ERROR] SeqQueue is Empty "<<endl;
		return false;
	}

	element = head->next->element;
	return true;
}

template<typename T>
bool LinkedQueue<T>::enQueue(T element) {

	if(head->next) {
		Node<T> *node = new Node<T>(element,rear->next);
		rear->next = node;
		rear = node;
	} else {
		Node<T> *node = new Node<T>(element,head->next);
		head->next = node;
		rear = node;
	}

	//进入队列使用链表尾插


	return true;
}

template<typename T>
bool LinkedQueue<T>::deQueue(T &element) {
	if(isEmpty()) {
		cout<<"deQueue:[ERROR] SeqQueue is Empty "<<endl;
		return false;
	}

	element = head->next->element;
	Node<T> *temp = head->next;
	head->next = head->next->next;
	delete temp;

	if(!rear) {
		rear = head;
	}

	return true;
}

template<typename T>
bool LinkedQueue<T>::clear() {

	Node<T> *p = head->next;
	int i = 0;
	while(p) {
		Node<T> *temp = p->next;
		delete p;
		p = p->next;
	}

	head->next = NULL;
	rear = head;

	return true;
}

#endif
