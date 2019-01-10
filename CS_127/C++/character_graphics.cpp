//Saurav Hossain
//10/30/18
//A C++ program program that asks the user for a number and draws a triangle of that height and width using 'character graphics'

#include <iostream>
using namespace std;

int main() 
{
  int x;
  cin >> x; 
  for(int i = 0; i < x; i++)
  {
    cout << "\n";
    for(int j = 0; j <= i; j++)
      cout << "*";
  }
}