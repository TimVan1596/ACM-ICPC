#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
using namespace std;

int trans16To10(char num) {
	if(num>='A' && num <='F') {
		return num-'A'+10;
	} else {
		return num-'0';
	}
}

int main() {
	int n = 0;
	cin>>n;

	while(n--) {
		//s保存输入的数据，mids保存转换成二进制的字符串
		string s,mids;
		cin>>s;

		for(int i = 0; i <s.size(); ++i) {
			//将每一个16进制数转成4位二进制字符串

			switch(s[i]) {
				case '0':
					mids+="0000";
					break;
				case '1':
					mids+="0001";
					break;
				case '2':
					mids+="0010";
					break;
				case '3':
					mids+="0011";
					break;
				case '4':
					mids+="0100";
					break;
				case '5':
					mids+="0101";
					break;
				case '6':
					mids+="0110";
					break;
				case '7':
					mids+="0111";
					break;
				case '8':
					mids+="1000";
					break;
				case '9':
					mids+="1001";
					break;
				case 'A':
					mids+="1010";
					break;
				case 'B':
					mids+="1011";
					break;
				case 'C':
					mids+="1100";
					break;
				case 'D':
					mids+="1101";
					break;
				case 'E':
					mids+="1110";
					break;
				case 'F':
					mids+="1111";
					break;

			}

			//			//cache_mids作为每个16位转成2进制的中间变量字符串，防止每4位的顺序颠倒
//			string cache_mids;
//			int num = trans16To10(s[i]);
//			while(num > 0 ) {
//				char cache =  '0'+num%2;
//				//	mids+= ;
//				cache_mids =cache + cache_mids;
//				num /=2;
//			}
//
//			//补0
//			if(cache_mids.size()%4!=0) {
//				int cache_num = 4-mids.size()%4;
//				for(int j = 0 ; j < cache_num; ++j ) {
//					cache_mids = "0" + cache_mids;
//				}
//			}
//
//			mids = mids+cache_mids;

		}


		int lenth = mids.size();
//补0
		if(mids.size()%3!=0) {
			int cache_num = 3-mids.size()%3;
			for(int j = 0 ; j < cache_num; ++j ) {
				mids = "0" + mids;
			}

		}


		bool isNo1 = false; //防止出现补0
		for(int i = 0; i <mids.size();  ) {
			int num = (mids[i++]-'0')*4+(mids[i++]-'0')*2+(mids[i++]-'0');
			if(num) {
				isNo1 = true;
			}
			if(isNo1) {
				cout<<num;
			}
		}
		cout<<endl;
	}
	return 0;
}

