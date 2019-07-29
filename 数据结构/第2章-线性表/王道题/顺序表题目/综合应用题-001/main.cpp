#include <iostream>

#include "ArrayList.h"
using namespace std;

static void selectAll (ArrayList<int> list);
bool deleteMinElement (ArrayList<int> &list);

//题目：从顺序表中删除具有最小值的元素（假设唯一）并由函数返回被删元素的值。
//空出的位置由最后一个元素填补，若顺序表为空则显示出错信息并退出运行。
int main(int argc, char** argv) {

	ArrayList<int> list(20);
	const int LEN = 7;
	int arr[LEN] = {14,6,20,9,7,11,1};
	for(int i = 0; i < LEN ; ++i ) {
		list.insert(i,arr[i]);
	}
	selectAll(list);

	if(!deleteMinElement(list)){
		return 1;
	}
	selectAll(list);


	return 0;
}



// 顺序表中删除具有最小值的元素（假设唯一）
bool deleteMinElement (ArrayList<int> &list) {
	cout<<"--- 从顺序表中删除具有最小值的元素 ---"<<endl;

	int min = 0;
	int index = 0;
	if(list.select(0,min)) {
		for(int i = 0; i < list.getCurrLength() ; ++i ) {
			int element = 0;
			list.select(i,element);
			if(min>element) {
				min = element;
				index = i;
			}
		}
	} else {
		cout<<"[ERROR]=> ArrayList is NULL"<<endl;
		return false;
	}

	int element;
	list.deleteByIndex(index,element);
	cout<<"delete element = "<<element<<endl;
	list.select(list.getCurrLength()-1,element);
	list.insert(index,element);

	cout<<"--- ---"<<endl;
	return true;
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
