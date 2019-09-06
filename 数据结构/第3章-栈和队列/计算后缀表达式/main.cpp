#include <iostream>
#include "PostFixCalculator.h"
using namespace std;

int main(int argc, char** argv) {

	const int LEN = 20;
	string str = "642-/32*+";
	PostFixCalculator cal(LEN);
	cout<<"642-/32*+  ="<<cal.run(str)<<endl;
	str = "123+4*+5-";
	cout<<str<<"  ="<<cal.run(str)<<endl;
	str = "2963/+5-*4+";
	cout<<str<<"  ="<<cal.run(str)<<endl;
	str = "90/3+(30/2-1)*3";
	PostFixCalculator::InFixToPostFix(str);
	str = "24*19-34/17+(128+35*3)";
	PostFixCalculator::InFixToPostFix(str);

	return 0;
}
