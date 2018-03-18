#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
#include <vector>
using namespace std;

//nΪ��ͼ�Ķ��������mΪ�ߵĸ���
unsigned int n = 0 , m = 0;

//��������Զ��
const int MAX_INF =  999999;
//������
const int START_NAME = 3;

class Node {
	public:
		//������
		int name;
		//��㵽������̾���
		int dis;
		bool isUsed;

		Node(int name,int dis) {
			this->name = name;
			this->dis = dis;
			isUsed = false;
		}

};



//��ӡ�ڽӾ���,nΪ�������(ע������Ķ�ά���鴫�η���)
void printChart(int n,int (*array)[20000]) {

	for(int i = 0; i < n ; ++i ) {

		for(int j = 0; j < n ; ++j ) {
			if(array[i][j] == MAX_INF ) {
				cout<<"\t"<<'X';
			} else {
				cout<<"\t"<<array[i][j];
			}
		}
		cout<<endl;
	}
}

//��ӡSU����
void printSU( vector<Node> &S ,  vector<Node> &U) {
	cout<<"S = {";
	vector<Node>::iterator it = U.begin();
	for (; it != U.end(); it++) {
		if((*it).isUsed == true) {
			cout<<"��"<<(*it).name<<"��- "<<(*it).dis<<"��";
		}
	}
	cout<<"}"<<endl;

	cout<<"N = {";
	it = U.begin();
	for (; it != U.end(); it++) {
		if((*it).isUsed == false) {
			cout<<"��"<<(*it).name<<"��- "<<(*it).dis<<"��";
		}

	}
	cout<<"}"<<endl<<endl;

}

//�򶥵����ߣ��ڽӾ���
void add(unsigned int u , unsigned int v , int w , int (*array)[20000]) {
	array[u][v] = array[v][u] = w;
}


int main() {
	//nΪ��ͼ�Ķ��������mΪ�ߵĸ���
	cin>>n>>m;
	int array[n][20000] = {MAX_INF};
	vector<Node> S , U;


	//��ʼ��
	for(int i = 0; i < n ; ++i ) {


		U.push_back(*( new Node(i,MAX_INF)));

		for(int j = 0; j < n ; ++j ) {
			array[i][j] = MAX_INF;
		}

	}

	//��������Ϊ0
	U[START_NAME].dis = 0;


	//¼��ʱ����ʱ��������������u, v, l����ʾu��v��һ������Ϊl�ı�
	int cache_u , cache_v, cache_w;
	//¼��ÿ���ߵ���Ϣ

	for(int i = 0 ; i < m ; ++i) {
		cin>>cache_u>>cache_v>>cache_w;
		add(cache_u,cache_v,cache_w,array);

//		if(cache_u == START_NAME) {
//			U[cache_v].dis = cache_w;
//		} else if (	cache_v == START_NAME) {
//			U[cache_u].dis = cache_w;
//		}
	}



	/*
		*---------------*
			��ʼ�����
		*---------------*
	*/


	//��һ�α�����Ѱ����̵ıߣ���ΪS
	vector<Node>::iterator it = U.begin();
	int min_index = 0,min_dis = MAX_INF, cnt = -1;
	for(; it < U.end(); it++) {
		cnt++;
		// cout<<"cnt="<<cnt<<"  -(*it).dis="<<(*it).dis<<endl;


		if((*it).dis < min_dis && (*it).isUsed == false ) {
			min_dis = (*it).dis;
			min_index = cnt;
		}

	}
//	cout<<"min_index : "<<min_index<<endl;

	//����̵�����Ѽ�¼
	U.at(min_index).isUsed = true;

	//��������㵽������̾���
	it = U.begin();
	for(; it < U.end(); it++) {
		if((*it).isUsed == false && array[(*it).name][min_index] +min_dis  < MAX_INF) {
			//cout<<"-name="<<(*it).name<<"  -min="<<array[(*it).name][min_index]<<endl;
			(*it).dis =(array[(*it).name][min_index] +min_dis);
		}
	}

	printSU(S,U);



	/*
	*---------------*
	    ��һ��Ѱ�ҽ���
	*---------------*
	*/


	it = U.begin();
	 min_index = 0,min_dis = MAX_INF, cnt = -1;
	for(; it < U.end(); it++) {
		cnt++;
		// cout<<"cnt="<<cnt<<"  -(*it).dis="<<(*it).dis<<endl;


		if((*it).isUsed == false && (*it).dis < min_dis) {
			min_dis = (*it).dis;
			min_index = cnt;
		}

	}
	U.at(min_index).isUsed = true;
		//��������㵽������̾���
	it = U.begin();
	for(; it < U.end(); it++) {
		if((*it).isUsed == false && (array[(*it).name][min_index] +min_dis) < MAX_INF) {
			//cout<<"-name="<<(*it).name<<"  -min="<<array[(*it).name][min_index]<<endl;
			(*it).dis =(array[(*it).name][min_index] +min_dis);
		}
	}

	printSU(S,U);





	printChart(n,array);



	return 0;
}



