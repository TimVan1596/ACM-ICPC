#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//按顺序给出每段时间能做的任务，以及任务所带来的价值
// 前提:只能按照升序做任务

int main() {

	//输入阶段
	int n = 0;
	cin>>n;
	int start[n+1] = {-1} , end[n+1] = {-1}, value[n+1] = {-1};



	for(int i = 1 ; i <= n ; ++i) {
		int scanner = 0;
		cin>>scanner;
		start[i] = scanner;

		cin>>scanner;
		end[i] = scanner;

		cin>>scanner;
		value[i] = scanner;
	}

	//不冲突的可做前个任务
//	int prep[n+1] = {-1,0,0,0,1,0,2,3,5};
	int prep[n+1] = {-1};
	//获得perp[]数组
	for(int i = 1 ; i <= n ; ++i) {

		for(int j = i-1 ; j >= 0 ; --j) {


			if( start[i] >= end[j]) {
				prep[i] = j;
				break;
			}
		}
//		cout<<"prep["<<i<<"] = "<<prep[i]<<endl;


	}



	//选择某一任务带来的收益（0、1即选或不选)
	int opt[n+1] = {0};

	for(int i = 1 ; i <= n ; ++i) {

		//前者是不选，后者是选
		opt[i] = max( opt[i-1] , opt[prep[i]]+value[i] );

//		cout<<"opt["<<i<<"] = "<<opt[i]<<endl;

	}




	cout<<"sum = "<<opt[n]<<endl;




}

