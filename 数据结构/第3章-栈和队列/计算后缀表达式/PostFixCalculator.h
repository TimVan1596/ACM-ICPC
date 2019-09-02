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

		double run(string str) {
			double ret;

			for(int i = 0; i<str.size() ; ++i) {
				char ch = str.at(i);
				double num = 0;
				if(ch >= '0' && ch <= '9') {
					double num = ch-'0';
				} else {
					num = doOperator(ch);
				}
				pushOperand(num);
			}
			stack->pop(ret);
			return ret;
		}


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
		double doOperator(char ch) {
			double ret;
			double num1 ,num2;
			getOperands(num1,num2);
			switch(ch) {
				case '+': {
					ret = num1+num2;
					break;
				}

				case '-': {
					ret = num1-num2;
					break;
				}

				case '*': {
					ret = num1+num2;
					break;
				}

				case '/': {
					ret = num1+num2;
					break;
				}

				default:{
					cout<<"doOperator:[ERROR] Operator is Illegal"<<endl;
					break;
				}
			}


			return ret;
		}

};

#endif
