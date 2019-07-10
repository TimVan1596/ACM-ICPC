#ifndef LINEARLIST_H
#define LINEARLIST_H

template<typename T>
class LinearList {
	protected:
		//��ǰ����
		int currLength;
	public:
		//����
		virtual bool select (int i, T& element) const = 0;
		//����
		virtual bool insert (int i, T element) = 0;
		//ɾ��
		virtual bool deleteByIndex (int i, T &element)= 0;
		//����
		virtual bool update (int i, T element) = 0;

};

#endif
