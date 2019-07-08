#include <iostream>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);

//设计一个高效算法，将顺序表的所有元素逆置，
//要求算法的空间复杂度为O(1).
int main(int argc, char** argv) {
	ArrayList<int> list(10);
	const int LEN = 7;
	int arr[LEN] = {14,6,20,9,7,11,1};
	for(int i = 0; i < LEN ; ++i ) {
		list.insert(i,arr[i]);
	}
	selectAll(list);

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
