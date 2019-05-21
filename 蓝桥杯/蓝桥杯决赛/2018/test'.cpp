#include<cstdio>
#include<algorithm>
using namespace std;

int main(){
	int a = 1, b =  1 ,c = 1;

	for( ; a < 200 ; ++a){
		b = 10*a;
		for(; c < 40  ; ++c){
			int account = a + 2 * b + 5 * c;
			if(account == 200){
				cout<<a<<","<<b<<","<<c<<","<<endl;
			}
		}
	}

	return 0;
}
