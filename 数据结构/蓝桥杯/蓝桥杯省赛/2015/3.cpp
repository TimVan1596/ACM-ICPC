/*
�۲�����ļӷ���ʽ��
      �� �� �� ��
  +   �� �� �� ��
-------------------
   �� �� �� �� ��
���У���ͬ�ĺ��ִ�����ͬ�����֣���ͬ�ĺ��ִ���ͬ�����֡�
������д�����������������4λ���֣���Ψһ������Ҫ��д�κζ������ݡ�

	9567
+   1085
=  10652

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

	for(int a = 1 ; a <= 9 ; ++a) {
		for(int b = 0 ; b <= 9 ; ++b) {
			if(b==a) {
				continue;
			}
			for(int c = 0 ; c <= 9 ; ++c) {
				if(a==b || a==c || b==c) {
					continue;
				}
				for(int d = 0 ; d <= 9 ; ++d) {
					if(a==b || a==c || b==c || a == d || a == d || b == d || c==d ) {
						continue;
					}
					for(int e = 1 ; e <= 9 ; ++e) {
						if(a==b || a==c || b==c || a == d || a == d || b == d || c==d || a==e||b ==e || c==e ||d ==e) {
							continue;
						}
						for(int f = 0 ; f <= 9 ; ++f) {
							if(a==b || a==c || b==c || a == d || a == d || b == d || c==d || a==e||b ==e || c==e
							        ||d ==e || a==f || b==f || c==f || d==f || e==f) {
								continue;
							}
							for(int g = 0 ; g <= 9 ; ++g) {
								if(a==b || a==c || b==c || a == d || a == d || b == d || c==d || a==e||b ==e || c==e
								        ||d ==e || a==f || b==f || c==f || d==f || e==f
								        ||a==g ||b==g ||c==g ||d==g ||e==g ||f==g) {
									continue;
								}
								for(int h = 0 ; h <= 9 ; ++h) {
									if(a==b || a==c || b==c || a == d || a == d || b == d || c==d || a==e||b ==e || c==e
									  ||d ==e || a==f || b==f || c==f || d==f || e==f
									  ||a==g ||b==g ||c==g ||d==g ||e==g ||f==g
									  ||a==h ||b==h ||c==h ||d==h ||e==h ||f==h ||g==h) {
										continue;
									}


									int first = a*1000+b*100+c*10+d;
									int end = e*1000+f*100+g*10+b;
									int sum = e*10000+f*1000+c*100+b*10+h;
									if(first+end == sum) {
										cout<<a<<b<<c<<d<<endl;
										cout<<e<<f<<g<<b<<endl;
										return 0;
									}
								}
							}
						}
					}
				}
			}
		}
	}



}


