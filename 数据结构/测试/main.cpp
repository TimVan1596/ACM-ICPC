#include <iostream>
using namespace std;

template<typename T>
class Base
{
	public:
		int n;
		virtual void show (T element) = 0;
};

template<typename T>
class Wheel
{
	public:
		string name;
		Wheel<T> *next;
		Wheel(string _name){
			name = _name;
		}

};

template<typename T>
class Derived:public Base<T>
{
	public:
		Wheel<T> *head;

		Derived()
		{
			this->n = 12;
			this->head = NULL;
		}
		void show (T element)
		{
			
			Wheel<T> *p;
			p = head;
			
			Wheel<int> *p_wheel = new Wheel<int>("ÂÖ×Ó");
			p = p_wheel;
			
			cout<<"p_wheel->name"<<p_wheel->name<<endl; 
			cout<<"p->name"<<p->name<<endl; 
			
		}
};


int main(int argc, char** argv)
{
	Derived<int> de;
	de.show(3);
	return 0;
}
