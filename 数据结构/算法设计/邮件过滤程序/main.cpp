#include<iostream>
#include<cstdio>
#include<ctime>
#include<cstring>
#include <cassert>
using namespace std;
//1、邮件过滤程序；要求写出下列三个，并给出修改前后的性能比较。
//a)原始邮件过滤程序（直接调用c函数）；
//b)改写字符串比较后；
//c)改写邮件过滤逻辑后。
char* pat[5] = {"免费","广告","优惠","廉价","便宜"};

//char* pat[5] = {"ad","ads","free","cheap","Advertisement"};
int npat = 5;
int N = 1000000;
// isspam 垃圾邮件处理
int original_isspam( const char *mesg ) {
	int i;
	for( i=0; i<npat; i++ )
		if(strstr( mesg, pat[i] ) ) {
//			printf( "垃圾邮件：检测到 %s\n", pat[i] ); //实际软件中没有
			return 1;
		}
	return 0;
}


//自己的strstr函数
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
		//*s2不为空，并且*s1要与*s2相等
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


// isspam 垃圾邮件处理
int improved_isspam(const char *mesg ) {
	int i;
	for( i=0; i<npat; i++ )
		if( my_strstr( mesg, pat[i] ) ) {
//			printf( "垃圾邮件：检测到 %s\n", pat[i] ); //实际软件中没有
			return 1;
		}
	return 0;
}

int main() {
	string msg_1 = "鲁迅写给许广平 1925年3月11日 ";
	string msg_2 = "广平兄：今天收到来信，有些问题恐怕我答不出，姑且写下去看。";
	string msg_3 = "鲁迅 3月11日";
	string msg_spam = "广告：本店新品免费试用，开业优惠！";

	string msg = msg_1.append(msg_2).append(msg_3).append(msg_spam);
	string msg_ad = msg_1.append(msg_2).append(msg_3).append(msg_spam);


	// 将邮件转为char*格式
	const char* char_msg = msg.data();
	const char* char_ad_msg = msg_ad.data();

	
	cout<<"运行"<<N<< "次后，"<<endl;
	//计算程序运行时间
	clock_t start,end;
	start = clock();

	for (int i = 0; i<N; ++i) {
		original_isspam(char_ad_msg);
	}
	end = clock();
	cout<<"original_isspam：time = "<<double(end-start)/CLOCKS_PER_SEC<<"s"<<endl;


	start = clock();

	for (int i = 0; i<N; ++i) {
		improved_isspam(char_ad_msg);
	}
	end = clock();
	cout<<"improved_isspam：time = "<<double(end-start)/CLOCKS_PER_SEC<<"s"<<endl;


	return 0;


}
