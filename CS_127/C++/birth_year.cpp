//Saurav Hossain
//10/30/18
//A C++ program that asks the user for the year born, and continue asking until the number entered that is 2018 or earlier

#include <iostream>
using namespace std;

int main() 
{
 int x;
 cout << "Please enter year born:";
 cin >> x;

 while (x > 2018)
 {
  if(x < 2018)
  {
    break;
  }
  else
  cout << "Entered a future year\n";
  cout << "Please enter age:";
  cin >> x;
 }
cout << "You entered: ";
cout << x;
}