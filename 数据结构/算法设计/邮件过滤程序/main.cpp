#include<iostream>
#include<cstdio>
#include<ctime>
#include<cstring>
#include <cassert>
using namespace std;
//1���ʼ����˳���Ҫ��д�������������������޸�ǰ������ܱȽϡ�
//a)ԭʼ�ʼ����˳���ֱ�ӵ���c��������
//b)��д�ַ����ȽϺ�
//c)��д�ʼ������߼���
char* pat[5] = {"���","���","�Ż�","����","����"};

//char* pat[5] = {"ad","ads","free","cheap","Advertisement"};
int npat = 5;
int N = 1000000;
// isspam �����ʼ�����
int original_isspam( const char *mesg ) {
	int i;
	for( i=0; i<npat; i++ )
		if(strstr( mesg, pat[i] ) ) {
//			printf( "�����ʼ�����⵽ %s\n", pat[i] ); //ʵ�������û��
			return 1;
		}
	return 0;
}


//�Լ���strstr����
const char * __cdecl my_strstr( const char *str1,  char *str2) {
	char *cur = (char *)str1;
	char *s1 = NULL;
	char *s2 = NULL;
	if (!*str2) {
		return ((char *)str1);
	}
	while (*cur) {
		s1 = cur;
		s2 = (char *)str2;
		//*s2��Ϊ�գ�����*s1Ҫ��*s2���
		while (*s2 && !(*s1 - *s2)) { 
			s1++;
			s2++;
		}
		if (!*s2) {
			return cur;
		}
		cur++;
	}
	return NULL;
}


// isspam �����ʼ�����
int improved_isspam(const char *mesg ) {
	int i;
	for( i=0; i<npat; i++ )
		if( my_strstr( mesg, pat[i] ) ) {
//			printf( "�����ʼ�����⵽ %s\n", pat[i] ); //ʵ�������û��
			return 1;
		}
	return 0;
}

int main() {
	string msg_1 = "³Ѹд�����ƽ 1925��3��11�� ";
	string msg_2 = "��ƽ�֣������յ����ţ���Щ��������Ҵ𲻳�������д��ȥ����";
	string msg_3 = "³Ѹ 3��11��";
	string msg_spam = "��棺������Ʒ������ã���ҵ�Żݣ�";

	string msg = msg_1.append(msg_2).append(msg_3).append(msg_spam);
	string msg_ad = msg_1.append(msg_2).append(msg_3).append(msg_spam);


	// ���ʼ�תΪchar*��ʽ
	const char* char_msg = msg.data();
	const char* char_ad_msg = msg_ad.data();

	
	cout<<"����"<<N<< "�κ�"<<endl;
	//�����������ʱ��
	clock_t start,end;
	start = clock();

	for (int i = 0; i<N; ++i) {
		original_isspam(char_ad_msg);
	}
	end = clock();
	cout<<"original_isspam��time = "<<double(end-start)/CLOCKS_PER_SEC<<"s"<<endl;


	start = clock();

	for (int i = 0; i<N; ++i) {
		improved_isspam(char_ad_msg);
	}
	end = clock();
	cout<<"improved_isspam��time = "<<double(end-start)/CLOCKS_PER_SEC<<"s"<<endl;


	return 0;


}
