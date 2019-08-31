#ifndef STACKEDQUEUE_H
#define STACKEDQUEUE_H

#include <iostream>
#include "X_SeqStack.h"
using namespace std;

template<typename T>
class StackedQueue {
	private:
		X_SeqStack<T> *S1;
		X_SeqStack<T> *S2;

		//QueueFull; 判断队列是否为满
		//原理：S1为空，或者S1为满但S2为空时，队列为满
		bool QueueFull() {

			if(!(X_SeqStack<T>::StackOverflow(*S1))) {
				return false;
			}

			//!注意，这里隐含条件，S1为满
			if((X_SeqStack<T>::StackEmpty(*S2))) {

				while(!X_SeqStack<T>::StackEmpty(*S1)) {
					T element;
					X_SeqStack<T>::Pop(*S1,element);
					X_SeqStack<T>::Push(*S2,element);
				}
				return false;
			}

			return true;
		}
	public:
		StackedQueue(int size) {
			S1 = new X_SeqStack<T>(size);
			S2 = new X_SeqStack<T>(size);
		}
		~StackedQueue() {
			delete S1;
			delete S2;
		}

		//Enqueue; 将元素x入队
		//原理是直接将x进栈S1
		bool Enqueue(T element) {
			if(QueueFull()) {
				cout<<"Enqueue:[ERROR] StackedQueue is Full "<<endl;
				return false;
			}
			X_SeqStack<T>::Push(*S1,element);
			return true;
		}
		//Dequeue; 出队，并将出队元素存储在x中
		//理是直接是从栈S2弹出，若S2为空则从S1一次性全部进入S2
		bool Dequeue(T &element) {
			if(QueueEmpty()) {
				cout<<"Dequeue:[ERROR] StackedQueue is Empty "<<endl;
				return false;
			}

			if(X_SeqStack<T>::StackEmpty(*S2)) {
				while(!X_SeqStack<T>::StackEmpty(*S1)) {
					T element;
					X_SeqStack<T>::Pop(*S1,element);
					X_SeqStack<T>::Push(*S2,element);
				}
			}
			X_SeqStack<T>::Pop(*S2,element);
			return true;
		}
		//QueueEmpty; 判断队列是否为空
		//原理判断S1和S2是否为空
		bool QueueEmpty() {
			return (X_SeqStack<T>::StackEmpty(*S1))
			       && (X_SeqStack<T>::StackEmpty(*S2));
		}
};

#endif
