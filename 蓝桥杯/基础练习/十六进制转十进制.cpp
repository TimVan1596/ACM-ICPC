#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
using namespace std;

#define TRANSNUM 16


int print16To10(char num) {
	if(num>='A' && num <='F') {
		//printf("%c",num-10+'A');
		return num-'A'+10;
	} else {
		//printf("%d",num);
		return num-'0';
	}
}

int main() {


	string s;
	cin>>s;

	int c = 0;
	long long result = 0;
	int length = s.size();
	
	for(int i = length-1;i>=0;--i){
		//cout<<s[i];
		result += print16To10(s[i])*pow(16,c);
		c++;
	}
	
//	while(!s.empty()) {
//
//		result += print16To10(s.top())*pow(16,c);
//		printf("%d * pow(16,%d) = %lf\n",print16To10(s.top()),c,pow(16,c));
//		c++;
//		s.pop();
//	}

	cout<<result;


//	int cache_n = n;
//	int c = 0,result =0;
//	while(n>0) {
//
//		n /= 10;
//	}


	return 0;
}


