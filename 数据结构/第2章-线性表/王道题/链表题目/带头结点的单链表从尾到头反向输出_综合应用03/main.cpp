#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//��LΪ��ͷ��� �ĵ�����,
//��д�㷨ʵ�ִ�β��ͷ�������ÿ������ֵ
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
