/*
���磺������ը��2015��1��1�շ��ã���ʱΪ15�죬������2015��1��16�ձ�ը��
��һ������ը����2014��11��9�շ��ã���ʱΪ1000�죬�����������ը��׼ȷ���ڡ�
����д�����ڣ���ʽΪ yyyy-mm-dd  ��4λ���2λ�·�2λ���ڡ����磺2015-02-19
���ϸ��ո�ʽ��д�����ܳ����������ֻ���š�
*/
#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;


/*
*  					----------------------------------δ���-----------------------------------------
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


