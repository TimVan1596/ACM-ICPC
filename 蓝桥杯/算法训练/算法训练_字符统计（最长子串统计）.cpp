#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

//����һ������Ϊn���ַ���S������һ������L��
//ͳ�Ƴ��ȴ��ڵ���L�ĳ��ִ��������Ӵ�����ͬ�ĳ��ֿ����ཻ����
//����ж���������ģ������Ȼ�ж���������һ�γ�������ġ�

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

