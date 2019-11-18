#include<iostream>
using namespace std;

int main() {
	int k = 2;
	int j=k/2+k%2+1-(k/2)%2;
	printf("When k = %d , j = %d \n",k,j);
	k = 3;
	j=k/2+k%2+1-k/2/2;
	printf("When k = %d , j = %d \n",k,j);
	k = 7;
	j=k/2+k%2+1-k/2/2;
	printf("When k = %d , j = %d \n",k,j);
	return 0;
}
