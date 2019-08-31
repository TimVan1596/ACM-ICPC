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

		//QueueFull; �ж϶����Ƿ�Ϊ��
		//ԭ��S1Ϊ�գ�����S1Ϊ����S2Ϊ��ʱ������Ϊ��
		bool QueueFull() {

			if(!(X_SeqStack<T>::StackOverflow(*S1))) {
				return false;
			}

			//!ע�⣬��������������S1Ϊ��
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

		//Enqueue; ��Ԫ��x���
		//ԭ����ֱ�ӽ�x��ջS1
		bool Enqueue(T element) {
			if(QueueFull()) {
				cout<<"Enqueue:[ERROR] StackedQueue is Full "<<endl;
				return false;
			}
			X_SeqStack<T>::Push(*S1,element);
			return true;
		}
		//Dequeue; ���ӣ���������Ԫ�ش洢��x��
		//����ֱ���Ǵ�ջS2��������S2Ϊ�����S1һ����ȫ������S2
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
		//QueueEmpty; �ж϶����Ƿ�Ϊ��
		//ԭ���ж�S1��S2�Ƿ�Ϊ��
		bool QueueEmpty() {
			return (X_SeqStack<T>::StackEmpty(*S1))
			       && (X_SeqStack<T>::StackEmpty(*S2));
		}
};

#endif
