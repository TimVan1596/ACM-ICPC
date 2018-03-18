#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <algorithm>
#include <vector>
using namespace std;

//n为此图的顶点个数，m为边的个数
unsigned int n = 0 , m = 0;

//代表无穷远点
const int MAX_INF =  999999;
//起点序号
const int START_NAME = 3;

class Node {
	public:
		//结点序号
		int name;
		//结点到起点的最短距离
		int dis;
		bool isUsed;

		Node(int name,int dis) {
			this->name = name;
			this->dis = dis;
			isUsed = false;
		}

};



//打印邻接矩阵,n为顶点个数(注意这里的二维数组传参方法)
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

//打印SU数组
void printSU( vector<Node> &S ,  vector<Node> &U) {
	cout<<"S = {";
	vector<Node>::iterator it = U.begin();
	for (; it != U.end(); it++) {
		if((*it).isUsed == true) {
			cout<<"【"<<(*it).name<<"】- "<<(*it).dis<<"，";
		}
	}
	cout<<"}"<<endl;

	cout<<"N = {";
	it = U.begin();
	for (; it != U.end(); it++) {
		if((*it).isUsed == false) {
			cout<<"【"<<(*it).name<<"】- "<<(*it).dis<<"，";
		}

	}
	cout<<"}"<<endl<<endl;

}

//向顶点加入边（邻接矩阵）
void add(unsigned int u , unsigned int v , int w , int (*array)[20000]) {
	array[u][v] = array[v][u] = w;
}


int main() {
	//n为此图的顶点个数，m为边的个数
	cin>>n>>m;
	int array[n][20000] = {MAX_INF};
	vector<Node> S , U;


	//初始化
	for(int i = 0; i < n ; ++i ) {


		U.push_back(*( new Node(i,MAX_INF)));

		for(int j = 0; j < n ; ++j ) {
			array[i][j] = MAX_INF;
		}

	}

	//起点距离设为0
	U[START_NAME].dis = 0;


	//录入时的临时变量，三个整数u, v, l，表示u到v有一条长度为l的边
	int cache_u , cache_v, cache_w;
	//录入每条边的信息

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
			初始化完成
		*---------------*
	*/


	//第一次遍历，寻找最短的边，作为S
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

	//将最短点归入已记录
	U.at(min_index).isUsed = true;

	//更新其余点到起点的最短距离
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
	    第一次寻找结束
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
		//更新其余点到起点的最短距离
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



