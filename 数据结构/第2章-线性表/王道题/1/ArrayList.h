#ifndef ARRAYLIST_H
#define ARRAYLIST_H

#include <iostream>
using namespace std;

template<typename T>
class ArrayList {
	private:
		//最大长度
		int maxLength;
		//存储数组
		T *list;


	public:
		ArrayList(int _maxLength);
		~ArrayList() {
			cout<<"析构函数"<<endl;
			delete []list;
		}

		// 查找
		bool select (int i, T& element) const;
		//插入
		bool insert (int i, T element);

		int getMaxLength() const {
			return maxLength;
		}
};


#endif

template<typename T>
ArrayList<T>::ArrayList(int _maxLength) {
	this->maxLength = _maxLength;
	list = new T[maxLength]();
	cout<<"构造函数"<<endl;
}

template<typename T>
bool ArrayList<T>::select (int index, T& element) const {
	if(checkIndexOutOfBound(index)) {
		return false;
	}
	
	element = list[index];
	
	return true;
}

template<typename T>
bool ArrayList<T>::insert (int index, T element) {

	if(checkIndexOutOfBound(index)) {
		return false;
	}


	for(int i = maxLength-1 ; i >index ;  --i) {
		list[i] = list[i-1];
	}

	list[index] = element;

	return true;
}


static bool checkIndexOutOfBound(int index) {
	if(index<0 || index >= maxLength) {
		cout<<"--- i is out of bound ---"<<endl;
		return false;
	}
	return true;
}

