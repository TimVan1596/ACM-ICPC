#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//链表测试
int main(int argc, char** argv)
{

	LinkedList<int> list;
	const int LEN = 7;
	int arr[LEN] = {2,4,8,16,32,64,128};
	for(int i = 0 ; i < 3 ; ++i)
	{
		list.insert(i,arr[i]);
	}

	list.selectAll();


	int element  = 3;
	int i =0;
	list.select(i,element);
	cout<<i<<"->"<<element<<endl;

	i =1;
	list.select(i,element);
	cout<<i<<"->"<<element<<endl;

	i =2;
	list.select(i,element);
	cout<<i<<"->"<<element<<endl;

		selectAll(list);

	return 0;
}


// 查找所有的element
static void selectAll (LinkedList<int> list)
{
	
	cout<<"list.getCurrLength()="<<list.getCurrLength()<<endl;
	
	cout<<"LinkedList={"<<endl;
	for(int i = 0 ; i < list.getCurrLength(); ++i )
	{
		int element  = 0;
		if(list.select(i,element))
		{
			cout<<i<<"->"<<element<<endl;
		}
		else
		{
			cout<<i<<"->"<<"Out of Bound"<<endl;
		}
	}
	cout<<"}"<<endl;
}


