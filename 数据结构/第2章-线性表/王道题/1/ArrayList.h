#ifndef ARRAYLIST_H
#define ARRAYLIST_H

#include <iostream>
using namespace std;

template<typename T>
class ArrayList{
	private:
		//��󳤶�
		int maxLength;
		//�洢����
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
	cout<<"���캯��"<<endl;
}

