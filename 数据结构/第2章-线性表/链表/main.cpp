#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//链表测试
int main(int argc, char** argv) {

	LinkedList<int> list;
	const int LEN = 7;
	int arr[LEN] = {12,34,4,9,16,7,68};
//	for(int i = 0 ; i < 1 ; ++i) {
//		list.insert(i,arr[i]);
//	}

	list.insert(0,233);

	//selectAll(list);
	return 0;
}


// 查找所有的element
static void selectAll (LinkedList<int> list) {
	cout<<"LinkedList={"<<endl;
	for(int i = 0 ; i < list.getCurrLength(); ++i ) {
		int element  = 0;
		if(list.select(i,element)) {
			cout<<i<<"->"<<element<<endl;
		} else {
			cout<<i<<"->"<<"Out of Bound"<<endl;
		}
	}
	cout<<"}"<<endl;
}


