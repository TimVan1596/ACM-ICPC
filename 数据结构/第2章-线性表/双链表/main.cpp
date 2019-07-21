#include <iostream>
#include "DoubleLinkedList.h"
using namespace std;

int main(int argc, char** argv)
{
	DoubleLinkedList<int> dList;
	
	const int LEN = 5;
	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i)
	{
		dList.insert(i,arr[i]);
	}
	//β�� 
	dList.insertEnd(999);
	//ͷ�� 
	dList.insertHead(-188);
	dList.selectAll();
	dList.reverseSelectAll();
	 
	return 0;
}
