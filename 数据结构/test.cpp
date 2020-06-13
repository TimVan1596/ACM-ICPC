#include<iostream>
#include<cmath>
using namespace std;


int main() {

	for(int n = 10 ; n <2000 ; n += 20) {
		int y=0;
		int x= n; //n>1
		while(x >= (y+1)*(y+1)) {
			y++;
		}
		cout<<" "<<n<<" "<<y<<"--"<<sqrt(n)<<endl;
	}

}

