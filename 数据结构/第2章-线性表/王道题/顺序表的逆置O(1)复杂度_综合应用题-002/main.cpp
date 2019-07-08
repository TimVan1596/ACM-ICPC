#include <iostream>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);
static void reverseList (ArrayList<int> &list);

//���һ����Ч�㷨����˳��������Ԫ�����ã�
//Ҫ���㷨�Ŀռ临�Ӷ�ΪO(1).
int main(int argc, char** argv) {
	ArrayList<int> list(10);
	const int LEN = 7;
	int arr[LEN] = {14,6,20,9,7,11,1};
	for(int i = 0; i < 2 ; ++i ) {
		list.insert(i,arr[i]);
	}
	selectAll(list);
	
	reverseList(list);
	selectAll(list);

	return 0;
}


// ��˳��������Ԫ������
static void reverseList (ArrayList<int> &list) {
	int CurrLength = list.getCurrLength();
	if(CurrLength < 2) {
		return;
	}
	int N = CurrLength/2;

	for(int i = 0; i < N ; ++i ) {
		int a  = 0;
		list.select(i,a);
		int b  = 0;
		list.select(CurrLength-i-1,b);
		list.update(i,b);
		list.update(CurrLength-i-1,a);
	}
}


// �������е�element
static void selectAll (ArrayList<int> list) {
	cout<<"ArrayList={"<<endl;
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
