//Saurav Hossain
//10/30/18
//Converts miles to kilometers

#include <iostream>

const double c = 0.621371;
int main() 
{
	double x;
	std::cin >> x;
	double s = x * c;
	std::cout << s;
}