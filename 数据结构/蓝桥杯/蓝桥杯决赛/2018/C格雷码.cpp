#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;

//�ӱ���ȫ0��ʼ���ɡ�
//����������������ʱ��ֻ�ѵ�ǰ������ĩλ�ı䣨0��1��1��0��
//��������ż������ʱ�����ҵ����ұߵ�һ��1��������ߵ����ָı䡣
//��������������4λ�������������£�
//0000
//0001
//0011
//0010
//0110

void show(int a,int n)
{
	int i;
	int msk = 1;
	for(i=0; i<n-1; i++) msk = msk << 1;
	for(i=0; i<n; i++){
		printf((a & msk)? "1" : "0");
		msk = msk >> 1;
	}
	printf("\n");
}

void f(int n)
{
	int i;
	int num = 1;
	for(i=0; i<n; i++){
		num = num<<1;
		
		//cout<<"i="<<i<<",num="<<num<<endl;
	} 

	int a = 0;
	for(i=0; i<num; i++){
		show(a,n);

		if(i%2==0){
			a = a ^ 1;
		}
		else{
			a = 0 ; //���
		}
	}
}

int main()
{
	f(4);
	return 0;
}
