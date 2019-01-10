//Saurav Hossain
//10/30/18
//A C++ program that asks the user for a whole number between -31 and 31 and prints out the number in "two's complement" notation

#include <iostream>
using namespace std;

int main() 
{

 int n;
 int x;
 int b = 16;
 cin >> n;


 if(n < 0)
 {
   x = 32 + n;
   cout << 1;
 }
 if(n >= 0)
 {
   x = n;
   cout << 0;
 }
 while(b > 0.5)
 {
   if(x >= b)
   {
     cout << 1;
   }
   else
     cout << 0;
   x = x % b;
   b = b/2;
 }
 cout << "\n";
}