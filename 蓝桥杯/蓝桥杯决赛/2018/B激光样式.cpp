#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;


//显然，如果只有3台机器，一共可以成5种样式，即：
//全都关上（sorry, 此时无声胜有声，这也算一种）
//开一台，共3种
//开两台，只1种

static int cnt = 0;


void print(int arr[],int start , int end);
bool check(int arr[] , int end);

//排列
void paramate(int arr[] , int start ,int end){
	
	 //cout<<"start = "<<start<<","<<"end = "<<end<<endl;
	
	if(start >=  end ){
		if(check(arr,end)){
			//print(arr,0,end);
			cnt++;
		}
		
		return;
	}


	for(int i = 0 ; i < 2 ; ++i ){
		arr[start] = i;
		paramate(arr,start+1,end);

	}
	
	
}

//打印
void print(int arr[],int start , int end){
	cout<<"arr"<<"["<<start<<","<<end<<"]"<<" =>";
	for(int i = 0 ; i < end ; ++i) {
		cout<<arr[i]<<",";
	}
	
	if(check(arr,end)){
	 	cout<<"true";
	}
	else{
		cout<<"false";
	}
	
	cout<<endl;
}

bool check(int arr[] , int end){
	
	int lastValue = 0;
	for(int i = 0 ; i < end ; ++i) {
		if(arr[i] == 1 && lastValue == 1){
			return false;
		}
		lastValue = arr[i];
	}
	
	return true;
}


int main(){
	
	int N = 30;
	int arr[N];
	
	memset(arr,-1,sizeof(arr));
	//print(arr,0,N);
	paramate(arr,0,N);
		cout<<"cnt = "<<cnt<<endl;
	


	return 0;
}
