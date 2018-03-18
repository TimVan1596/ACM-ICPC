#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
#define MODNUM 10007

const double  PI = acos(-1);

int alphabet[51] = {0};

int main() {

	int n = 0 , m = 0;
	cin>>n>>m;

//	for(int i = 25-(m-1) ; i <= 25+(m-1) ; ++i) {
//		printf("%c",abs(i-25)+'a');
//	}

	for(int j = 0 ; j < n ; ++j) {
		for(int i = 25-j ; i <= 25+(m-1)-j ; ++i) {
			printf("%c",abs(i-25)+'A');
		}
		printf("\n");
	}



	return 0;
}


