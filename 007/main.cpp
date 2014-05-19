#include <iostream>
#include <list>

using namespace std;

int main (){
  list <int> primos;
  primos.push_back (2);
  int i=3;
  while (primos.size () < 10001){
    bool esPrimo=true;
    for (list <int>::const_iterator iter = primos.begin (); iter != primos.end (); iter++){
      if (i%(*iter)==0)
	esPrimo=false;
    }
    if (esPrimo){
      primos.push_back (i);
    }
    i+=2; // Solo tenemos que recorrer los impares
  }
  cout << primos.back () << endl;
}
