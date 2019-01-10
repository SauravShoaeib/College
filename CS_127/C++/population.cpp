//Saurav Hossain
//10/30/18
//A complete C++ program that prints the change in population of the the United States 

#include <iostream>
using namespace std;

int main() 
{
 std::cout.precision(2);
 std::cout.setf(std::ios::fixed);

 int x;
 cin >> x;
 
 double p = 325.7;
 double b = 12.4;
 double d = 8.4;
 int year = 2017;
 
 for(int i = 0; i < x; i++)
 {
 	cout << "Year " << i + year << " " << p << "\n";
 	p = p + b*p - d*p;
 }
}