#ifndef X_SEQSTACK_H
#define X_SEQSTACK_H

#include <iostream>
#include "SeqStack.h"
using namespace std;

template<typename T>
class X_SeqStack {
	private:
		SeqStack<T> *stack;

		bool isEmpty() const{
			return stack->isEmpty();
		}

		bool isFull() const {
			return stack->isFull() ;
		}

		//ÍùÕ»¶¥²åÈëÔªËØ
		bool Push(T element) {
			if(stack->push(element)) {
				return false;
			}
			return true;
		}

		//ÍùÕ»¶¥²åÈëÔªËØ
		bool Pop(T element) {
			if(stack->pop(element)) {
				return false;
			}
			return true;
		}
	public:
		X_SeqStack(int size) {
			stack = new SeqStack<T>(size+1);
		};
		~X_SeqStack() {
			stack->clear();
			delete stack;
		}

		static bool StackEmpty(X_SeqStack<T> S) {
			return S.isEmpty();
		}
		static bool StackOverflow(X_SeqStack<T> S) {
			return S.isFull();
		}


		//ÍùÕ»¶¥²åÈëÔªËØ
		static bool Push(X_SeqStack<T> S,T element) {
			if(S.Push(element)) {
				return false;
			}
			return true;
		}
		//µ¯³öÕ»¶¥ÔªËØ
		static bool Pop(X_SeqStack<T> S,T& element) {
			if(S.Pop(element)) {
				return false;
			}
			return true;
		}

};

#endif


