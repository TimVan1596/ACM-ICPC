#ifndef QUEUE_H
#define QUEUE_H

//∂”¡–-–È¿‡ 
template<typename T>
class Queue {
	public:
		virtual bool isEmpty() const = 0;
		virtual bool isFull() const = 0;
		virtual bool getHead(T &element) const = 0;
		virtual bool enQueue(T element)  = 0;
		virtual bool deQueue(T &element)  = 0;
		virtual bool clear() = 0;
};

#endif
