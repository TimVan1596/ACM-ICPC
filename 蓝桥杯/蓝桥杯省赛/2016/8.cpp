/*
��ȯ��Ŀ
��Щ�˺��������֣��������4�������֣���Ϊ�͡�����г�����;��ò�������
��Ȼ��Щ˵�������޻�̸֮������ʱ��Ҫӭ�ϴ��ڵ�����ĳ�齱��Ľ�ȯ������5λ����10000-99999����
Ҫ�����в�Ҫ���ִ���4���ĺ��룬���쵥λ�������һ�£�����κ����Ž�ȯ���غţ����ɷ�����ȯ�����š�
���ύ�����֣�һ������������Ҫд�κζ�������ݻ�˵�������֡�
*/
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


/*
*  					----------------------------------δ���-----------------------------------------
*/

int main() {
	//NΪ������
	//M
	int num = 0;
	cin>>num;
	int a = 0 , b = 1 , c = 2 , d = 3;

	for(int i = 0; i <= sqrt(num)+1 ; ++i) {
		a = i;
		for(int j = 0; j < sqrt(num)+1 ; ++j) {
			b = j;
			for(int k = 0; k < sqrt(num)+1 ; ++k) {
				c = k;
				for(int m = 0; m < sqrt(num)+1 ; ++m) {
					d = m;
					int cache  = i*i + j*j + k*k + m*m;
					if(cache == num) {
						printf("%d %d %d %d",i,j,k,m);
						return 0;
					}
				}
			}
		}
	}


}


