#include <iostream>

#include "TagCircleQueue.h"
using namespace std;

//���ϣ��ѭ�������е�Ԫ�ض��ܵõ����ã�����Ҫ����һ����־��tag
//����tag��ֵΪ0��1������βָ���ͷָ��ֵ��ͬʱ�Ķ���״̬�ǡ��ա����ǡ�������
//�Ա�д��˽ṹ��Ӧ������кͳ����е��㷨��
int main(int argc, char** argv) {

	const int LEN = 7;
	TagCircleQueue<int> queue(5);

	cout<<"TagCircleQueue:"<<endl<<"isEmpty = "<< queue.isEmpty()<<endl;

	cout<<"queue.enQueue(2,4,8,16,32,64,128)"<<endl;
	int arr[LEN] = {2,4,8,16,32,64,128};
	for(int i = 0 ; i < LEN ; ++i) {
		queue.enQueue(arr[i]);
	}
	int element = 0;
	queue.getHead(element);
	cout<<"getHead = "<<element <<endl;
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;

	queue.selectAll();
	queue.deQueueAll();
	queue.selectAll();


	cout<<"queue.clear()"<<endl;
	queue.clear();
	cout<<" isEmpty = "<< queue.isEmpty()<<endl;


//	cout<<"queue.enQueue(13,2,8)"<<endl;
//	int arr2[3] = {13,2,8};
//	for(int i = 0 ; i < 3 ; ++i) {
//		queue.enQueue(arr2[i]);
//	}

	return 0;
}
