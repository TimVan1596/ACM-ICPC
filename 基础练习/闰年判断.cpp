#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
#define MODNUM 10007

const double  PI = acos(-1);

bool isRun(int n){
	if((n%4==0 && n%100) || n%400 ==0 ){
		return true;
	}
	return false;
}

int main() {
	int year = 0;
	scanf("%d",&year);
	if(isRun(year)){
		printf("yes");
	}
	else{
		printf("no");
	}

	return 0;
}


