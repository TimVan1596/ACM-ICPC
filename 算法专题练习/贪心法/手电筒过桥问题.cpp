/*
	������N����Ҫ���ţ�ֻ��һ���ֵ�Ͳ��ÿ�ι��Ŷ���Ҫ�ֵ�Ͳ��
	ÿ������ͬʱ��K���ˣ����е�һ���˹���ҪA���ӣ��ڶ�����ҪB���ӡ�������N����Ҫx���ӡ�����̵Ĺ���ʱ�䡣
	 ��һ������K��N
	 ��������һ������K�˹��������ʱ��
*/

#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define MAXNUM 10000

vector<int> a;  //aΪδ����
vector<int> b;  //bΪ�Ѿ�����

int main() {
	//first��lastΪ�����±�
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
			//�������Ϊ·��
			ans+=a[K-1];
			//		printf("ans+=a[%d-1]=%d;\n",K,ans);
			//����С���Ǹ�����Ҫ���������� a.begin()+1
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
		//	printf("��ʱans = %d\n",ans);

			break;
		}

		//��һ�������� ������·��
		vector<int>::iterator it = a.begin();
		ans+=(*it);
//		printf("ans+=(%d);\n",*it);
	//	printf("��ʱans = %d\n",ans);

	//	cout<<"a.size() = "<<a.size()<<endl;

		int cache_i = 0;
		//�������Ϊ·��
		vector<int>::iterator it_cache = a.end()-1;
		ans+=(*it_cache);
	//	printf("��ʱans = %d\n",ans);

		if(a.size()>K) {
			//������K�����ͻ�
			//	printf("b.push_back();\n");

			for(vector<int>::iterator it = a.end()-1 ; cache_i < K; --it) {
		//		printf("b.push_back(%d);\n",*it);
				b.push_back(*it);
				//�������Ϊ·��

				a.erase(it);
				cache_i++;
			}

			sort(b.begin(),b.end());
			vector<int>::iterator it_cache = b.begin();
			ans+=(*it_cache);
			a.push_back(*it_cache);
	//		printf("�ͻ�  %d\n\n",*it_cache);

			b.erase(it_cache);
	//		cout<<"a.size() = "<<a.size()<<endl;
	//		printf("����ѭ��ans = %d\n\n",ans);

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
