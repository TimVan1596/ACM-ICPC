#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;

void printArray(int *arr , int n);

//函数需要接受数组及其元素个数作为参数，
//函数返回值应为删除操作执行后数组的新元素个数
int CompactIntegers(int *arr , int n){
	//定义新长度、新数组
	int currLen = n;
	int currArr[n] = {0};
	int currI = 0;

	for(int i = 0; i < n ; ++i){
		if(arr[i] != 0){
			currArr[currI] = arr[i];
			currI++;
		}
	}

	cout<<currI<<endl;
	printArray(currArr,currI);

	cout<<endl;
	return n;
}

//打印数组
void printArray(int *arr , int n){
	for(int i = 0; i < n ; ++i){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}

int main(){

	int n = 0;
	cin>>n;
	int arr[n] = {0};

	//从键盘输入
	for(int i = 0; i < n ; ++i){
		int cache = 0;
		cin>>cache;
		arr[i] = cache;
	}



	CompactIntegers(arr,n);
	return 0;
}


