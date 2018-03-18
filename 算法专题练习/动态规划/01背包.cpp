#include<cstdio>
#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;
#define MAXNUM 100


int main() {
	unsigned int n = 0 , V = 0,w[MAXNUM] = {0},c[MAXNUM] = {0},dp[MAXNUM] = {0};
	cin>>n>>V;
	for(int i = 1 ; i <= n ; ++i) {
		unsigned int cache = 0;
		cin>>cache;
		w[i] =cache;
	}
	for(int i = 1 ; i <= n ; ++i) {
		unsigned int cache = 0;
		cin>>cache;
		c[i] =cache;
	}

//	for(int i = 1 ; i <= n ; ++i) {
//		for(int j = w[i] ; j <= V ; ++j) {
//			dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+c[i]);
//			printf("dp[%d][%d] = max(dp[%d-1][%d],dp[%d-1][%d-w[%d]=%d]+c[%d]=%d)=%d; \n",i,j,i,j,i,j,i,w[i],i,c[i],dp[i][j]);
//		}
//	}

	for(int i = 1 ; i <= n ; ++i) {
		for(int j = V ; j >= w[i] ; --j) {
			dp[j] = max(dp[j],dp[j-w[i]]+c[i]);
			printf("dp[%d] = max(dp[%d],dp[%d-w[%d]=%d]+c[%d]=%d) = %d; \n",j,j,j,i,w[i],i,c[i],dp[j]);
		}
	}

	cout<<dp[V];



}
