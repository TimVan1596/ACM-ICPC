/*
	生日蜡烛
某君从某年开始每年都举办一次生日party，并且每次都要吹熄与年龄相同根数的蜡烛。
现在算起来，他一共吹熄了236根蜡烛。
请问，他从多少岁开始过生日party的？
请填写他开始过生日party的年龄数。
注意：你提交的应该是一个整数，不要填写任何多余的内容或说明性文字。

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


