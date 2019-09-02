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
