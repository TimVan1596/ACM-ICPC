#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

int main(){
	//int a = 1, b =  1 ,c = 1;

	//cout<<"hello"<<endl;
	//printf("hello");

	for( int a = 1 ; a < 200 ; ++a){

		for(int c = 1 ; c < 40  ; ++c){
			int account =( a + 20 * a + 5 * c);
			//cout<<a<<","<<10 * a<<","<<c<<","<<"="<<account<<endl;
			if( account == 200){
				cout<<a<<","<<10 * a<<","<<c<<","<<"="<<account<<endl;
			}
		}
	}

	return 0;
}
