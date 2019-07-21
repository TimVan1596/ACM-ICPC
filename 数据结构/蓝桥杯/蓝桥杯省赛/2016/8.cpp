/*
奖券数目
有些人很迷信数字，比如带“4”的数字，认为和“死”谐音，就觉得不吉利。
虽然这些说法纯属无稽之谈，但有时还要迎合大众的需求。某抽奖活动的奖券号码是5位数（10000-99999），
要求其中不要出现带“4”的号码，主办单位请你计算一下，如果任何两张奖券不重号，最多可发出奖券多少张。
请提交该数字（一个整数），不要写任何多余的内容或说明性文字。
*/
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


/*
*  					----------------------------------未完成-----------------------------------------
*/

int main() {
	//N为国家数
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


