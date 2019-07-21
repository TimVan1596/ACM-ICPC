#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;

//��������
//������дһ�����򣬶���һ�����������������ǰ��մ�С�����˳�����еģ�
//	���ǵĸ���NҲ�����û�����ģ���಻�ᳬ��20��Ȼ
//	����򽫶�����������ͳ�ƣ��ѳ��ִ��������Ǹ�����Ԫ��ֵ��ӡ������
//	���������Ԫ��ֵ���ֵĴ�����ͬ�������е�һ����ôֻ��ӡ�Ƚ�С���Ǹ�ֵ��

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
