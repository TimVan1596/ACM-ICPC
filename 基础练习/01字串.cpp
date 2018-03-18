#include <stdio.h>
#include <iostream>
#include <cmath>
using namespace std;
#define MODNUM 10007

const double  PI = acos(-1);

int main() {
	int a = 0,b = 0,c = 0 ,d = 0,e =0;
	for(int a = 0 ; a < 2 ; ++a) {
		for(int b = 0 ; b < 2 ; ++b) {
			for(int c = 0 ; c < 2 ; ++c) {
				for(int d = 0 ; d < 2 ; ++d) {
					for(int e = 0 ; e < 2 ; ++e) {
						if(!a) {
							printf("0");
						} else {
							printf("1");
						}
						if(!b) {
							printf("0");
						} else {
							printf("1");
						}
						if(!c) {
							printf("0");
						} else {
							printf("1");
						}
						if(!d) {
							printf("0");
						} else {
							printf("1");
						}
						if(!e) {
							printf("0\n");
						} else {
							printf("1\n");
						}
					}
				}
			}
		}
	}

	return 0;
}


