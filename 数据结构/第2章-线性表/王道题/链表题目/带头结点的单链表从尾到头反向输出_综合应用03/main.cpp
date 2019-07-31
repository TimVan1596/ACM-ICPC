#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//设L为带头结点 的单链表,
//编写算法实现从尾到头反向输出每个结点的值
int main(int argc, char** argv) {

	LinkedList<int> list;
	const int LEN = 5;
	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i) {
		list.insert(i,arr[i]);
	}
	selectAll(list);
	
	list.revertSelectAll();

	return 0;
}

static void selectAll (LinkedList<int> list) {
	cout<<"LinkedList={"<<endl;
	for(int i = 0 ; i < list.getCurrLength(); ++i ) {

		int element  = 0;
		if(list.select(i,element)) {
			cout<<"  "<<i<<"->"<<element<<endl;
		} else {
			cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
		}
	}
	cout<<"}"<<endl;
}
