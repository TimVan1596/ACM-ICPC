#include <iostream>
#include "NoHeadSingleLinkedList.h"
using namespace std;

static void selectAll (NoHeadSingleLinkedList<int> list);

int main(int argc, char** argv) {

	NoHeadSingleLinkedList<int> list;

	const int LEN = 5;
	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i<LEN ; ++i) {
		list.insert(i,arr[i]);
	}
	list.insert(0,1);
	list.insert(4,-999);
	list.insert(list.size(),64);
	//É¾³ý
	int element = 0;
	list.deleteByIndex(0,element);
	cout<<"list.deleteByIndex(0,element) = "<<element<<endl;
	list.deleteByIndex(3,element);
	cout<<"list.deleteByIndex(3,element) = "<<element<<endl;
	list.deleteByIndex(list.size()-1,element);
	cout<<"list.deleteByIndex(list.getCurrLength()-1,element) = "<<element<<endl;
//	selectAll(list);

//	list.update(0,1);
//	list.update(2,-999);
	list.update(list.size()-1,64);
	
	selectAll(list);


	return 0;
}


static void selectAll (NoHeadSingleLinkedList<int> list) {
	cout<<"NoHeadSingleLinkedList={"<<endl;
	for(int i = 0 ; i < list.size(); ++i ) {

		int element  = 0;
		if(list.select(i,element)) {
			cout<<"  "<<i<<"->"<<element<<endl;
		} else {
			cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
		}
	}
	cout<<"}"<<endl;
}


