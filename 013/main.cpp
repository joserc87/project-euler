#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>

using namespace std;

long int leerDigito (ifstream &fi){
  char dig=' ';
  while (dig<'0' || dig>'9'){
    fi >> dig;
  }
  return (dig-'0');
}

int main (){
  ifstream fi;
  fi.open ("50digit.txt");
  if (!fi){
    cerr << "ERROR: El archivo 50digit.txt no se puede abrir" << endl;
    return (-1);
  }
  
  vector <vector <long long int> > numbers (100);
  for (int i=0; i<100; i++){
    vector <long long int> fila (50, 0);
    for (int d=0; d<50; d++){
      long int n = leerDigito (fi);
      fila[d]=n;
    }
    numbers [i] = fila;
  }
  fi.close ();

  vector <long long int> resultado (50, 0);
  long long  int suma=0;
  for (int d=49; d>=0; d--){
    for (int i=0; i<100; i++){
      suma += numbers [i][d];
    }
    if (d>0)
      resultado [d] = suma %10;
    else
      resultado [d] = suma;
    suma /= 10;
  }
  int extraDigitosUltimo = log10(resultado [0]);
  for (int i=0; i<10-extraDigitosUltimo; i++){
    cout << resultado [i];
  }
  cout << endl;
}
