#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//¡¥±Ì≤‚ ‘
int main(int argc, char** argv)
{

	LinkedList<int> list;
	const int LEN = 5;
	int arr[LEN] = {2,4,8,16,32};
	for(int i = 0 ; i < LEN ; ++i)
	{
		list.insert(i,arr[i]);
	}
	selectAll(list);

	int element  = 0;
	list.deleteByIndex(4,element);
	cout<<endl<<"deleteByIndex(4,element),element="<<element<<endl;
	selectAll(list);

	element  = 2019;
	list.update(0,element);
	cout<<endl<<"update(0,2019)"<<endl;
	selectAll(list);

	return 0;
}



