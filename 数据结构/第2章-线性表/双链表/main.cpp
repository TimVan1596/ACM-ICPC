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

	selectAll(dList);


	return 0;
}


static void selectAll (DoubleLinkedList<int> dList) {
	cout<<"DoubleLinkedList={"<<endl;
	int currLength = dList.getCurrLength();
	for(int i = 0 ; i < currLength; ++i ) {
		int element  = 0;
		if(i<(currLength/2)) {
			if(dList.select(i,element)) {
				cout<<"  "<<i<<"->"<<element<<endl;
			} else {
				cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
			}

		} else {
			if(dList.reverseSelect(i,element)) {
				cout<<"  "<<i<<"->"<<element<<endl;
			} else {
				cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
			}

		}
	}

	cout<<"}"<<endl;
}

