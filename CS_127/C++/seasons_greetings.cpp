//Saurav Hossain
//10/30/18
//A C++ program that asks the user for the month of the year (as a number), and prints the season's Greetings 

#include <iostream>
using namespace std;

int main() 
{
  int x;
  cin >> x; 
  
  if(x < 3 || x > 11)
    cout << "Happy Winter";
  if(x >= 3 || x < 7)
    cout << "Happy Spring";
  if(x >= 7 || x > 9)
    cout << "Happy Summer";
  else 
    cout << "Happy Fall";
}