#include <iostream>

#include "SeqStack.h"
using namespace std;

const bool isBracketCorrect(string str);

//����һ���������ʽ�п��԰����������ţ�
//Բ���š�(���͡�)���������š�[���͡�]���ͻ����š�{���͡�}��
//��д�б�������ʽ�����������Ƿ���ȷ���
//���ַ� "\0"��Ϊ�������ʽ�Ľ�����
int main(int argc, char** argv) {


	string str = "{[3*4-(6*1.1)]/[3+0]}/{[3-2]+[2*2]}+{[(3.14)]}\0";
	cout<<"{\n Expression = "<<str<<endl;
	cout<<"Bracket is Correct = "<<isBracketCorrect(str)<<endl<<"}"<<endl<<endl;

	str = "{([])}";
	cout<<"{\n Expression = "<<str<<endl;
	cout<<"Bracket is Correct = "<<isBracketCorrect(str)<<endl<<"}"<<endl<<endl;

	str = "{([)}";
	cout<<"{\n Expression = "<<str<<endl;
	cout<<"Bracket is Correct = "<<isBracketCorrect(str)<<endl<<"}"<<endl<<endl;

	str = "3*{3-(2019/[33)}/8";
	cout<<"{\n Expression = "<<str<<endl;
	cout<<"Bracket is Correct = "<<isBracketCorrect(str)<<endl<<"}"<<endl<<endl;

	str = "3*{3-(2019/[33])}/8";
	cout<<"{\n Expression = "<<str<<endl;
	cout<<"Bracket is Correct = "<<isBracketCorrect(str)<<endl<<"}"<<endl<<endl;

	return 0;
}


//�б�������ʽ�����������Ƿ���ȷ���
const bool isBracketCorrect(string str) {
	bool isCorrect = true;
	const int len = str.size();
	SeqStack<char> bracketStack(len);

	for(int i = 0 ; i < len ; ++i) {
		char ch = str.at(i);

		if(ch == '{' || ch == '(' || ch == '[') {
			bracketStack.push(ch);
		} else if(ch == '}') {
			char previousChar;
			bracketStack.top(previousChar);
			if(previousChar == '{' ) {
				bracketStack.pop(previousChar);
			} else {
				isCorrect = false;
			}
		} else if(ch == ')') {
			char previousChar;
			bracketStack.top(previousChar);
			if(previousChar == '(') {
				bracketStack.pop(previousChar);
			} else {
				isCorrect = false;
			}
		} else if(ch == ']') {
			char previousChar;
			bracketStack.top(previousChar);
			if(previousChar == '[') {
				bracketStack.pop(previousChar);
			} else {
				isCorrect = false;
			}
		}
	}

	if(!bracketStack.isEmpty()) {
		isCorrect = false;
	}

	return isCorrect;
}
