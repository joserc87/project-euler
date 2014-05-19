#include <iostream>
#include <list>

using namespace std;

int primos [] = {2,3,5,7,11,13,17,19};

void divisores (int n, int div[], int tam){
  for (int i=0; i<tam; i++)
    div [i]=0;
  int i=0;
  while (n!=1){
    while (n%primos [i]==0){
      div [primos [i]]++;
      n/=primos [i];
    }
    i++;
  }
}

void max (int total [], int div [], int tam){
  for (int i=0; i<tam; i++){
    if (div [i] > total [i])
      total [i] = div [i];
  }
}

int main (){
  int num=1;
  int total [20];
  for (int i=0; i<20; i++)
    total [i]=0;
  int div [20];
  for (int i=20; i>=1; i--){
    divisores (i, div, 20);
    max (total, div, 20);
  }
  int resultado=1;
  for (int i=0; i<20; i++){
    while (total [i] > 0){
      resultado *= i;
      total [i]--;
    }
  }
  cout << resultado << endl;
}
