#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;

//从编码全0开始生成。
//当产生第奇数个数时，只把当前数字最末位改变（0变1，1变0）
//当产生第偶数个数时，先找到最右边的一个1，把它左边的数字改变。
//用这个规则产生的4位格雷码序列如下：
//0000
//0001
//0011
//0010
//0110

void show(int a,int n)
{
	int i;
	int msk = 1;
	for(i=0; i<n-1; i++) msk = msk << 1;
	for(i=0; i<n; i++){
		printf((a & msk)? "1" : "0");
		msk = msk >> 1;
	}
	printf("\n");
}

void f(int n)
{
	int i;
	int num = 1;
	for(i=0; i<n; i++){
		num = num<<1;
		
		//cout<<"i="<<i<<",num="<<num<<endl;
	} 

	int a = 0;
	for(i=0; i<num; i++){
		show(a,n);

		if(i%2==0){
			a = a ^ 1;
		}
		else{
			a = 0 ; //填空
		}
	}
}

int main()
{
	f(4);
	return 0;
}
