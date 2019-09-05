#ifndef POSTFIXCALCULATOR_H
#define POSTFIXCALCULATOR_H

#include <iostream>
#include "SeqStack.h"
using namespace std;

//��׺���ʽ������
class PostFixCalculator {
	public:
		PostFixCalculator(int size) {
			stack = new SeqStack<double>(size);
		}

		//ִ�к�׺���ʽ���㣬�����ؽ��
		double run(string str);

		//��׺���ʽת��׺���ʽ
		static string InFixToPostFix(string str);
	private:
		//��������ջ
		SeqStack<double> *stack;

		//��������ջ
		void pushOperand(double num) {
			stack->push(num);
		}

		//���ջ��ǰ����������
		void getOperands(double &num1 , double &num2) {
			stack->pop(num1);
			stack->pop(num2);
		}

		//���в�������������ļ���
		double doOperator(char ch);
};

double PostFixCalculator::run(string str)  {
	double ret;

	for(unsigned int i = 0; i<str.size() ; ++i) {
		char ch = str.at(i);
		double num = 0;
		if(ch >= '0' && ch <= '9') {
			num = ch-'0';
		} else {
			num = doOperator(ch);
		}
		pushOperand(num);
		//cout<<"pushOperand("<<num<<");"<<endl;
	}
	stack->pop(ret);
	return ret;
}

double PostFixCalculator::doOperator(char ch) {
	double ret;
	double num1 ,num2;
	getOperands(num1,num2);


	switch(ch) {
		case '+': {
			ret = num1+num2;
			break;
		}

		case '-': {
			ret = num2-num1;
			break;
		}

		case '*': {
			ret = num2*num1;
			break;
		}

		case '/': {
			ret = num2/num1;
			break;
		}

		default: {
			cout<<"doOperator:[ERROR] Operator is Illegal"<<endl;
			break;
		}
	}

	//cout<<"doOperator:("<<num1<<ch<<num2<<") = "<<ret<<endl;
	return ret;
}

string PostFixCalculator::InFixToPostFix(string str) {
	string ret = "";
	int cache_num = 0;

	cout<<"--------- InFixToPostFix Start --------"<<endl;
	cout<<"str = "<<str<<endl;
	int arrIndex = 0;
	for(unsigned int i=0; i<str.size(); ++i) {
		char c = str.at(i);
		if((c-'0')>=0 && (c-'0')<=9) {
			cache_num = cache_num*10 + (c-'0');
		} else {
			if(cache_num != 0) {
				cout<<++arrIndex<<":"<<cache_num<<endl;
				cache_num = 0;
			}
			cout<<++arrIndex<<":"<<c<<endl;
		}

	}
	if(cache_num != 0) {
		cout<<++arrIndex<<":"<<cache_num<<endl;
		cache_num = 0;
	}
	cout<<"--------- InFixToPostFix End --------"<<endl;

	return ret;
}
#endif
