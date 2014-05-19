#include <iostream>
#include <cmath>

using namespace std;

bool esPalindromo (int num){
  // No creo que tenga >20 dígitos el número... Me ahorro un vector dinámico
  int digitos [20];
  //  int numDigitos = log10 ((float)num)+1;
  int n=num;
  //  for (int i=0; i<numDigitos; i++){
  int numDigitos=0;
  while (n!=0){
    digitos [numDigitos] = n%10;
    n/=10;
    numDigitos++;
  }
  bool palindromo = true;
  for (int i=0; i<ceil (((float)numDigitos)/2.0) && palindromo; i++){
    if (digitos [i] != digitos [numDigitos-i-1]){
      palindromo=false;
    }
  }
  return (palindromo);
}

int main (){
  // En plan chapucero:
  int maximo=-1;
  for (int a=100; a<999; a++){
    for (int b = a; b < 999; b++){
      int c = a*b;
      if (c>maximo && esPalindromo (c)){
	maximo=c;
      }
    }
  }
  cout << maximo << endl;
}
