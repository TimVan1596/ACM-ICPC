/*
区间不相交问题：
	给出N个开区间（x,y），从中选择 尽可能多的开区间，使得这些开区间两两没有交集
	例如开区间(1,3)、(2,4)、(3,5)、(6,7)，可以选择最多3个区间(1,3)、(3,5)、(6,7)，它们互相没有交集
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;
#define MAX_ 105



struct section {
	int x;
	int y;

} sect[MAX_];

bool cmp(const section a,const section b) {
	if(a.y!=b.y) {
		return a.y<b.y;
	} else {
		return a.x>b.x;
	}
}

int main() {

	int N = 0;
	cin>>N;

	for(int i = 0; i <N; ++i) {
		cin>>sect[i].x>>sect[i].y;
	}
	sort(sect,sect+N,cmp);



		cout<<endl;
	for(int i = 0; i <N; ++i) {
		cout<<sect[i].x<<" "<<sect[i].y<<endl;
	}


	unsigned int ans = 0,lastY =0;
	for(int i = 0; i <N; ++i) {
		if(lastY <= sect[i].x) {
			ans++;
			lastY = sect[i].y;
			printf("lastY = sect[%d].y = %d; \n",i,lastY);
		}
	}
	cout<<ans;

//	cout<<endl;
//	for(int i = 0; i <N; ++i) {
//		cout<<sect[i].x<<" "<<sect[i].y<<endl;
//	}

	return 0;
}
