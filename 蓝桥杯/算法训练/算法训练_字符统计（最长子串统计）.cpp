#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//给定一个长度为n的字符串S，还有一个数字L，
//统计长度大于等于L的出现次数最多的子串（不同的出现可以相交），
//如果有多个，输出最长的，如果仍然有多个，输出第一次出现最早的。

int main() {


//	int L = 0;
//	cin>>L;
//
//	string S;
//	cin>>S;

	string S = "desktop";
	int L = 4;



	for(int i = L-1 ; i < S.length(); ++i) {
		string str;
		str.assign(S,i,str.length()-1);
		cout<<str<<endl;

	}




}

