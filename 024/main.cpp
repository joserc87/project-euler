#include <iostream>
#include <vector>


using namespace std;

int numPermutaciones (int numElm){
  if (numElm<=0){
    return (0);
  }else if (numElm==1){
    return (1);
  }else if (numElm==2){
    return (2);
  }
  return (numPermutaciones (numElm-1)*numElm);
}

int main (){
  const int numElm=10;
  int perm [numElm];
  int numPerm=1000000-1;
  vector <int> elementos (numElm);
  for (int i=0; i<numElm; i++)
    elementos [i]=i;
  for (int i=0; i<numElm; i++){
    int np = numPermutaciones (numElm-i-1);
    int indice = np>0?numPerm /np:0;
    perm [i] = elementos [indice];
    numPerm = np>0?numPerm%np:0;
    elementos.erase (elementos.begin ()+indice);
  }
  for (int i=0; i<numElm; i++){
    cout << perm [i];
  }
  cout << endl;
}
