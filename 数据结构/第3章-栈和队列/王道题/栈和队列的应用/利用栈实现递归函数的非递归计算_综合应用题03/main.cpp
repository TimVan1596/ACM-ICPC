#include <iostream>

#include "SeqStack.h"
using namespace std;

double reCurCal(double x,int n);
double noReCurCal(double x,int n);
double stackCal(double x,int n);

/* 利用栈实现递归函数的非递归计算 */
int main(int argc, char** argv) {
	double x = 1;
	int n = 2;

	x = 1;
	n = 3;

	for(int i = 1 ; i <= 4 ; ++i) {
		if(reCurCal(i*i,i+i) == noReCurCal(i*i,i+i)) {
			cout<<i<<": x="<<i*i<<",n="<<i+i<<"->相等"<<endl;
		} else {
			cout<<i<<": x="<<i*i<<",n="<<i+i<<"->!不相等!"<<endl;

		}
	}

	return 0;
}

//递归方法
//未知数x 和 阶数n
double reCurCal(double x,int n) {
	double ret;

	if(n == 0) {
		ret = 1;
	} else if(n == 1) {
		ret = 2*x;
	} else {
		ret = 2*x*reCurCal(x,n-1)-2*(n-1)*reCurCal(x,n-2);
	}

	return ret;
}

//非递归方法
double noReCurCal(double x,int n) {
	double results[n] = {0};
	for(int i = 0 ; i <= n ; ++i) {
		if(i == 0) {
			results[i] = 1;
		} else if(i == 1) {
			results[i] = x*2;
		} else {
			results[i] = 2*x*results[i-1]-2*(i-1)*results[i-2];
		}
	}
	return results[n];
}

//栈实现非递归计算
double stackCal(double x,int n) {
	double ret;
	struct Stack {
		int no;
		double val;
	} stack[n];

	for(int i = 0 ; i <= n ; ++i) {
		stack[i].no = i;
	}
	int top = n;
	
	
	while(top--){
		
	}

	return ret;
}
