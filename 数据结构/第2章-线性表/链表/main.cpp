#include <iostream>
#include "LinkedList.h"
using namespace std;

static void selectAll (LinkedList<int> list);

//�������
int main(int argc, char** argv)
{

	LinkedList<int> list;
	const int LEN = 7;
	int arr[LEN] = {2,4,8,16,32,64,128};
	for(int i = 0 ; i < 3 ; ++i)
	{
		list.insert(i,arr[i]);
	}
	selectAll(list);

	return 0;
}


// �������е�element
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


