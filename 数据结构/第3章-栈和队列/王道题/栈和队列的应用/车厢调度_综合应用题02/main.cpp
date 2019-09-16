#include <iostream>
#include "SeqStack.h"
using namespace std;

const string trackSchedule(string str);

/* 如图所示铁道进行车厢调度(注意: 两侧铁道均为单向行驶道,火车调度站有一个
用于调度的“栈道”),火车调度站的入口处有n节硬座和软座车厢(分别以H和S表示)等待调
度,试编写算法,输出对这n节车厢进行调度的操作(即入栈或出栈操作)序列,以使所有的软
座车厢都被调整到硬座车厢之前。 */
int main(int argc, char** argv) {
 
	string str = "HSHHSHHHSHHSH";
	cout<<"{\n Track = "<<str<<endl;
	cout<<"OutPut = "<<trackSchedule(str)<<endl<<"}"<<endl<<endl;
	return 0;
}

//使所有的软座车厢都被调整到硬座车厢之前
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
