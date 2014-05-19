#include <iostream>
#include <fstream>

using namespace std;

int leerDigito (ifstream &fi){
  while (!fi.eof ()){
    char c=' ';
    fi >> c;
    if (c >= '0' || c <= '9'){
      return (c-'0');
    } 
  }
}

int main (){
  int digitos [1000];
  ifstream fi;
  fi.open ("1000digit.txt");
  if (!fi){
    cerr << "ERROR: el archivo 1000digit.txt no existe" << endl;
    return (-1);
  }
  for (int i=0; i<1000; i++){
    digitos [i] = leerDigito (fi);
  }
  int maxMul=0;
  for (int i=0; i<1000-5; i++){
    int mul=1;
    for (int j=i; j<i+5; j++){
      mul *= digitos [j];
    }
    if (mul > maxMul){
      maxMul = mul;
    }
  }
  cout << maxMul << endl;
}
