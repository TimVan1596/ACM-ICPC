#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
#define MODNUM 10007

const double  PI = acos(-1);

int main() {
	unsigned int r = 0;
	scanf("%d",&r); 
	double S = PI*r*r;
	printf("%.7lf",S);

	return 0;
}


