#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <algorithm>
#include <vector>
using namespace std;

#define TRANSNUM 16



int print16To10(char num) {
	if(num>='A' && num <='F') {
		return num-'A'+10;
	} else {
		return num-'0';
	}
}

long long Trans16To10(string s) {
	int c = 0;
	long long result = 0;
	int length = s.size();

	for(int i = length-1; i>=0; --i) {
		//cout<<s[i];
		result += print16To10(s[i])*pow(16,c);
		c++;
	}

	return result;
}

int main() {

	int n = 0;
	cin>>n;
	vector< stack<int> > out;

	while(n--) {
		string s;
		cin>>s;
		long long ten = Trans16To10(s);
		if(ten == 0) {
			cout<<0;
			continue;
		}
		//long long ten = 5000;
		long long ten_cache = ten;
		int c = 0,result = 0;
		stack<int> output;

		while(ten > 0 ) {
			output.push(ten%8);
			//cout<<ten%8<<endl;
			ten /=8;

		}
//		while(!output.empty()) {
//			cout<<output.top();
//			output.pop();
//		}
//		cout<<endl;
		out.push_back(output);
	}

	vector< stack<int> >::iterator it = out.begin();

	for(; it!=out.end(); it++) {
		while(!(*it).empty()) {
			cout<<(*it).top();
			(*it).pop();
		}
		cout<<endl;
	}



	return 0;
}


