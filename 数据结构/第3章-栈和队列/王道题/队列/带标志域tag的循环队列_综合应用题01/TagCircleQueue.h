#ifndef TAGCIRCLEQUEUE_H
#define TAGCIRCLEQUEUE_H

//����־��tag��ѭ������
class TagCircleQueue {
	private:
		int front,rear;
		int maxSize;
		T *arr;

		//ͷ��βָ��ֵ��ͬʱ
		//tag==0 -> ����Ϊ�� 
		//tag==1 -> ����Ϊ�� 
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
