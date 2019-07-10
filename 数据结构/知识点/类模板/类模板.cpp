#include <cstdio>
#include <iostream>
using namespace std;

//template<typename T>
//int bigger (){
//	int a = 1;
//	cout<<"Ä£°åÌåÄÚ"<<endl;
//	return 1;
//}

template<typename T>
T isbigger (const T a , const T b ){
	return a>b?a:b;
}


//template <typename T>
//inline T const& Max (T const& a, T const& b) 
//{ 
//    return a < b ? b:a; 
//} 


int main(){
	cout<<isbigger(3,2)<<endl; 
	cout<<isbigger(3.2,1.22)<<endl; 
	cout<<isbigger("hello","wor")<<endl; 
	return 0;
}
