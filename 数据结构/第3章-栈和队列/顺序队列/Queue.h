#ifndef QUEUE_H
#define QUEUE_H

//∂”¡–-–È¿‡ 
template<typename T>
class Queue {
	public:
		virtual bool isEmpty() const = 0;
		virtual bool isFull() const = 0;
		virtual bool getHead(T &element) const = 0;
		virtual bool enQueue(T element) const = 0;
		virtual bool deQueue(T &element) const = 0;
		virtual bool clear() const = 0;
};

#endif
