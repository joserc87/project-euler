#include <iostream>

using namespace std;

/**
 * @return Devuelve <0 si es deficiente, >0 si es abundante o ==0 si es propio
 */
int abundanteDeficiente (int n){
  int accum = 0;
  for (int i=1; i<=n/2; i++){
    if (n%i==0){
      accum += i;
    }
  }
  if (accum>n){
    return (1);
  }else if (accum<n){
    return (-1);
  }else{
    return (0);
  }
}

int main (){
  // Calcular los abundantes
  bool abundantes [28123];
  for (int i=0; i<28123; i++){
    abundantes [i] = (abundanteDeficiente(i+1)>0);
  }
  // Calcular los números que pueden escribirse como suma de 2 números abundantes.
  bool sumaAbundantes [28123];
  for (int i=0; i<28123; i++)sumaAbundantes [i]=false;
  for (int i=0; i<28123; i++){
    if (abundantes [i]){
      for (int j=i; j<28123; j++){
	if (abundantes [j]){
	  int n = i+1 + j+1;
	  if (n<28123){
	    sumaAbundantes [n-1] = true;
	  }
	}
      }
    }
  }
  // Mirar cuales no se pueden calcular como suma de 2 números abundantes
  int count=0;
  int accum=0;
  for (int i=0; i<28123; i++){
    if (!sumaAbundantes [i-1]){
      count++;
      accum += i;
    }
  }
  cout << "Hay " << count << " números que no se pueden representar como suma de números abundantes y la suma total es " << accum << endl;
}
