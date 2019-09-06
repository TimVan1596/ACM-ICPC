#ifndef STACK_H
#define STACK_H

template<typename T>
class Stack {
	public: 
		virtual bool isEmpty() const = 0;
		virtual bool isFull() const = 0;
		//返回栈顶元素 
		virtual bool top(T &x) const = 0;
		//往栈顶插入元素 
		virtual bool push(T x)  = 0;
		//弹出栈顶元素 
		virtual bool pop(T& element)  = 0;
		virtual bool clear()  = 0;
};

#endif
