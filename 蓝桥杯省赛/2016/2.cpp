/*
	��������
ĳ����ĳ�꿪ʼÿ�궼�ٰ�һ������party������ÿ�ζ�Ҫ��Ϩ��������ͬ����������
��������������һ����Ϩ��236������
���ʣ����Ӷ����꿪ʼ������party�ģ�
����д����ʼ������party����������
ע�⣺���ύ��Ӧ����һ����������Ҫ��д�κζ�������ݻ�˵�������֡�

*/

#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;

int main() {
	for(int i = 1 ; i < 100 ; ++i) {
		int start = i;
		int cache = start;
		for(int j = i+1 ; j < 100 ; ++j) {
			cache+=j;
			if(cache == 236){
				cout<<start<<endl;
				return 0;
			}
		}
	}

//	int start = 20;
//	for(int i = 21 ; i < 100 ; ++i){
//		start += i ;
//		cout<<start<<endl;
//	}
}


