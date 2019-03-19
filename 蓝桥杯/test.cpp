#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//打印行列式
void printMatrix(int *matrix , int m , int n) {
	for(int i = 0; i < m ; ++i) {
		for(int j = 0 ; j < n ; ++j) {
			int cache = 0;
			cout<<*(matrix+i*n+j)<<" ";
		}
		cout<<endl;
	}

}



int main() {
	int m = 3, n = 2;
	int arr[3][2] = {
		{0,3},
		{1,2},
		{3,1},
	};
	
	printMatrix(&arr[0][0],m,n);
	
}

