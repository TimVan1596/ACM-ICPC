#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//问题描述
//　　Torry从小喜爱数学。一天，老师告诉他，像2、3、5、7……这样的数叫做质数。
//	Torry突然想到一个问题，前10、100、1000、10000……个质数的乘积是多少呢？他把这个问题告诉老师。
//	老师愣住了，一时回答不出来。于是Torry求助于会编程的你，请你算出前n个质数的乘积。
//	不过，考虑到你才接触编程不久，Torry只要你算出这个数模上50000的值。
//		输入格式
//		　　仅包含一个正整数n，其中n<=100000。
//		输出格式
//		　　输出一行，即前n个质数的乘积模50000的值。
//		样例输入
//		1
//		样例输出
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


	//自然数循环
	int i = 2;
	//循环中质数的个数
	int zhiNum = 0;

	unsigned int sum = 1;
	while(zhiNum < n) {

		if(isZhi(i)) {
			zhiNum++;


			sum *=i;
			if(sum>50000) {
				sum %= 50000;
			}
//			cout<<zhiNum<<"： "<<i<<"\t sum="<<sum%50000<<endl;
		}

		i++;
	}

	cout<<sum<<endl;


	return 0;
}
