#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//��������
//����Torry��Сϲ����ѧ��һ�죬��ʦ����������2��3��5��7����������������������
//	TorryͻȻ�뵽һ�����⣬ǰ10��100��1000��10000�����������ĳ˻��Ƕ����أ�����������������ʦ��
//	��ʦ�ס�ˣ�һʱ�ش𲻳���������Torry�����ڻ��̵��㣬�������ǰn�������ĳ˻���
//	���������ǵ���ŽӴ���̲��ã�TorryֻҪ����������ģ��50000��ֵ��
//		�����ʽ
//		����������һ��������n������n<=100000��
//		�����ʽ
//		�������һ�У���ǰn�������ĳ˻�ģ50000��ֵ��
//		��������
//		1
//		�������
//		2


bool isZhi(int num) {
	bool isZhiShu = true;


	for(int  i = 2 ;  i <= (num/2)+1 ; ++i) {
		if(num%i == 0) {
			isZhiShu = false;
			break;
		}
	}
	if(num < 2) {
		isZhiShu = false;
	}
	
	if(num == 2 ){
		isZhiShu = true;
	}

	return isZhiShu;
}


int main() {
	unsigned int n = 0;
	cin>>n;


	//��Ȼ��ѭ��
	int i = 2;
	//ѭ���������ĸ���
	int zhiNum = 0;

	unsigned int sum = 1;
	while(zhiNum < n) {

		if(isZhi(i)) {
			zhiNum++;


			sum *=i;
			if(sum>50000) {
				sum %= 50000;
			}
//			cout<<zhiNum<<"�� "<<i<<"\t sum="<<sum%50000<<endl;
		}

		i++;
	}

	cout<<sum<<endl;


	return 0;
}
