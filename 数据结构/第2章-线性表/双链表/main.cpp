#include <iostream>
#include "DoubleLinkedList.h"
using namespace std;

static void selectAll (DoubleLinkedList<int> dList);

int main(int argc, char** argv) {
	DoubleLinkedList<int> dList;

	const int LEN = 5;
	int arr[LEN] = {2,4,8,16,32};
	for(int i = LEN-4 ; i >= 0 ; --i) {
		//Í·²å
		dList.insertHead(arr[i]);
	}
	for(int i = 2 ; i < LEN ; ++i) {
		//Î²²å
		dList.insertEnd(arr[i]);
	}

	dList.insert(0,1);
	dList.insert(4,-999);
	dList.insert(dList.getCurrLength(),64);
	//É¾³ý
	int element = 0;
	dList.deleteByIndex(0,element);
	cout<<"dList.deleteByIndex(0,element) = "<<element<<endl;
	dList.deleteByIndex(3,element);
	cout<<"dList.deleteByIndex(3,element) = "<<element<<endl;
	dList.deleteByIndex(dList.getCurrLength()-1,element);
	cout<<"dList.deleteByIndex(dList.getCurrLength()-1,element) = "<<element<<endl;
	selectAll(dList);

	dList.update(0,1);
	dList.update(2,-999);
	dList.update(dList.getCurrLength()-1,64);
	selectAll(dList);


	return 0;
}


static void selectAll (DoubleLinkedList<int> dList) {
	cout<<"DoubleLinkedList={"<<endl;
	int currLength = dList.getCurrLength();
	for(int i = 0 ; i < currLength; ++i ) {
		int element  = 0;
		if(dList.select(i,element)) {
			cout<<"  "<<i<<"->"<<element<<endl;
		} else {
			cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
		}

	}

	cout<<"}"<<endl;
}

