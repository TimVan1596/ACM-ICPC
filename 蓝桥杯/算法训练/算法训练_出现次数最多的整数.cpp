#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;

//问题描述
//　　编写一个程序，读入一组整数，这组整数是按照从小到大的顺序排列的，
//	它们的个数N也是由用户输入的，最多不会超过20。然
//	后程序将对这个数组进行统计，把出现次数最多的那个数组元素值打印出来。
//	如果有两个元素值出现的次数相同，即并列第一，那么只打印比较小的那个值。

bool comp(const pair<int,int> &a , const pair<int,int> &b) {
	bool isDesc = true;
	if(a.second ==  b.second) {
		isDesc = a.first < b.first;
	} else {
		isDesc = a.second > b.second;
	}

	return isDesc;
}

int main() {

	int N = 0;
	cin >> N;

	map<int,int> cnt;

	for(int i = 0 ; i < N ; ++ i) {
		int scanner = 0;
		cin>>scanner;
		map<int,int>::iterator it = cnt.find(scanner);
		if(it != cnt.end()) {
			int count = cnt[scanner];
			count++;
			cnt[scanner] = count;
		} else {
			cnt[scanner] = 1;
		}
	}

	if(N != 0) {
		vector< pair<int,int> > vec(cnt.begin(),cnt.end());
		sort(vec.begin(),vec.end(),comp);
		cout<<vec[0].first<<endl;
	}



//	for(int i = 0 ; i < vec.size() ;  ++i) {
//		cout<<"vec["<<i<<"] = "<<vec[i].first<<"-"<<vec[i].second<<endl;
//	}

	

}
