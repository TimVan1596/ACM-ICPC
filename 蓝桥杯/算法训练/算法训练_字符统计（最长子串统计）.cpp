#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

//����һ������Ϊn���ַ���S������һ������L��
//ͳ�Ƴ��ȴ��ڵ���L�ĳ��ִ��������Ӵ�����ͬ�ĳ��ֿ����ཻ����
//����ж���������ģ������Ȼ�ж���������һ�γ�������ġ�

static int L;

bool comp(const pair<string,int> &a
          , const  pair<string,int> &b  ) {

	return 	a.second > b.second;
}


int main() {


//	int L = 0;
//	cin>>L;
//
//	string S;
//	cin>>S;

	string S = "bbaabbaaaaa";
	L = 4;

	string newStr;


	//�и��Ӵ�
	int max = 0;
	for(int i = 0 ; i <= S.length()-L+1; ++i) {
		for(int j = S.length()-1 ; j >= i+L-1; --j) {
			string str;
			str.assign(S,i,j-i+1);
//			cout<<str<<endl;


			int cnt = 0;
			//�ظ�����һ������
			for(int k = S.length()-1 ; k >= i+L-1; --k) {
				if(k != i) {
					string strTwo;
					strTwo.assign(S,i,j-i+1);
					if(strTwo == str) {
						cnt++;
						cout<<"cnt = "<<cnt<<endl;
					}
				}

			}

			if(cnt > max){
				max = cnt;
				newStr = str;
			}


		}

	}


	cout<<newStr<<endl;


}
