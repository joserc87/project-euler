#include <iostream>
#include <cmath>
#include <list>

using namespace std;

int main (){
  list <int> primos;
  primos.push_back (2);
  int i=3;
  long int suma=2;
  bool terminar=false;
  while (!terminar){
    bool esPrimo=true;
    int raiz = (int)sqrt(i);
    for (list <int>::const_iterator iter = primos.begin (); iter != primos.end () && (*iter)<=raiz; iter++){
      if (i%(*iter)==0)
	esPrimo=false;
    }
    if (esPrimo){
      primos.push_back (i);
      if (i>=2000000){
	terminar=true;
      }else{
	suma += i;
      }
    }
    i+=2; // Solo tenemos que recorrer los impares
  }
  cout << suma << endl;
}
