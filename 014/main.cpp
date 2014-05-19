#include <iostream>
#include <vector>

using namespace std;

long int longChain (long int n, vector <long int> &chains){
  if (n==1){
    return (1);
  }
  if (n<1000000 && chains [n]>0){
    return (chains [n]);
  }

  n=(n%2==0?n/2:3*n+1);
  
  long int lng=1+longChain (n, chains);
  if (n<1000000){
    chains [n]=lng;
  }
  return (lng);
}

int main (){
  vector <long int> chains (1000000, -1);
  long int maxChain=0;
  long int start=0;
  for (int i=2; i<1000000; i++){
    long int chain = longChain (i, chains);
    if (chain > maxChain){
      maxChain = chain;
      start = i;
    }
  }
  cout << start << endl;
}
