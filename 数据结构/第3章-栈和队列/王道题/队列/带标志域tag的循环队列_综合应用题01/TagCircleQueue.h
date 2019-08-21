#ifndef TAGCIRCLEQUEUE_H
#define TAGCIRCLEQUEUE_H

//带标志域tag的循环队列
class TagCircleQueue {
	private:
		int front,rear;
		int maxSize;
		T *arr;

		//头、尾指针值相同时
		//tag==0 -> 队列为空 
		//tag==1 -> 队列为满 
		int tag;

		static const int EMPTY_LEN;
	public:
		TagCircleQueue(int size) {
			maxSize = size;
			front = rear = EMPTY_LEN;
			arr = new T[maxSize];
			
			tag = 0;
		}

		bool isEmpty(){
			return tag == 0;
		}
		bool isFull(){
			return tag == 1;
		}
		bool getHead(T &element);
		bool enQueue(T element) ;
		bool deQueue(T &element);
		bool clear();

};


template<typename T>
const int TagCircleQueue<T>::EMPTY_LEN = -1;
#endifi
