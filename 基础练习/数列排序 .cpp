#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;


int main() {
	int n = 0;
	cin>>n;

	int num[n] = {0};

	for(int i = 0 ; i < n; ++i) {
		cin>>num[i];
	}

	sort(num,num+n);

	for(int i = 0 ; i < n; ++i) {
		cout<<num[i]<<' ';
	}



	return 0;
}

