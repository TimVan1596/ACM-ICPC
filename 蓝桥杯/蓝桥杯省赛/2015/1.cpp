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


int main() {
	int cnt= 0;
	for(int i = 1 ; i < 10 ; ++i) {
		if(i == 4 ) continue;
		for(int j = 0 ; j < 10 ; ++j) {
			if(j == 4 ) continue;
			for(int k = 0 ; k < 10 ; ++k) {
				if(k == 4 ) continue;
				for(int m = 0 ; m < 10 ; ++m) {
					if(m == 4 ) continue;
					for(int n = 0 ; n < 10 ; ++n) {
						if(n == 4 ) continue;
						else{
							cnt++;
						}
					}
				}
			}
		}
	}
	cout<<"cnt ="<<cnt<<endl;
}


