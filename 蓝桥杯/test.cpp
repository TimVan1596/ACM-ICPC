#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;
int judge (int k) {
	int i;
	for (i=2; i*i<=k; i++) {
		if (k%i==0)
			return 0;
	}
	return 1;
}
int main() {
	int n;
	int i=1;
	long long k=1;
	long long sum=1;
	scanf("%d",&n);
	while(i<=n) {
		k++;
		if (judge(k)==1) {
			i++;
			sum*=k;
			if (sum>50000) {
				sum%=50000;
			}
//			cout<<i<<"£º "<<k<"\t sum="<<sum<<endl;
			printf("%d£º %lld\t sum= %lld\n",i,k,sum);

		}
	}
	printf("%lld",sum);
}

