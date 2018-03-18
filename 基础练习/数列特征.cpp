#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
#define MODNUM 10007

int main() {
	int n = 0 , max = 0 , min = 0 ,  sum = 0;
	bool isFirst = true;
	scanf("%d",&n);

	for(int i = 0; i < n ; ++i) {
		int cache = 0;
		scanf("%d",&cache);
		if(isFirst) {
			min = max = cache;
			isFirst = false;
		} else {
			if(cache < min) min = cache;
			else if(cache > max) max = cache;
		}
		sum += cache;
	}

	cout<<max<<endl;
	cout<<min<<endl;
	cout<<sum<<endl;


	return 0;
}


