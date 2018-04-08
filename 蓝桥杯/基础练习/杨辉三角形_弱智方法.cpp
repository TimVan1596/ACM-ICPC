#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

unsigned long long A[35][35] = {0};


int main() {
	int n = 0;
	cin>>n;

	for(int i = 0 ; i < n ; ++i) {
		A[i][0] = 1;
		A[i][i] = 1;

		for(int j = 1 ; j <= i-1 ; ++j) {
			A[i][j] = A[i-1][j-1]+A[i-1][j];
		}
	}

	for(int i = 0 ; i < n ; ++i) {
		for(int j = 0 ; j < i+1 ; ++j) {
			cout<<A[i][j]<<" ";
		}
		cout<<endl;
	}

	return 0;
}


