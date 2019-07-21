#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int rest[100] = {0};

#define MODNUM 10007
#define MIN 30

//取斐波那契数列 
int fibonacci(int n) {

	if(n==3) {
		return 2;
	} else if (n ==2) {
		return 1;
	} else if (n ==1) {
		return 1;
	}

	return fibonacci(n-2)+fibonacci(n-1);
}
//取之前的余数 
int getRest(int N) {
	if(N <= MIN) {
		return rest[N];
	} else {
		return getRest(N-1)+getRest(N-2);
	}
}


int main() {
	memset(rest,0,sizeof(rest));
	int a = 1,b = 1,N=0;
	scanf("%d",&N);

	for(int i = 1 ; i <= MIN ; ++i) {
		rest[i] = fibonacci(i)%MODNUM;
	}

	printf("%d\n",getRest(N)%MODNUM);  //若余数小于100007输出 


	return 0;
}
