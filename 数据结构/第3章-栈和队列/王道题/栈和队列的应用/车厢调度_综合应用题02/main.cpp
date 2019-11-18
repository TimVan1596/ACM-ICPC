#include <iostream>
#include "SeqStack.h"
using namespace std;

const string trackSchedule(string str);

/* ��ͼ��ʾ�������г������(ע��: ����������Ϊ������ʻ��,�𳵵���վ��һ��
���ڵ��ȵġ�ջ����),�𳵵���վ����ڴ���n��Ӳ������������(�ֱ���H��S��ʾ)�ȴ���
��,�Ա�д�㷨,�������n�ڳ�����е��ȵĲ���(����ջ���ջ����)����,��ʹ���е���
�����ᶼ��������Ӳ������֮ǰ�� */
int main(int argc, char** argv) {
 
	string str = "HSHHSHHHSHHSH";
	cout<<"{\n Track = "<<str<<endl;
	cout<<"OutPut = "<<trackSchedule(str)<<endl<<"}"<<endl<<endl;
	return 0;
}

//ʹ���е��������ᶼ��������Ӳ������֮ǰ
const string trackSchedule(string str) {
	string ret = "";
	const int len = str.size();
	SeqStack<char> carriageStack(len);

	for(int i = 0 ; i < len ; ++i) {
		char ch = str.at(i);
		if(ch == 'H') {
			carriageStack.push(ch);
		} else {
			ret.append("S");
		}
	}

	while(!carriageStack.isEmpty()) {
		char ch;
		carriageStack.pop(ch);
		ret.push_back(ch);
	}

	return ret;
}
