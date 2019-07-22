#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;

unsigned long long maxGY(unsigned long long a , unsigned long long b) {
	if(a>b) swap(a,b);
	int rest = b % a;
	while(rest) {
		b = a;
		a = rest;
		rest = b%a;
	}
	return a;
}

unsigned long long maxGY(unsigned long long a , unsigned long long b,unsigned long long c) {
	return maxGY(maxGY(a,b),c);
}

int main() {
	unsigned long long n = 0;
	cin>>n;

	if(n%2) {
		cout<<n*(n-1)*(n-2);
	} else {
		if(n%3) {
			cout<<n*(n-1)*(n-3);
		} else {
			cout<<(n-1)*(n-2)*(n-3);
		}
	}


	return 0;
}



