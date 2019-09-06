#include <iostream>

#include "SeqStack.h"
using namespace std;

void matchBracket(const string str);

//ÿ����ͬ�������Ž�������������Ǹ���������ƥ��
int main(int argc, char** argv) {

	string str = "[([][])]";
	matchBracket(str);
	str = "([()]([[()[]]]))";
	matchBracket(str);
	return 0;
}


void matchBracket(const string str) {
	//�洢������
	SeqStack<char> stack(str.size()/2);

	for(int i = 0 ; i < str.size() ; ++i) {
		char c = str.at(i);
		if(c == ']' || c == ')') {
			char cache;
			stack.top(cache);
//			cout<<"c="<<c<<endl;
//			cout<<"cache="<<cache<<endl;
			if(((cache == '(') && (c == ')'))
			        || ((cache == '[') && (c == ']'))) {
				stack.pop(cache);
				cout<<"Match Successfully! -> "<<cache<<","<<c<<endl;
			} else {
				cout<<"matchBracket:[ERROR] SeqStack is Wrong "<<endl;
			}

		} else if(c == '[' || c == '(') {
			stack.push(c);
		} else {
			cout<<"matchBracket:[ERROR] Input Sequence is Wrong "<<endl;
		}
	}

	cout<<"isEmpty = "<<stack.isEmpty()<<endl;

	cout<<str<<endl;
}
