#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//链表测试
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


// 查找所有的element
static void selectAll (LinkedList<int> list)
{
	cout<<"LinkedList={"<<endl;
	for(int i = 0 ; i < list.getCurrLength(); ++i )
	{

		int element  = 0;
		if(list.select(i,element))
		{
			cout<<"  "<<i<<"->"<<element<<endl;
		}
		else
		{
			cout<<"  "<<i<<"->"<<"Out of Bound"<<endl;
		}
	}
	cout<<"}"<<endl;
}


