#ifndef STACK_H
#define STACK_H

template<typename T>
class Stack {
	public: 
		virtual bool isEmpty() const = 0;
		virtual bool isFull() const = 0;
		//����ջ��Ԫ�� 
		virtual bool top(T &x) const = 0;
		//��ջ������Ԫ�� 
		virtual bool push(T x)  = 0;
		//����ջ��Ԫ�� 
		virtual bool pop(T& element)  = 0;
		virtual bool clear()  = 0;
};

#endif
