#ifndef ARRAYLIST_H
#define ARRAYLIST_H

#include <iostream>
using namespace std;

template<typename T>
class ArrayList{
	private:
		//最大长度
		int maxLength;
		//存储数组
		T *list;

	public:
		ArrayList(int _maxLength);


};


#endif

template<typename T>
ArrayList<T>::ArrayList(int _maxLength){
//ArrayList::ArrayList(int _maxLength){

	this.maxLength = _maxLength;
	list = new T[maxLength];
	cout<<"构造函数"<<endl;
}

