#include <iostream>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);
bool deleteMinElement (ArrayList<int> &list);

//��Ŀ����˳�����ɾ��������Сֵ��Ԫ�أ�����Ψһ�����ɺ������ر�ɾԪ�ص�ֵ��
//�ճ���λ�������һ��Ԫ�������˳���Ϊ������ʾ������Ϣ���˳����С�
int main(int argc, char** argv) {

	ArrayList<int> list(20);
	const int LEN = 7;
	int arr[LEN] = {14,6,20,9,7,11,1};
	for(int i = 0; i < LEN ; ++i ) {
		list.insert(i,arr[i]);
	}
	selectAll(list);

	if(!deleteMinElement(list)){
		return 1;
	}
	selectAll(list);


	return 0;
}



// ˳�����ɾ��������Сֵ��Ԫ�أ�����Ψһ��
bool deleteMinElement (ArrayList<int> &list) {
	cout<<"--- ��˳�����ɾ��������Сֵ��Ԫ�� ---"<<endl;

	int min = 0;
	int index = 0;
	if(list.select(0,min)) {
		for(int i = 0; i < list.getCurrLength() ; ++i ) {
			int element = 0;
			list.select(i,element);
			if(min>element) {
				min = element;
				index = i;
			}
		}
	} else {
		cout<<"[ERROR]=> ArrayList is NULL"<<endl;
		return false;
	}

	int element;
	list.deleteByIndex(index,element);
	cout<<"delete element = "<<element<<endl;
	list.select(list.getCurrLength()-1,element);
	list.insert(index,element);

	cout<<"--- ---"<<endl;
	return true;
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
