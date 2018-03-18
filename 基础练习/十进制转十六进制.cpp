#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
using namespace std;

#define TRANSNUM 16


char print10To16(int num) {
	if(num >9) {
		//printf("%c",num-10+'A');
		return num-10+'A';
	} else {
		//printf("%d",num);
		return num+'0';
	}
}

int main() {
	unsigned long n = 0;
	cin>>n;

//	for(int i = 0 ; i < 16 ; ++i) {
//		//print10To16(i);
//		printf("%c",print10To16(i));
//	}

	stack<char> output ;

	int cache_n = n;
	if(n==0) {
		printf("0");
		return 0;
	}

	while(n>0) {
		output.push(print10To16(n%TRANSNUM));
		n /= 16;
	}

	while(!output.empty()) {
		printf("%c",output.top());
		output.pop();
	}

	return 0;
}


