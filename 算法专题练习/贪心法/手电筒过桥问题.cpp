/*
	晚上有N个人要过桥，只有一个手电筒，每次过桥都需要手电筒，
	每次最多可同时过K个人，其中第一个人过桥要A分钟，第二个人要B分钟。。。第N个人要x分钟。求最短的过桥时间。
	 第一行输入K和N
	 接下来的一行输入K人过桥所需的时间
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define MAXNUM 10000

vector<int> a;  //a为未过桥
vector<int> b;  //b为已经过桥

int main() {
	//first和last为两个下标
	unsigned int K = 0 , N = 0,ans = 0,first = 0,last = 0;
	cin>>N>>K;
	first = 0;
	last  = N-1;
	for(int i = 0 ; i < N ; ++i) {
		int cache;
		cin>>cache;
		a.push_back(cache);
	}

	sort(a.begin(),a.end());

//	cout<<"a.size() = "<<a.size()<<endl;




	while(a.size()) {
	//	printf("hello \n");
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());

		if(a.size()>K) {
			//最大数作为路程
			ans+=a[K-1];
			//		printf("ans+=a[%d-1]=%d;\n",K,ans);
			//从最小的那个数还要回来，所以 a.begin()+1
			int cache_i = 0;
			for(vector<int>::iterator it = a.begin()+1 ;  cache_i < K-1;) {
				b.push_back(*it);
				//printf("b.push_back(%d);\n",*it);
				cache_i++;
				a.erase(it);
			}
		} else {
			vector<int>::iterator it_cache = a.end()-1;
			ans+=(*it_cache);
		//	printf("此时ans = %d\n",ans);

			break;
		}

		//第一个数返回 ，加上路程
		vector<int>::iterator it = a.begin();
		ans+=(*it);
//		printf("ans+=(%d);\n",*it);
	//	printf("此时ans = %d\n",ans);

	//	cout<<"a.size() = "<<a.size()<<endl;

		int cache_i = 0;
		//最大数作为路程
		vector<int>::iterator it_cache = a.end()-1;
		ans+=(*it_cache);
	//	printf("此时ans = %d\n",ans);

		if(a.size()>K) {
			//将最大的K个数送回
			//	printf("b.push_back();\n");

			for(vector<int>::iterator it = a.end()-1 ; cache_i < K; --it) {
		//		printf("b.push_back(%d);\n",*it);
				b.push_back(*it);
				//最大数作为路程

				a.erase(it);
				cache_i++;
			}

			sort(b.begin(),b.end());
			vector<int>::iterator it_cache = b.begin();
			ans+=(*it_cache);
			a.push_back(*it_cache);
	//		printf("送回  %d\n\n",*it_cache);

			b.erase(it_cache);
	//		cout<<"a.size() = "<<a.size()<<endl;
	//		printf("本次循环ans = %d\n\n",ans);

		} else {

			//	printf("ans+=a[%d-1]=%d;\n",K,ans);
			for(vector<int>::iterator it = a.end()-1 ; it >= a.begin(); --it) {
				b.push_back(*it);
				//	printf("b.push_back(%d);\n",*it);
				cache_i++;
				a.erase(it);
			}
			break;

		}
	}


	cout<<ans<<endl;
	return 0;
}
