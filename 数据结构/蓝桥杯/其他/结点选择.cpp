#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;


int main() {
	unsigned long long n = 0;
	cin>>n;

	int a[n] = {0};

	for(int i = 0 ; i < n ; ++i) {
		int cache = 0 ;
		cin>>cache;
		a[i] = cache;
	}

	for(int i = 0 ; i < n ; ++i) {
		cout<<a[i]<<endl;
	}



	return 0;
}



