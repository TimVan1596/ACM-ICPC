#include <iostream>
#include "PostFixCalculator.h"
using namespace std;

int main(int argc, char** argv) {

	string str = "642-/32*+";
	PostFixCalculator cal(str.size());
	cout<<"642-/32*+  ="<<cal.run(str)<<endl;
	return 0;
}
