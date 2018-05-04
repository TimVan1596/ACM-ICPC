#include <bits/stdc++.h>
using namespace std;

//http://acm.hfut.edu.cn/OnlineJudge/
//第一行输入正整数T，表示数据的组数。
//每组数据的第一行是购买的物品的种类数n 和顾客给的钱的总数m(顾客给的钱不会有"分"),
// 接下来有n行[1,100],每行两个数字,第一个数字是该物品的价格Pi([0.01,10000]),第二个数字是该物品的数量Ci([1,10])。

double change(double sum_price) {
	int big = sum_price*100;

	int ret = big%10;
	if(ret > 0) {
		big = (big-ret)+10;
	}
	return (big/100.0);
}

int main() {
	int T = 0;
	cin>>T;
	for (int sum_i = 0; sum_i < T ; ++sum_i) {
		int n = 0;
		double sum_price = 0,sum_cost = 0;
		cin>>n>>sum_price;

		for (int i = 0; i < n ; ++i) {
			double price = 0;
			int num = 0;
			cin>>price>>num;
			sum_cost += num*price;

		}
		
		sum_cost = change(sum_cost);
		
		if((sum_price-sum_cost)>=0) {
		//	cout<<"sum_price = "<<sum_price<<endl;
			cout<<"Case "<<sum_i+1<<": "<<setiosflags(ios::fixed)<<setprecision(2)<<sum_price-sum_cost<<endl;
		} else {
			cout<<"Case "<<sum_i+1<<": "<<-1<<endl;
		}

	}

	return 0;
}


/*
#include<bits/stdc++.h>
using namespace std;


double change(double sum_cost) {
	int big = sum_cost*100;



	int ret = big%10;
	if(ret > 0) {
		big = (big-ret)+10;
	}
	return (big/100.0);

}


int main() {
	double sum_cost = 8.819;
	double sum_price = 200.20;

	sum_cost = change(sum_cost);
	cout<<"sum_cost = "<<sum_cost<<endl;
	cout<<"sum_price = "<<sum_price-sum_cost<<endl;
	cout<<"--precision--  sum_price = "<<setiosflags(ios::fixed)<<setprecision(2)<<sum_price-sum_cost<<endl;




//	cout<<setiosflags(ios::fixed)<<setprecision(1)<<(floor(sum_price*10))/10<<0<<endl;

	return 0;
}
*/
