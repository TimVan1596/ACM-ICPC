#include <iostream>
using namespace std;

template<typename T>
class Base{
	public:
		int n;
		virtual void show (T element) = 0;
}; 

template<typename T>
class Wheel{
	public:
		string name;
		int value;
		Wheel(){
			name = "ÂÖ×Ó";
			value = 100;
		}
		
};

template<typename T>
class Derived:public Base<T>{
	public:
		Derived(){
			this->n = 12;
		}
		 void show (T element){
		 	Wheel<T> *wheel = new Wheel<T>();
		 	cout<<"wheel->name = "<<wheel->name<<endl;
		 }
};


int main(int argc, char** argv) {
	Derived<int> de;
	de.show(3);
	return 0;
}
