#ifndef SEQQUEUE_H
#define SEQQUEUE_H

template<typename T>
class SeqQueue {
	private:
		//队头 和 队尾
		int front , rear;
		int maxSize;
		T *arr;
	public:
		SeqQueue(int size) {
			maxSize = size;
			arr = new T[size];
		}
		bool isEmpty() const;
		bool isFull() const ;
		bool getHead(T &element) const;
		bool enQueue(T element) const;
		bool deQueue(T &element) const;
		bool clear() const;
};

template<typename T>
bool SeqQueue<T>::isEmpty() const {
	return true;
}

template<typename T>
bool isFull() const {
	return true;
}
template<typename T>
bool getHead(T &element) const {
	return true;
}

template<typename T>
bool enQueue(T element) const {
	return true;
}

template<typename T>
bool deQueue(T &element) const {
	return true;
}

template<typename T>
bool clear() const {
	return true;
}

#endif
