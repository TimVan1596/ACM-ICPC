#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

int num[10005];

int main() {
	int n = 0;
	scanf("%d",&n);
	memset(num,0,sizeof(num));
	for(int i = 0 ; i < n; ++i ) {
		int cache;
		cin>>cache;
		num[i] = cache;
	}
	int findNum = 0;
	cin>>findNum;

//	cout<<"n="<<n<<endl;
//	cout<<"findNum="<<findNum<<endl;


	for(int i = 0 ; i < n; ++i ) {

		if(num[i] == findNum) {
			cout<<i+1;
			return 0;
		}
	}
	cout<<-1;

	return 0;
}


