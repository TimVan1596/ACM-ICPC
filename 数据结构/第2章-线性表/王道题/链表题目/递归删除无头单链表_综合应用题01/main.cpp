#include <iostream>
#include "NoHeadSingleLinkedList.h"
using namespace std;

//设计一个递归算法，删除不带头结点的单链表L中所有值为x的结点
int main(int argc, char** argv) {

	NoHeadSingleLinkedList<int> list;

	const int LEN = 7;
	int arr[LEN] = {2,4,8,2,16,32,2};
	for(int i = 0 ; i<LEN ; ++i) {
		list.insert(i,arr[i]);
	}
	list.selectAll();
	int element = 2;
	list.recurveDelete(element);

	list.selectAll();

	return 0;
}
