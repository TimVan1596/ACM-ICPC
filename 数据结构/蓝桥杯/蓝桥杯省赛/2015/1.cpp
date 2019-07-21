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


