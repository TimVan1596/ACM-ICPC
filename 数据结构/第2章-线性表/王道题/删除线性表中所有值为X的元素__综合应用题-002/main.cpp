#include <iostream>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);
void deleteValue (ArrayList<int> &list , int value);
//����Ϊn��˳���L����дһ��ʱ�临�Ӷ�ΪO(n),
//�ռ临�Ӷ�ΪO(1)���㷨��
//���㷨ɾ�����Ա�������ֵΪX��Ԫ��
int main(int argc, char** argv) {

	ArrayList<int> list(10);
	const int LEN = 7;
	int arr[LEN] = {14,6,14,9,7,11,14};
	for(int i = 0; i < LEN ; ++i ) {
		list.insert(i,arr[i]);
	}
	selectAll(list);

	deleteValue(list,14);
	selectAll(list);

	return 0;
}


// ɾ�����Ա�������ֵΪX��Ԫ��
void deleteValue (ArrayList<int> &list , int value) {
	for(int i = 0 ; i < list.getCurrLength(); ++i ) {
		int element  = 0;
		if(list.select(i,element)) {
			if(element == value) {
				list.deleteByIndex(i,element);
				i--;
			}
		} else {
			cout<<i<<"->"<<"Out of Bound"<<endl;
			return;
		}
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
