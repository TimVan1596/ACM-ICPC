#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;

bool cmp(const int a,const int b) {
	return a>b;
}

int main() {

	/*
		n表示序列长度。
	    m表示询问个数。
	    每行三个数l,r,K表示询问序列从左往右第l个数到第r个数中，从大往小第K大的数是哪个
	*/
	
	int n = 0 ,m = 0,l = 0 ,r = 0 ,k = 0 ;
	int serials[1500] = {0};
	cin>>n;
//	cout<<"n ="<<n<<endl;
	for(int i = 1; i <= n ; ++i) {
		cin>>serials[i];
	}

	cin>>m;
	while(m--) {
		cin>>l>>r>>k;
//	cout<<"l ="<<l<<endl;
//	cout<<"r ="<<r<<endl;
//	cout<<"k ="<<k<<endl;


		int cache_serials[1500] = {0};
		for(int i = l; i <= r ; ++i) {
			cache_serials[i] = serials[i];
		}
		sort(cache_serials+l,cache_serials+r+1,cmp);

//		for(int i = l; i <= r ; ++i) {
//			cout<<"cache_serials["<<i<<"] ="<<cache_serials[i]<<endl;
//		}
		cout<<cache_serials[l+k-1]<<endl;
	}

	return 0;
}



