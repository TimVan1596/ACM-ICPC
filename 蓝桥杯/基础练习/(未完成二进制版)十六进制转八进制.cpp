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
		//s������������ݣ�mids����ת���ɶ����Ƶ��ַ��� 
		string s,mids;
		cin>>s;
		list<int> output;

		for(int i = s.size()-1; i >=0; --i) {
//			char c = s[i];
//			int num = trans16To10(c);
//			while(num > 0 ) {
//				output.push_back(num%2);
//				//cout<<"num%2 = "<<num%2<<endl;
//				num /=2;
//			}
//
//			//��0
//			if(output.size()%4!=0) {
//				int cache_num = 4-output.size()%4;
//				for(int j = 0 ; j < cache_num; ++j ) {
//					output.push_back(0);
//				}
//			}





		}


		//output.reverse();
		stack<int> result;
		//�����Ľ���ճ�3λ��������λ��������2��8����ת��
		if(output.size()%3!=0) {
			int cache_num = 3-output.size()%3;
			for(int j = 0 ; j < cache_num; ++j ) {
				output.push_back(0);
			}
		}

		//	int wei_num = output.size()/3;  //ת����8����֮���λ��
		//	cout<<"output.size() = "<<output.size()<<endl;
		output.reverse();
		bool isNo1 = true; //��ֹ���ֲ�0
		for(list<int>::iterator it = output.begin() ; it!=output.end(); ) {
			//cout<<*(it++);
			int num = (*(it++))*4+(*(it++))*2+*(it++);
			//result.push(num);

			if(isNo1 && num==0) {
				continue;
			} else if(isNo1 && num!=0) {
				isNo1= false;
			}


			cout<<num;
		}
		cout<<endl;


	}
	return 0;
}



