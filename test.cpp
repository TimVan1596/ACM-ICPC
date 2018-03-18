#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <stack>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;


typedef struct Human {
	string name;
	int age;
	char country[];
}human;


int main() {
	human man[5];
	man[0].name = "Tim";
	man[0].age = 10;
	strcat(man[0].country,"CN");


	cout<<man[0].name<<endl;
	cout<<man[0].age<<endl;
	cout<<man[0].country<<endl;

	
	

	return 0;
}
