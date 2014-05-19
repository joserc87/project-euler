#include <iostream>
#include <cmath>
#include <list>

using namespace std;

int main (){
  long int number = 600851475143;
  list <long int> primos;
  long int primoMasGrande=0;
  for (long int i=2; i<=number && number != 1; i++){
    bool esPrimo=true;
    for (list <long int>::const_iterator iter = primos.begin (); iter != primos.end () && esPrimo; iter ++){
      if (i%(*iter)==0)
	esPrimo=false;
    }
    if (esPrimo){
      primos.push_back (i);
      while (number%i==0){
	number /= i;
	primoMasGrande=i;
      }
    }
  }
  cout << primoMasGrande << endl;
}
