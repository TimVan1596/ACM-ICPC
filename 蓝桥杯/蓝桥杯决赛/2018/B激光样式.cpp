#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cstring>
using namespace std;


//��Ȼ�����ֻ��3̨������һ�����Գ�5����ʽ������
//ȫ�����ϣ�sorry, ��ʱ����ʤ��������Ҳ��һ�֣�
//��һ̨����3��
//����̨��ֻ1��

static int cnt = 0;


void print(int arr[],int start , int end);
bool check(int arr[] , int end);

//����
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

//��ӡ
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
