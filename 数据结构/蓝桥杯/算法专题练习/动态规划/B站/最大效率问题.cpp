#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//��˳�����ÿ��ʱ�������������Լ������������ļ�ֵ
// ǰ��:ֻ�ܰ�������������

int main() {

	//����׶�
	int n = 0;
	cin>>n;
	int start[n+1] = {-1} , end[n+1] = {-1}, value[n+1] = {-1};



	for(int i = 1 ; i <= n ; ++i) {
		int scanner = 0;
		cin>>scanner;
		start[i] = scanner;

		cin>>scanner;
		end[i] = scanner;

		cin>>scanner;
		value[i] = scanner;
	}

	//����ͻ�Ŀ���ǰ������
//	int prep[n+1] = {-1,0,0,0,1,0,2,3,5};
	int prep[n+1] = {-1};
	//���perp[]����
	for(int i = 1 ; i <= n ; ++i) {

		for(int j = i-1 ; j >= 0 ; --j) {


			if( start[i] >= end[j]) {
				prep[i] = j;
				break;
			}
		}
//		cout<<"prep["<<i<<"] = "<<prep[i]<<endl;


	}



	//ѡ��ĳһ������������棨0��1��ѡ��ѡ)
	int opt[n+1] = {0};

	for(int i = 1 ; i <= n ; ++i) {

		//ǰ���ǲ�ѡ��������ѡ
		opt[i] = max( opt[i-1] , opt[prep[i]]+value[i] );

//		cout<<"opt["<<i<<"] = "<<opt[i]<<endl;

	}




	cout<<"sum = "<<opt[n]<<endl;




}

