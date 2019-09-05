#ifndef POSTFIXCALCULATOR_H
#define POSTFIXCALCULATOR_H

#include <iostream>
#include "SeqStack.h"
using namespace std;

//后缀表达式计算器
class PostFixCalculator {
	public:
		PostFixCalculator(int size) {
			stack = new SeqStack<double>(size);
		}

		//执行后缀表达式计算，并返回结果
		double run(string str);

		//中缀表达式转后缀表达式
		static string InFixToPostFix(string str);
	private:
		//操作数的栈
		SeqStack<double> *stack;

		//操作数进栈
		void pushOperand(double num) {
			stack->push(num);
		}

		//获得栈顶前两个操作手
		void getOperands(double &num1 , double &num2) {
			stack->pop(num1);
			stack->pop(num2);
		}

		//进行操作数与操作符的计算
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
