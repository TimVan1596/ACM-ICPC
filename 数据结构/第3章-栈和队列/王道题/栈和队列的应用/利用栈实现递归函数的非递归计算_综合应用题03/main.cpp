#include <iostream>

#include "SeqStack.h"
using namespace std; 

double reCurCal(double x,int n);

/* 利用栈实现递归函数的非递归计算 */
int main(int argc, char** argv) {
	double x = 1;
	int n = 3;	
	cout<<"x = "<<x<<"，n="<<n<<endl;
	cout<<"reCurCal = "<<reCurCal(x,n)<<endl;
	
	return 0;
}

//未知数x 和 阶数n 
double reCurCal(double x,int n){
	double ret;
	
	if(n == 0){
		ret = 1;
	}else if(n == 1){
		ret = 2*x;
	}else{
		ret = 2*x*reCurCal(x,n-1)-2*(n-1)*reCurCal(x,n-2);
	}
	
	return ret;
}
