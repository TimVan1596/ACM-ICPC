#include <iostream>
#include <vector>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);

int main(int argc, char** argv) {
	
	ArrayList<int> list(10);
	
	int element = 123;
	list.insert(0,element);
	selectAll(list);
	
	//ArrayList list(3);

	return 0;
}


// 查找所有的element
static void selectAll (ArrayList<int> list) {
	cout<<"ArrayList={"<<endl;
	for(int i = 0 ; i < list.getMaxLength();++i ){
		int element  = 234;
		if(list.select(i,element)){
			cout<<i<<"->"<<element<<endl;
		}else{
			cout<<i<<"->"<<"Out of Bound"<<endl;
		}
		
		
	}
	cout<<"}"<<endl;
}
