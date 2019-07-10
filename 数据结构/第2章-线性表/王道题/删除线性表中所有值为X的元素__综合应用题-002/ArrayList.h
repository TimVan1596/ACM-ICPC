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
		bool checkIndexOutOfBound(int index) const;
		//当前长度
		int currLength;


	public:
		ArrayList(int _maxLength);
		~ArrayList() {
			delete []list;
		}

		//查找
		bool select (int i, T& element) const;
		//插入
		bool insert (int i, T element);
		//删除
		bool deleteByIndex (int i, T &element);
		//更新
		bool update (int i, T element);

		int getMaxLength() const {
			return maxLength;
		}
		int getCurrLength() const {
			return currLength;
		}
		void setCurrLength(const int length) {
			this->currLength = length;
		}
		T* getList() const {
			return list;
		}
};


#endif

template<typename T>
ArrayList<T>::ArrayList(int _maxLength) {
	this->maxLength = _maxLength;
	list = new T[maxLength]();
	currLength = 0;
}

template<typename T>
bool ArrayList<T>::select (int index, T& element) const {
	if(!checkIndexOutOfBound(index)) {
		return false;
	}

	element = list[index];

	return true;
}

template<typename T>
bool ArrayList<T>::insert (int index, T element) {

//	cout<<"[DEBUG]=>{"<<endl;
//	cout<<"\t"<<"maxLength:"<<maxLength<<endl;
//	cout<<"\t"<<"currLength:"<<currLength<<endl;
//	cout<<"\t"<<"index:"<<index<<endl;
//	cout<<"\t"<<"element:"<<element<<endl;
//	cout<<"}"<<endl;

	if(!checkIndexOutOfBound(index)) {
		return false;
	}



	for(int i = currLength-1 ; i >index ;  --i) {
		list[i] = list[i-1];
	}

	list[index] = element;
	currLength++;
	return true;
}


template<typename T>
bool ArrayList<T>::deleteByIndex (int index, T& element) {


	if(!checkIndexOutOfBound(index)) {
		return false;
	}


	element = list[index];
	for(int i = index ; i < currLength-1 ;  ++i) {
		list[i] = list[i+1];
	}


	currLength--;
	return true;
}

template<typename T>
bool ArrayList<T>::update (int index, T element) {
	if(!checkIndexOutOfBound(index)) {
		return false;
	}

	list[index]=element;

	return true;
}


template<typename T>
bool ArrayList<T>::checkIndexOutOfBound(int index) const {
	if(index<0 || index > currLength) {
		cout<<"[ERROR]=> i is out of bound"<<endl;
		return false;
	}
	if(index > maxLength-1) {
		cout<<"[ERROR]=> ArrayList space is not enough "<<endl;
		return false;
	}
	return true;
}

