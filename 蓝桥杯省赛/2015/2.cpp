/*
比如：阿尔法炸弹2015年1月1日放置，定时为15天，则它在2015年1月16日爆炸。
有一个贝塔炸弹，2014年11月9日放置，定时为1000天，请你计算它爆炸的准确日期。
请填写该日期，格式为 yyyy-mm-dd  即4位年份2位月份2位日期。比如：2015-02-19
请严格按照格式书写。不能出现其它文字或符号。
*/
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


/*
*  					----------------------------------未完成-----------------------------------------
*/

const int months[13] = {0,31,28,31,30,31,30,31,31,30,31,30,31};

int main() {
	int year = 2014 , mon = 11 , day = 9;

	for(int i = 0 ; i < 1000 ; ++i) {

		if(day == 1 && mon == 2){
			//printf("sao ni ma");
		}

		if(year != 2016 || mon!=2) {
			if(day == months[mon]) {
				day = 1;
				if(mon == 12) {
					year++;
					mon = 1;
				} else {
					mon++;
				}
			} else {
				day++;
			//	cout<<"fuck"<<endl;
			}
		} else if(year == 2016 && mon==2) {
			if(day == months[mon]+1) {
				day = 1;
				if(mon == 12) {
					year++;
					mon = 1;
				} else {
					mon++;
				}
			} else {
				day++;
			}
		}

	//	cout<<year<<"-"<<mon<<"-"<<day<<endl;

	}
	cout<<year<<"-"<<mon<<"-"<<day<<endl;

}


