#include<iostream>
using namespace std;

int N;
string str;

int main(void) {
	int len;
	int Maxcnt = 0;
	string ans, s;


	cin >> N >> str;
//	N = 4;
//	str = "bbaabbaaaaa";
//	len = str.size();


	for(int k = len; k >= N; --k) {
		for(int i = 0; i < len - k; ++i) {

			//�ָ������Ӵ�
			s.assign(str, i, k);

			int cnt = 0;
			string temp;
			//�ظ����ң����ҷ����Ӵ�������
			for(int j = 0; j < len - k; j++) {  
				temp.assign(str, j, k);
				if(s == temp) {
					cnt++;
				}
			}

			if(Maxcnt < cnt) {
				Maxcnt = cnt;
				ans = s;
			}
		}
	}

	cout << ans;
	return 0;
}
