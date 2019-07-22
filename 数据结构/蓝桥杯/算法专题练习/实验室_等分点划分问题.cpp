#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;

int lenof_spilit_num =0;
int spilit_num[1000] = {0};

int findSplitNum(int m,int max) {
	for(int i = max ; i < m ; ++i) {
		if(m%i == 0) {
			spilit_num[lenof_spilit_num++]=i;
		}
	}
}

int main() {

	int score[10000] = {0};
	int sum =0,lenof_score = 0;
	lenof_score = sizeof(score)/sizeof(int);

	cin>>lenof_score;
	for(int i = 0 ; i <lenof_score; ++i) {
		int cache = 0;
		cin>>cache;
		score[i] =cache;
	}

	int max = 0;
	for(int i = 0 ; i < lenof_score ; ++i) {
		sum +=score[i];
		if(score[i]>max) {
			max = score[i];
		}
	}
	findSplitNum(sum,max);


	for(int i_spilit_num = lenof_spilit_num-1 ; i_spilit_num >= 0 ; --i_spilit_num) {
		int split =  sum/spilit_num[i_spilit_num];
		int _split_num=0;
		int sum   = 0;
		for(int i = 0 ; i < lenof_score ; ++i) {
			sum +=score[i];
			if(sum==spilit_num[i_spilit_num]) {
				sum = 0;
				_split_num++;
			}
		}
		if(_split_num == split) {
			cout<<_split_num<<endl;
			break;
		}
	}
	cin>>sum; 
	return 0;
}
