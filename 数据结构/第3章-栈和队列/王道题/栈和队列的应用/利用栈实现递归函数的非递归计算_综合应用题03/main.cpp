#include <iostream>

#include "SeqStack.h"
using namespace std;

double reCurCal(double x,int n);
double noReCurCal(double x,int n);
double stackCal(double x,int n);

/* ����ջʵ�ֵݹ麯���ķǵݹ���� */
int main(int argc, char** argv) {
	double x = 1;
	int n = 2;

	x = 1;
	n = 3;

	for(int i = 1 ; i <= 4 ; ++i) {
		if(reCurCal(i*i,i+i) == noReCurCal(i*i,i+i)) {
			cout<<i<<": x="<<i*i<<",n="<<i+i<<"->���"<<endl;
		} else {
			cout<<i<<": x="<<i*i<<",n="<<i+i<<"->!�����!"<<endl;

		}
	}

	return 0;
}

//�ݹ鷽��
//δ֪��x �� ����n
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

//�ǵݹ鷽��
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

//ջʵ�ַǵݹ����
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
