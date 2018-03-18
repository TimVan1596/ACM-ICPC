#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;



int fun(int score[], int m, int below[]) {
	double avg = 0;
	int i = 0 ;
	for(i = 0 ; i < m ; ++i) {
		avg +=score[i];
	}
	avg/=m;
	//printf("avg = %lf\n",avg);
	int num=0;
	for( i = 0 ; i < m ; ++i) {
		if(score[i]<avg) {
			below[i] = score[i];
			num++;
		}
	}
//	printf("num = %d\n",num);
	return num;
}

int main() {

	int score[100] = {1,2,1,1,1,0,2,1,3,0};
	
	sort(score,score+10);
	
	for(int i = 0 ; i < 10 ; ++i){
		cout<<score[i]<<endl;
	}
	
	
	return 0;
}
