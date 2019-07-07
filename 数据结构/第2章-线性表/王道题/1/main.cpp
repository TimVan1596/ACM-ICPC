#include <iostream>
#include <vector>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);

int main(int argc, char** argv) {

	ArrayList<int> list(10);

	for(int i = 0 ; i < 5 ; ++i) {
		list.insert(i,(i+1)*(i+1));
	}
	selectAll(list);

	int deleteElement  = 0;
	list.deleteByIndex(2,deleteElement);
	cout<<"deleteElement="<<deleteElement<<endl;

	selectAll(list);

	list.update(2,233);
	selectAll(list);

	//ArrayList list(3);

	return 0;
}


// 查找所有的element
static void selectAll (ArrayList<int> list) {
	cout<<"ArrayList={"<<endl;
	for(int i = 0 ; i < list.getCurrLength(); ++i ) {
		int element  = 0;
		if(list.select(i,element)) {
			cout<<i<<"->"<<element<<endl;
		} else {
			cout<<i<<"->"<<"Out of Bound"<<endl;
		}
	}
	cout<<"}"<<endl;
}
