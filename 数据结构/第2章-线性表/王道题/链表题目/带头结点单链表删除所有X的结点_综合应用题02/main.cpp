#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//�ڴ�ͷ���ĵ�����L�У�ɾ������ֵΪX�Ľ�㣬
//���ͷ���ռ䣬����ֵΪX�Ľ�㲻Ψһ���Ա�д�㷨��ʵ����������
int main(int argc, char** argv) {

	LinkedList<int> list;
	const int LEN = 7;
	int arr[LEN] = {2,4,8,16,2,32,2};
	for(int i = 0 ; i < LEN ; ++i) {
		list.insert(i,arr[i]);
	}

	selectAll(list);

	list.deleteByElement(2);
	selectAll(list);

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
