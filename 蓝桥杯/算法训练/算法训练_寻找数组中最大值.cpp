#include<iostream>
#include<cstdio>
using namespace std;

//��������
//�������ڸ�����������a[],Ѱ���������ֵ���������±ꡣ
//�����ʽ
//������������a[],����Ԫ�ظ���С��1����100��������ݷ������У���һ��ֻ��һ��������ʾ����Ԫ�ظ������ڶ���Ϊ����ĸ���Ԫ�ء�
//�����ʽ
//����������ֵ�������±�
//��������
//3
//3 2 1
//
//�������
//
//3 0

int main(){
	int num = 0;
	cin>>num;
	
	int max = 0, index = 0;
	for(int i = 0 ; i < num ; ++ i){
		int cache = 0;
		cin>>cache;
		if( (cache > max) || i == 0){
			max = cache;
			index = i;
		}
	
	}
	
	cout<<max<<" "<<index;
	return 0;
}
