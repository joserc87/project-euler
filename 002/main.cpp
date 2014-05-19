#include <iostream>

using namespace std;

int main (){
  int a=1;
  int b=2;
  int suma = 0;
  while (b<=4000000){
    int c = a+b;
    a = b;
    b = c;
    if (a%2==0)
      suma += a;
  }
  cout << suma << endl;
}
