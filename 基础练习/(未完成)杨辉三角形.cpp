#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

//排序数，Cnk，n在下，k在上
unsigned long long CNK(int n , int k) {

	if(k > 0.5*n) {
		k = n-k;
	}

	if(k==0) {
		return 1;
	}

	unsigned long long fenmu = 1, fenzi = 1;
	for(int i = 1; i<=k; ++i) {
		fenzi *= n+1-i;
		fenmu *= i;
	}

	return fenzi/fenmu;

}


int main() {
	int n = 0;
	cin>>n;

	for(int i = 0 ; i < n ; ++i) {
		for(int j = 0 ; j <= i ; ++j) {

			if(j==0) cout<<CNK(i,j);
			else cout<<" "<<CNK(i,j);

		}
		if(i!=n-1 )cout<<endl;
	}

	return 0;
}


