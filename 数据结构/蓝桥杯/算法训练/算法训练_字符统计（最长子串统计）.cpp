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

//给定一个长度为n的字符串S，还有一个数字L，
//统计长度大于等于L的出现次数最多的子串（不同的出现可以相交），
//如果有多个，输出最长的，如果仍然有多个，输出第一次出现最早的。

static int L;

bool comp(const pair<string,int> &a
          , const  pair<string,int> &b  ) {

	return 	a.second > b.second;
}


int main() {


	int L = 0;
	cin>>L;

	string S;
	cin>>S;

/*
	string S = "bbaabbaaaaa";
	L = 4;
	*/

	string newStr;

	//string a  = "bbaa";
//	string b  = "bbaa";
//	cout<<"strTwo.compare(str) = "<<a.compare(b)<<endl;
	

	//切割子串
	int max = 0;
	for(int i = 0 ; i <= S.length()-L+1; ++i) {
		for(int j = S.length()-1 ; j >= i+L-1; --j) {
			string str = S.substr(i,j-i+1);
//			cout<<str<<endl;
			int cnt = 1;
			
//			if( i==0 && j == S.length()-1){
//				cout<<"start: str = "<<str<<",cnt = "<<cnt<<endl;
//			}
			

			//重复进行一次搜索
			for(int t = 0 ; t <= S.length()-L+1; ++t) {
				for(int k = S.length()-1 ; k >= i+L-1; --k) {
					if(k != j && t!=i) {
					
						string strTwo= S.substr(t,k-t+1);
						if(strTwo.compare(str) == 0) {
							
							//cout<<"in , str ="<<str<<",strTwo="<<strTwo
//								<<",cnt = "<<cnt<<endl;
							cnt++;
						//	if( i==0 && j == S.length()-1){
	//							cout<<"in: str = "<<str<<",cnt = "<<cnt<<endl;
	//						}
				
						
							//cout<<"cnt = "<<cnt<<endl;
						}
					}

			}
			}

			

			if(cnt > max){
				max = cnt; 
				newStr = str;
			}
			
		//	cout<<"start: str = "<<str<<",cnt = "<<cnt<<endl;


		}

	}


	cout<<newStr<<endl;


}
